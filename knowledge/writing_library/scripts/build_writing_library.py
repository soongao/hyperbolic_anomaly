#!/usr/bin/env python3
"""Build a writing-oriented library from the paper knowledge base.

This is not a summarizer. It mines short, source-linked writing examples and
groups them by rhetorical function so they can be reused as patterns rather
than copied as prose.
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
WRITING_ROOT = ROOT / "writing_library"
GENERATED = WRITING_ROOT / "generated"
PAPERS_JSONL = ROOT / "metadata" / "papers.jsonl"


CATEGORY_RULES = {
    "task_definition": {
        "terms": [
            "aims to",
            "targets",
            "requires",
            "is a challenging",
            "is an important task",
            "plays a crucial role",
        ],
        "writing_move": "Define the task, then immediately state the operational constraint.",
        "why_useful": "Good for opening an Introduction without generic background.",
    },
    "problem_gap": {
        "terms": [
            "however",
            "nevertheless",
            "fall short",
            "limited",
            "fails to",
            "cannot",
            "requires task-specific",
            "lack",
            "challenging",
        ],
        "writing_move": "Move from known strength to concrete weakness or missing condition.",
        "why_useful": "Good for motivating a new method without overstating novelty.",
    },
    "motivation_bridge": {
        "terms": [
            "motivated by",
            "to address",
            "to tackle",
            "in this paper",
            "we introduce",
            "we propose",
            "the key insight",
            "inspired by",
        ],
        "writing_move": "Connect the diagnosed gap to the proposed design choice.",
        "why_useful": "Good for the last paragraph before contributions or method overview.",
    },
    "contribution_language": {
        "terms": [
            "contributions",
            "we make the following",
            "we summarize",
            "we show",
            "we demonstrate",
            "we design",
            "we further",
        ],
        "writing_move": "State contribution as an action plus its evidence or scope.",
        "why_useful": "Good for contribution bullets and Abstract endings.",
    },
    "method_narrative": {
        "terms": [
            "specifically",
            "first",
            "second",
            "finally",
            "we first",
            "we then",
            "we further",
            "module",
            "framework",
            "pipeline",
        ],
        "writing_move": "Describe modules in the order they answer the problem decomposition.",
        "why_useful": "Good for Method section roadmap paragraphs.",
    },
    "related_work_positioning": {
        "terms": [
            "unlike",
            "different from",
            "in contrast",
            "compared to",
            "existing methods",
            "prior works",
            "recent work",
            "instead of",
        ],
        "writing_move": "Compare along mechanism, assumption, or setting, not only performance.",
        "why_useful": "Good for Related Work and novelty boundary writing.",
    },
    "experiment_evidence": {
        "terms": [
            "experiments",
            "extensive experiments",
            "ablation",
            "demonstrate",
            "validate",
            "achieves",
            "outperforms",
            "benchmarks",
            "datasets",
        ],
        "writing_move": "Tie the experiment to the claim it supports.",
        "why_useful": "Good for Experiments introductions and result paragraphs.",
    },
    "claim_boundary": {
        "terms": [
            "without",
            "does not require",
            "while preserving",
            "while maintaining",
            "only",
            "rather than",
            "instead of",
            "under the",
            "in the zero-shot setting",
        ],
        "writing_move": "Bound the claim by data, supervision, assumptions, or evaluation setting.",
        "why_useful": "Good for avoiding reviewer objections about over-claiming.",
    },
    "limitation_language": {
        "terms": [
            "limitation",
            "future work",
            "may fail",
            "sensitivity",
            "poses",
            "challenging",
            "still",
            "remains",
        ],
        "writing_move": "Name a weakness, then identify the condition under which it matters.",
        "why_useful": "Good for Discussion and rebuttal-safe limitation writing.",
    },
}


SECTION_HINTS = {
    "task_definition": "Introduction opening",
    "problem_gap": "Introduction gap / Related Work",
    "motivation_bridge": "Introduction bridge / Method overview",
    "contribution_language": "Contribution bullets / Abstract",
    "method_narrative": "Method",
    "related_work_positioning": "Related Work",
    "experiment_evidence": "Experiments",
    "claim_boundary": "Abstract / Introduction / Discussion",
    "limitation_language": "Discussion / Limitations",
}


CORE_PRIORITY_WEIGHT = {
    "core": 4,
    "method": 3,
    "supporting": 2,
    "background": 1,
}


@dataclass
class Paper:
    paper_id: str
    title: str
    year: str
    area: str
    priority: str
    text_path: Path
    card_path: str


def load_papers() -> list[Paper]:
    papers: list[Paper] = []
    for line in PAPERS_JSONL.read_text(encoding="utf-8").splitlines():
        item = json.loads(line)
        papers.append(
            Paper(
                paper_id=item["id"],
                title=item["title"],
                year=item["year"],
                area=item["area"],
                priority=item["priority"],
                text_path=ROOT / item["text"],
                card_path=item["card"],
            )
        )
    return papers


def clean_text(raw: str) -> str:
    raw = raw.replace("\x00", " ")
    raw = raw.replace("\x0c", "\n")
    raw = re.sub(r"([A-Za-z])-[\n ]+([a-z])", r"\1\2", raw)
    raw = re.sub(r"\[[0-9,\s]+\]", "", raw)
    raw = re.sub(r"\([A-Z][A-Za-z]+ et al\.,? \d{4}[a-z]?\)", "", raw)
    raw = re.sub(r"\s+", " ", raw)
    return raw.strip()


def split_sentences(text: str) -> list[str]:
    text = clean_text(text)
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z(])", text)
    sentences = []
    for part in parts:
        part = part.strip()
        if not 90 <= len(part) <= 520:
            continue
        if sum(ch.isalpha() for ch in part) < 60:
            continue
        if part.count("|") > 2 or part.count("=") > 3:
            continue
        if re.search(r"^\d+(\.\d+)?\s", part):
            continue
        sentences.append(part)
    return sentences


def term_hits(sentence: str, terms: list[str]) -> int:
    low = sentence.lower()
    return sum(1 for term in terms if term.lower() in low)


def score_sentence(sentence: str, paper: Paper, category: str) -> int:
    rule = CATEGORY_RULES[category]
    score = term_hits(sentence, rule["terms"]) * 5
    score += CORE_PRIORITY_WEIGHT.get(paper.priority, 1)
    if paper.area in {"CLIP / ZSAD", "Frequency / ZSAD", "Hyperbolic", "OT / UOT", "TTA / VLM"}:
        score += 2
    if 140 <= len(sentence) <= 340:
        score += 2
    if any(marker in sentence.lower() for marker in ["we propose", "we introduce", "we show", "however"]):
        score += 1
    return score


def reusable_template(category: str) -> str:
    templates = {
        "task_definition": "[Task] aims to [decision/output] under [data/supervision constraint], where [source of difficulty].",
        "problem_gap": "Although [prior capability] has enabled [benefit], it remains limited because [mechanism/assumption mismatch].",
        "motivation_bridge": "Motivated by [observed failure mode], we formulate [task] as [new decision problem] and introduce [method component].",
        "contribution_language": "We contribute [formulation/component/evidence], which [specific effect] under [setting].",
        "method_narrative": "Specifically, we first [prepare representation], then [define scoring/alignment], and finally [produce decision/evidence].",
        "related_work_positioning": "Unlike [prior family], which [assumption/mechanism], our method [different mechanism] for [target setting].",
        "experiment_evidence": "Experiments on [benchmarks] evaluate [claim], with ablations isolating [mechanism] from [confounder].",
        "claim_boundary": "This claim is restricted to [setting/data/protocol] and does not imply [stronger claim].",
        "limitation_language": "The method may fail when [condition], suggesting that [future evidence/component] is needed.",
    }
    return templates[category]


def build_excerpts(papers: list[Paper]) -> list[dict]:
    candidates: list[dict] = []
    seen = set()
    for paper in papers:
        if not paper.text_path.exists():
            continue
        text = paper.text_path.read_text(encoding="utf-8", errors="replace")
        for sentence in split_sentences(text):
            normalized = re.sub(r"\s+", " ", sentence.lower())
            if normalized in seen:
                continue
            seen.add(normalized)
            for category in CATEGORY_RULES:
                hits = term_hits(sentence, CATEGORY_RULES[category]["terms"])
                if hits == 0:
                    continue
                score = score_sentence(sentence, paper, category)
                if score < 7:
                    continue
                candidates.append(
                    {
                        "category": category,
                        "section_hint": SECTION_HINTS[category],
                        "paper_id": paper.paper_id,
                        "paper_title": paper.title,
                        "year": paper.year,
                        "area": paper.area,
                        "priority": paper.priority,
                        "card": paper.card_path,
                        "score": score,
                        "source_excerpt": sentence,
                        "writing_move": CATEGORY_RULES[category]["writing_move"],
                        "why_useful": CATEGORY_RULES[category]["why_useful"],
                        "reusable_template": reusable_template(category),
                    }
                )

    by_category: dict[str, list[dict]] = defaultdict(list)
    for item in candidates:
        by_category[item["category"]].append(item)

    selected: list[dict] = []
    for category, items in by_category.items():
        items.sort(key=lambda item: (-item["score"], item["paper_id"], item["source_excerpt"]))
        per_paper = Counter()
        for item in items:
            if per_paper[item["paper_id"]] >= 3:
                continue
            selected.append(item)
            per_paper[item["paper_id"]] += 1
            if sum(1 for x in selected if x["category"] == category) >= 45:
                break
    selected.sort(key=lambda item: (item["category"], -item["score"], item["paper_id"]))
    return selected


def write_jsonl(excerpts: list[dict]) -> None:
    path = GENERATED / "excerpts.jsonl"
    with path.open("w", encoding="utf-8") as fh:
        for item in excerpts:
            fh.write(json.dumps(item, ensure_ascii=False) + "\n")


def write_markdown(excerpts: list[dict]) -> None:
    by_category: dict[str, list[dict]] = defaultdict(list)
    for item in excerpts:
        by_category[item["category"]].append(item)

    lines = [
        "# Generated Writing Excerpts",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        "These are source-linked candidates. Use them as pattern evidence, not as copy-paste prose.",
        "",
    ]
    for category in CATEGORY_RULES:
        items = by_category.get(category, [])
        lines.extend(
            [
                f"## {category}",
                "",
                f"Writing move: {CATEGORY_RULES[category]['writing_move']}",
                "",
                f"Reusable template: `{reusable_template(category)}`",
                "",
            ]
        )
        for idx, item in enumerate(items[:30], 1):
            lines.extend(
                [
                    f"### {idx}. {item['paper_id']}",
                    "",
                    f"- Source: [{item['paper_title']}](../{item['card']})",
                    f"- Section use: {item['section_hint']}",
                    f"- Why useful: {item['why_useful']}",
                    f"- Excerpt: \"{item['source_excerpt']}\"",
                    "",
                ]
            )
    (GENERATED / "excerpts_by_category.md").write_text("\n".join(lines), encoding="utf-8")


def write_index(excerpts: list[dict]) -> None:
    counts = Counter(item["category"] for item in excerpts)
    paper_counts = Counter(item["paper_id"] for item in excerpts)
    lines = [
        "# Generated Writing Library Index",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        "## Excerpt Counts By Writing Move",
        "",
        "| Writing move | Count |",
        "|---|---:|",
    ]
    for category in CATEGORY_RULES:
        lines.append(f"| `{category}` | {counts[category]} |")
    lines.extend(["", "## Most Represented Papers", "", "| Paper id | Count |", "|---|---:|"])
    for paper_id, count in paper_counts.most_common(20):
        lines.append(f"| `{paper_id}` | {count} |")
    (GENERATED / "index.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    GENERATED.mkdir(parents=True, exist_ok=True)
    papers = load_papers()
    excerpts = build_excerpts(papers)
    write_jsonl(excerpts)
    write_markdown(excerpts)
    write_index(excerpts)
    print(f"Built writing excerpt bank with {len(excerpts)} excerpts.")


if __name__ == "__main__":
    main()

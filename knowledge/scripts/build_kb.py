#!/usr/bin/env python3
"""Build a human- and agent-friendly paper knowledge base.

The script keeps PDFs as immutable source artifacts and generates:
- extracted full text for grep/RAG-like access
- machine-readable metadata
- one Markdown card per paper
- top-level human and agent guides
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
import subprocess
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
PDF_DIR = ROOT / "PDFs"
TEXT_DIR = ROOT / "text"
CARD_DIR = ROOT / "cards"
META_DIR = ROOT / "metadata"
MANIFEST = ROOT / "manifests" / "download_manifest.md"


TITLE_OVERRIDES = {
    "Batzner_2024_EfficientAD.pdf": "EfficientAD: Accurate Visual Anomaly Detection at Millisecond-Level Latencies",
    "Cao_2023_SegmentAnyAnomaly.pdf": "Segment Any Anomaly without Training via Hybrid Prompt Regularization",
    "Cao_2023_VAND_SAA_Report.pdf": "2nd Place Winning Solution for the CVPR2023 VAND Challenge: Multimodal Prompting for Data-centric Anomaly Detection",
    "Chen_2023_APRIL-GAN.pdf": "APRIL-GAN: A Zero-/Few-Shot Anomaly Classification and Segmentation Method for CVPR 2023 VAND Workshop Challenge",
    "Chizat_2018_UnbalancedOptimalTransport.pdf": "Scaling Algorithms for Unbalanced Optimal Transport Problems",
    "Compositional_2024_HyperbolicVLMEntailment.pdf": "Compositional Entailment Learning for Hyperbolic Vision-Language Models",
    "Courty_2017_OptimalTransportDomainAdaptation.pdf": "Optimal Transport for Domain Adaptation",
    "Cuturi_2013_SinkhornDistances.pdf": "Sinkhorn Distances: Lightspeed Computation of Optimal Transport",
    "Daubechies_2011_SynchrosqueezedWaveletTransforms.pdf": "Synchrosqueezed Wavelet Transforms: An Empirical Mode Decomposition-like Tool",
    "Defard_2021_PaDiM.pdf": "PaDiM: A Patch Distribution Modeling Framework for Anomaly Detection and Localization",
    "Deng_2022_ReverseDistillation.pdf": "Anomaly Detection via Reverse Distillation from One-Class Embedding",
    "Desai_2023_MERU.pdf": "MERU: Multimodal Poincare Embeddings for Text-Image Representation",
    "Ganea_2018_HyperbolicEntailmentCones.pdf": "Hyperbolic Entailment Cones for Learning Hierarchical Embeddings",
    "Ganea_2018_HyperbolicNeuralNetworks.pdf": "Hyperbolic Neural Networks",
    "Gao_2025_MetaUAS.pdf": "MetaUAS: Universal Anomaly Segmentation with One-Prompt Meta-Learning",
    "Gu_2023_AnomalyGPT.pdf": "AnomalyGPT: Detecting Industrial Anomalies Using Large Vision-Language Models",
    "Gu_2024_FiLo.pdf": "FiLo: Zero-Shot Anomaly Detection by Fine-Grained Description and High-Quality Localization",
    "HADNet_2025_ScientificReports.pdf": "HADNet: Hyperbolic Geometry Enhanced Feature Filtering Network for Industrial Anomaly Detection",
    "Jeong_2023_WinCLIP.pdf": "WinCLIP: Zero-/Few-Shot Anomaly Classification and Segmentation",
    "Li_2024_HypAD.pdf": "Hyperbolic Anomaly Detection",
    "Li_2024_PromptAD.pdf": "PromptAD: Learning Prompts with only Normal Samples for Few-Shot Anomaly Detection",
    "Liu_2018_MultiLevelWaveletCNN.pdf": "Multi-Level Wavelet-CNN for Image Restoration",
    "Long_2020_SearchingActionsHyperbole.pdf": "Searching for Actions on the Hyperbole",
    "Ma_2025_AA-CLIP.pdf": "AA-CLIP: Enhancing Zero-shot Anomaly Detection via Anomaly-Aware CLIP",
    "Mallat_2012_GroupInvariantScattering.pdf": "Group Invariant Scattering",
    "Nickel_2017_PoincareEmbeddings.pdf": "Poincare Embeddings for Learning Hierarchical Representations",
    "Niu_2023_SAR.pdf": "Towards Stable Test-Time Adaptation in Dynamic Wild World",
    "Peyre_2019_ComputationalOptimalTransport.pdf": "Computational Optimal Transport",
    "Poudineh_2026_DevPrompt.pdf": "DevPrompt: Deviation-Based Prompt Learning for One-Normal Shot Image Anomaly Detection",
    "Qin_2021_FcaNet.pdf": "FcaNet: Frequency Channel Attention Networks",
    "Qiu_2026_FreqAnchorAD.pdf": "FreqAnchorAD: Language-Free Zero-Shot Anomaly Detection via Frequency-Deviation Anchoring",
    "Qu_2024_VCP-CLIP.pdf": "VCP-CLIP: A Visual Context Prompting Model for Zero-Shot Anomaly Segmentation",
    "Radford_2021_CLIP.pdf": "Learning Transferable Visual Models From Natural Language Supervision",
    "Ramasinghe_2024_AcceptModalityGapHyperbolic.pdf": "Accept the Modality Gap: An Exploration in the Hyperbolic Space",
    "Roth_2022_PatchCore.pdf": "Towards Total Recall in Industrial Anomaly Detection",
    "Shu_2022_TPT.pdf": "Test-Time Prompt Tuning for Zero-Shot Generalization in Vision-Language Models",
    "Wang_2021_TENT.pdf": "Tent: Fully Test-Time Adaptation by Entropy Minimization",
    "Wang_2022_CoTTA.pdf": "Continual Test-Time Domain Adaptation",
    "Wang_2024_Real-IAD.pdf": "Real-IAD: A Real-World Multi-View Dataset for Benchmarking Versatile Industrial Anomaly Detection",
    "Yao_2024_AdaCLIP.pdf": "AdaCLIP: Adapting CLIP with Hybrid Learnable Prompts for Zero-Shot Anomaly Detection",
    "You_2022_UniAD.pdf": "A Unified Model for Multi-class Anomaly Detection",
    "Zavrtanik_2021_DRAEM.pdf": "DRAEM: A Discriminatively Trained Reconstruction Embedding for Surface Anomaly Detection",
    "Zhang_2022_MEMO.pdf": "MEMO: Test Time Robustness via Adaptation and Augmentation",
    "Zhou_2022_CoCoOp.pdf": "Conditional Prompt Learning for Vision-Language Models",
    "Zhou_2022_CoOp.pdf": "Learning to Prompt for Vision-Language Models",
    "Zhou_2024_AnomalyCLIP.pdf": "AnomalyCLIP: Object-agnostic Prompt Learning for Zero-shot Anomaly Detection",
}


PRIORITY_OVERRIDES = {
    "Jeong_2023_WinCLIP.pdf": "core",
    "Zhou_2024_AnomalyCLIP.pdf": "core",
    "Yao_2024_AdaCLIP.pdf": "core",
    "Gu_2024_FiLo.pdf": "core",
    "Qu_2024_VCP-CLIP.pdf": "core",
    "Ma_2025_AA-CLIP.pdf": "core",
    "Chen_2023_APRIL-GAN.pdf": "core",
    "Li_2024_PromptAD.pdf": "core",
    "Li_2024_HypAD.pdf": "core",
    "HADNet_2025_ScientificReports.pdf": "core",
    "Qiu_2026_FreqAnchorAD.pdf": "core",
    "Cuturi_2013_SinkhornDistances.pdf": "method",
    "Chizat_2018_UnbalancedOptimalTransport.pdf": "method",
    "Peyre_2019_ComputationalOptimalTransport.pdf": "method",
    "Ganea_2018_HyperbolicEntailmentCones.pdf": "method",
    "Nickel_2017_PoincareEmbeddings.pdf": "method",
    "Shu_2022_TPT.pdf": "method",
    "Wang_2021_TENT.pdf": "method",
}


KEYWORD_TAGS = {
    "CLIP": "clip",
    "ZSAD": "zsad",
    "Zero-Shot": "zero-shot",
    "Zero-/Few-Shot": "zero-shot",
    "Anomaly": "anomaly-detection",
    "Prompt": "prompt-learning",
    "Hyperbolic": "hyperbolic",
    "Poincare": "hyperbolic",
    "Entailment": "entailment",
    "Optimal Transport": "optimal-transport",
    "Unbalanced": "uot",
    "Sinkhorn": "optimal-transport",
    "Wavelet": "frequency",
    "Frequency": "frequency",
    "Scattering": "frequency",
    "Test-Time": "tta",
    "TENT": "tta",
    "Domain Adaptation": "domain-adaptation",
    "Vision-Language": "vlm",
    "Large Vision-Language": "lvlm",
    "Segment Any": "sam",
    "Industrial": "industrial-ad",
}


@dataclass
class Paper:
    paper_id: str
    filename: str
    title: str
    year: str
    area: str
    source: str
    pdf_path: Path
    text_path: Path
    card_path: Path
    tags: list[str]
    priority: str
    pages: int | None = None
    bytes: int = 0
    sha256: str = ""
    abstract: str = ""


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return re.sub(r"-+", "-", value).strip("-")


def parse_manifest_rows() -> dict[str, tuple[str, str]]:
    rows: dict[str, tuple[str, str]] = {}
    in_downloaded = False
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        if line.startswith("## Downloaded PDFs"):
            in_downloaded = True
            continue
        if line.startswith("## Not Downloaded"):
            break
        if not in_downloaded or not line.startswith("|"):
            continue
        parts = [part.strip() for part in line.strip().strip("|").split("|")]
        if len(parts) != 3 or parts[0] in {"Area", "---"}:
            continue
        area, file_cell, source = parts
        filename = file_cell.strip("`")
        rows[filename] = (area, source)
    return rows


def run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, text=True, capture_output=True, check=False)


def pdf_pages(pdf_path: Path) -> int | None:
    result = run(["pdfinfo", str(pdf_path)])
    if result.returncode != 0:
        return None
    match = re.search(r"^Pages:\s+(\d+)", result.stdout, re.MULTILINE)
    return int(match.group(1)) if match else None


def extract_text(pdf_path: Path, text_path: Path) -> None:
    if text_path.exists() and text_path.stat().st_mtime >= pdf_path.stat().st_mtime:
        return
    result = run(["pdftotext", "-layout", "-enc", "UTF-8", str(pdf_path), str(text_path)])
    if result.returncode != 0:
        fallback = run(["pdftotext", "-enc", "UTF-8", str(pdf_path), str(text_path)])
        if fallback.returncode != 0:
            text_path.write_text("", encoding="utf-8")


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def normalize_text(text: str) -> str:
    text = text.replace("\x0c", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def extract_abstract(text: str) -> str:
    compact = normalize_text(text[:35000])
    match = re.search(
        r"(?is)\babstract\b\s*[:.\-\u2014]?\s*(.+?)(?:\n\s*(?:1\s+)?(?:introduction|keywords|index terms)\b)",
        compact,
    )
    if match:
        abstract = re.sub(r"\s+", " ", match.group(1)).strip()
        abstract = re.sub(r"^(Abstract|ABSTRACT)\s*[:.\-\u2014]?\s*", "", abstract)
        if len(abstract) > 120:
            return abstract[:2500]

    lines = text[:35000].replace("\x0c", "\n").splitlines()

    def compressed_letters(line: str) -> str:
        return re.sub(r"[^A-Za-z]", "", line).lower()

    start = None
    for idx, line in enumerate(lines):
        letters = compressed_letters(line)
        if letters == "abstract" or letters.startswith("abstract"):
            start = idx + 1
            break
    if start is None:
        return ""

    collected: list[str] = []
    for line in lines[start:]:
        letters = compressed_letters(line)
        if letters in {"introduction", "keywords", "indexterms"}:
            break
        if letters.startswith("introduction"):
            break
        if re.match(r"^\s*\d+\s+[A-Z ]*I\s*N\s*T\s*R\s*O", line):
            break
        stripped = line.strip()
        if not stripped:
            if collected:
                collected.append(" ")
            continue
        if stripped.startswith("arXiv:"):
            continue
        stripped = re.split(r"Figure\s+\d+\.?", stripped, maxsplit=1)[0].strip()
        if not stripped:
            break
        collected.append(stripped)

    abstract = " ".join(collected)
    abstract = re.sub(r"-\s+", "", abstract)
    abstract = re.sub(r"\s+", " ", abstract).strip()
    abstract = re.sub(r"^(Abstract|ABSTRACT)\s*[:.\-]?\s*", "", abstract)
    return abstract[:2500] if len(abstract) > 120 else ""


def infer_year(filename: str) -> str:
    match = re.search(r"_(20\d{2})_", filename)
    if match:
        return match.group(1)
    return ""


def tags_for(area: str, title: str, filename: str) -> list[str]:
    tags = {slugify(area)}
    haystack = f"{area} {title} {filename}"
    for keyword, tag in KEYWORD_TAGS.items():
        if keyword.lower() in haystack.lower():
            tags.add(tag)
    if "ZSAD" in filename or "Zero-Shot" in title or "Zero-shot" in title:
        tags.add("zsad")
    return sorted(tags)


def priority_for(filename: str, area: str) -> str:
    if filename in PRIORITY_OVERRIDES:
        return PRIORITY_OVERRIDES[filename]
    if any(key in area.lower() for key in ["clip", "zsad", "hyperbolic", "frequency"]):
        return "supporting"
    return "background"


def build_paper(pdf_path: Path, manifest_rows: dict[str, tuple[str, str]]) -> Paper:
    filename = pdf_path.name
    area, source = manifest_rows.get(filename, ("Unclassified", "local"))
    title = TITLE_OVERRIDES.get(filename, pdf_path.stem.replace("_", " "))
    year = infer_year(filename)
    paper_id = slugify(pdf_path.stem)
    text_path = TEXT_DIR / f"{paper_id}.txt"
    card_path = CARD_DIR / f"{paper_id}.md"
    extract_text(pdf_path, text_path)
    text = text_path.read_text(encoding="utf-8", errors="replace") if text_path.exists() else ""
    return Paper(
        paper_id=paper_id,
        filename=filename,
        title=title,
        year=year,
        area=area,
        source=source,
        pdf_path=pdf_path,
        text_path=text_path,
        card_path=card_path,
        tags=tags_for(area, title, filename),
        priority=priority_for(filename, area),
        pages=pdf_pages(pdf_path),
        bytes=pdf_path.stat().st_size,
        sha256=file_sha256(pdf_path),
        abstract=extract_abstract(text),
    )


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def yaml_list(items: Iterable[str]) -> str:
    return "[" + ", ".join(json.dumps(item, ensure_ascii=False) for item in items) + "]"


def card_markdown(paper: Paper) -> str:
    abstract = paper.abstract or "_Abstract not extracted reliably yet. Use the text file for source reading._"
    return f"""---
id: {paper.paper_id}
title: {json.dumps(paper.title, ensure_ascii=False)}
year: {json.dumps(paper.year)}
area: {json.dumps(paper.area, ensure_ascii=False)}
priority: {json.dumps(paper.priority)}
tags: {yaml_list(paper.tags)}
status: unread
pdf: {json.dumps(rel(paper.pdf_path), ensure_ascii=False)}
text: {json.dumps(rel(paper.text_path), ensure_ascii=False)}
source: {json.dumps(paper.source, ensure_ascii=False)}
pages: {paper.pages if paper.pages is not None else "null"}
bytes: {paper.bytes}
sha256: {paper.sha256}
---

# {paper.title}

## Why This Paper Is Here

- Area: `{paper.area}`
- Priority: `{paper.priority}`
- Use this card as the human entry point. Use the extracted text for exact evidence.

## Abstract

{abstract}

## Reading Notes

- Main problem:
- Core idea:
- Key method components:
- Datasets / protocol:
- Important results:
- Limitations:
- Relevance to ZSAD improvement:
- Possible experiments to borrow:

## Agent Use

- PDF: [`{paper.filename}`](../{rel(paper.pdf_path)})
- Extracted text: [`{paper.text_path.name}`](../{rel(paper.text_path)})
- Suggested grep queries:
  - `{paper.title.split(':')[0]}`
  - `ablation`
  - `limitation`
  - `MVTec`
  - `VisA`

## Evidence Log

Add page-anchored findings here when this paper is read.

| Claim / note | Page | Evidence quote |
|---|---:|---|
| | | |
"""


def write_metadata(papers: list[Paper]) -> None:
    jsonl_path = META_DIR / "papers.jsonl"
    with jsonl_path.open("w", encoding="utf-8") as fh:
        for paper in papers:
            item = {
                "id": paper.paper_id,
                "title": paper.title,
                "year": paper.year,
                "area": paper.area,
                "priority": paper.priority,
                "tags": paper.tags,
                "status": "unread",
                "pdf": rel(paper.pdf_path),
                "text": rel(paper.text_path),
                "card": rel(paper.card_path),
                "source": paper.source,
                "pages": paper.pages,
                "bytes": paper.bytes,
                "sha256": paper.sha256,
                "abstract": paper.abstract,
            }
            fh.write(json.dumps(item, ensure_ascii=False) + "\n")

    csv_path = META_DIR / "papers.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=[
                "id",
                "title",
                "year",
                "area",
                "priority",
                "tags",
                "status",
                "pdf",
                "text",
                "card",
                "source",
                "pages",
                "bytes",
                "sha256",
            ],
        )
        writer.writeheader()
        for paper in papers:
            writer.writerow(
                {
                    "id": paper.paper_id,
                    "title": paper.title,
                    "year": paper.year,
                    "area": paper.area,
                    "priority": paper.priority,
                    "tags": ";".join(paper.tags),
                    "status": "unread",
                    "pdf": rel(paper.pdf_path),
                    "text": rel(paper.text_path),
                    "card": rel(paper.card_path),
                    "source": paper.source,
                    "pages": paper.pages or "",
                    "bytes": paper.bytes,
                    "sha256": paper.sha256,
                }
            )


def write_indexes(papers: list[Paper]) -> None:
    grouped: dict[str, list[Paper]] = {}
    for paper in papers:
        grouped.setdefault(paper.area, []).append(paper)

    index_lines = [
        "# ZSAD Knowledge Base",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        "This knowledge base is organized for both human reading and agent retrieval.",
        "",
        "## Fast Entry Points",
        "",
        "- `PDFs/`: original downloaded PDFs.",
        "- `text/`: extracted full text, one file per PDF, optimized for `rg` search.",
        "- `cards/`: one Markdown card per paper with metadata, abstract, and reading-note slots.",
        "- `metadata/papers.jsonl`: agent-friendly paper registry.",
        "- `metadata/papers.csv`: spreadsheet-friendly paper registry.",
        "- `agent_guide.md`: rules for future agents using this knowledge base.",
        "- `human_guide.md`: practical reading workflow for humans.",
        "- `taxonomy.md`: topic clusters and recommended first-pass reading order.",
        "",
        "## Papers By Area",
        "",
    ]
    for area in sorted(grouped):
        index_lines.append(f"### {area}")
        index_lines.append("")
        index_lines.append("| Priority | Year | Paper | Card | PDF | Text |")
        index_lines.append("|---|---:|---|---|---|---|")
        for paper in sorted(grouped[area], key=lambda p: (p.priority, p.year, p.title)):
            index_lines.append(
                f"| `{paper.priority}` | {paper.year} | {paper.title} | "
                f"[card]({rel(paper.card_path)}) | [pdf]({rel(paper.pdf_path)}) | [text]({rel(paper.text_path)}) |"
            )
        index_lines.append("")
    (ROOT / "README.md").write_text("\n".join(index_lines), encoding="utf-8")

    agent_guide = """# Agent Guide

Use this folder as a local literature memory, not as a black-box summary.

## Retrieval Order

1. Start from `metadata/papers.jsonl` for title, area, tags, priority, and file paths.
2. Use `rg` over `text/` for exact claims, method details, datasets, ablations, and limitations.
3. Open the matching `cards/*.md` for human notes and page-anchored evidence.
4. Use the original PDF only when layout, equations, figures, or tables matter.

## Grounding Rules

- Do not cite a card note as evidence unless it has an Evidence Log entry.
- Prefer exact quotes from `text/` plus PDF page checks for important claims.
- Keep new notes scoped to a paper card unless they synthesize multiple papers.
- When adding a cross-paper synthesis, link to every supporting card and name the evidence status.

## Common Queries

```bash
rg -n "MVTec|VisA|MPDD|BTAD" knowledge/text
rg -n "zero-shot|few-shot|training-free|prompt" knowledge/text
rg -n "ablation|limitation|failure|sensitivity" knowledge/text
rg -n "hyperbolic|Poincare|entailment|cone" knowledge/text
rg -n "optimal transport|unbalanced|Sinkhorn|partial" knowledge/text
rg -n "frequency|wavelet|scattering|Fourier" knowledge/text
```

## Status Convention

Use these values in card frontmatter when updating reading progress:

- `unread`
- `skimmed`
- `read`
- `summarized`
- `excluded`

Use `priority` for triage, not quality:

- `core`: closest to the ZSAD research direction.
- `method`: transferable method backbone.
- `supporting`: useful context or adjacent work.
- `background`: baseline or general reference.
"""
    (ROOT / "agent_guide.md").write_text(agent_guide, encoding="utf-8")
    (ROOT / "AGENTS.md").write_text(
        """# Knowledge Base Agent Instructions

This folder is a paper knowledge base for ZSAD and adjacent methods.

## Required Retrieval Order

1. Read `metadata/papers.jsonl` or `README.md` to locate candidate papers.
2. Search `text/` with `rg` for exact evidence.
3. Open the relevant `cards/*.md` for curated notes and reading status.
4. Open PDFs only for figures, equations, tables, or page validation.

## Evidence Discipline

- Do not treat extracted text as perfectly structured; PDF two-column extraction can interleave captions.
- For important claims, verify against the PDF page and add the quote to the card's `Evidence Log`.
- Keep machine-readable paths relative to this folder.
- Do not overwrite human notes in cards unless explicitly asked; if rebuilding, preserve manual notes first.

## Update Rules

- Add new PDFs to `PDFs/`.
- Add or update the row in `manifests/download_manifest.md`.
- Run `python3 scripts/build_kb.py`.
- If the script overwrites a card that already has human notes, merge the notes back manually.
""",
        encoding="utf-8",
    )

    human_guide = """# Human Guide

This KB is meant to support fast screening first, then deeper reading.

## Recommended Workflow

1. Read `taxonomy.md` to pick a cluster.
2. Open the corresponding cards in `cards/`.
3. Fill only the `Reading Notes` bullets that matter for the current research decision.
4. Add page-anchored quotes to `Evidence Log` when a claim will be reused in a paper.
5. Promote useful cross-paper insights into a separate synthesis note under `syntheses/`.

## First Screening Questions

- Is this a direct ZSAD baseline, a mechanism prior, or only background?
- Does it require target-domain normal samples, anomaly samples, or training?
- Does it report MVTec AD / VisA under a comparable setting?
- What part can be borrowed: prompt, scoring, feature geometry, adaptation, frequency processing, or transport?
- What claim would it weaken in a new paper?
"""
    (ROOT / "human_guide.md").write_text(human_guide, encoding="utf-8")

    queries = """# Query Cookbook

Use these commands from the repository root.

## Baselines And Protocols

```bash
rg -n "MVTec|VisA|MPDD|BTAD|DAGM|Real-IAD" knowledge/text
rg -n "zero-shot|few-shot|one-shot|training-free|train once" knowledge/text
rg -n "image-level|pixel-level|AUROC|AUPRO|PRO|AP" knowledge/text
```

## Mechanism Evidence

```bash
rg -n "prompt|normal prompt|abnormal prompt|state word|template" knowledge/text
rg -n "patch|window|local feature|dense feature|segmentation map" knowledge/text
rg -n "ablation|sensitivity|limitation|failure|false positive" knowledge/text
```

## Candidate Improvement Directions

```bash
rg -n "hyperbolic|Poincare|entailment|cone|hierarchy" knowledge/text
rg -n "optimal transport|unbalanced|Sinkhorn|partial|mass" knowledge/text
rg -n "test-time|entropy|minimization|adaptation|augmentation" knowledge/text
rg -n "frequency|Fourier|wavelet|scattering|high-frequency|low-frequency" knowledge/text
```

## Agent Metadata Queries

```bash
python3 - <<'PY'
import json
for line in open('knowledge/metadata/papers.jsonl'):
    p = json.loads(line)
    if p['priority'] == 'core':
        print(p['id'], '|', p['title'])
PY
```
"""
    (ROOT / "queries.md").write_text(queries, encoding="utf-8")

    (ROOT / "syntheses" / "README.md").write_text(
        """# Syntheses

Put cross-paper synthesis notes here.

Recommended files:

- `zsad_baseline_matrix.md`
- `hyperbolic_uot_opportunity_map.md`
- `frequency_tta_opportunity_map.md`
- `benchmark_protocol_notes.md`

Each synthesis should cite paper cards and include evidence status:

- `source-quoted`: supported by a card Evidence Log quote.
- `text-searched`: supported by extracted text search but not yet page-checked.
- `inferred`: your interpretation, needs validation.
""",
        encoding="utf-8",
    )

    taxonomy = """# Taxonomy And Reading Queue

## 1. Direct CLIP / ZSAD Baselines

Start here for comparison and novelty boundaries:

- WinCLIP
- AnomalyCLIP
- APRIL-GAN / VAND reports
- PromptAD
- AdaCLIP
- FiLo
- VCP-CLIP
- AA-CLIP
- FreqAnchorAD
- DevPrompt

## 2. Foundation-Model Anomaly Segmentation

Use these to understand SAM/LVLM alternatives and prompt-free or prompt-minimal directions:

- AnomalyGPT
- Segment Any Anomaly / SAA+
- MetaUAS

## 3. Hyperbolic / Entailment Mechanisms

Use these for geometry and semantic decision-rule design:

- Poincare Embeddings
- Hyperbolic Entailment Cones
- Hyperbolic Neural Networks
- Searching for Actions on the Hyperbole
- MERU
- Accept the Modality Gap
- Compositional Hyperbolic VLM Entailment
- HypAD
- HADNet

## 4. OT / UOT Mechanisms

Use these for rejectable matching, unmatched mass, and transport-cost design:

- Sinkhorn Distances
- Optimal Transport for Domain Adaptation
- Scaling Algorithms for Unbalanced OT
- Computational Optimal Transport

## 5. TTA / Adaptation

Use these for inference-time or lightweight adaptation:

- TENT
- CoTTA
- MEMO
- SAR
- Test-Time Prompt Tuning

## 6. Frequency / Wavelet Priors

Use these for local texture, frequency-deviation, and multi-scale feature design:

- Synchrosqueezed Wavelet Transforms
- Group Invariant Scattering
- Multi-Level Wavelet-CNN
- FcaNet
- FreqAnchorAD

## 7. Non-CLIP Industrial AD Baselines

Use these to avoid over-claiming against established non-VLM methods:

- PaDiM
- PatchCore
- DRAEM
- Reverse Distillation
- UniAD
- EfficientAD
- Real-IAD
"""
    (ROOT / "taxonomy.md").write_text(taxonomy, encoding="utf-8")


def main() -> None:
    for path in (TEXT_DIR, CARD_DIR, META_DIR, ROOT / "syntheses"):
        path.mkdir(parents=True, exist_ok=True)

    manifest_rows = parse_manifest_rows()
    papers = [build_paper(pdf, manifest_rows) for pdf in sorted(PDF_DIR.glob("*.pdf"))]

    for paper in papers:
        paper.card_path.write_text(card_markdown(paper), encoding="utf-8")

    write_metadata(papers)
    write_indexes(papers)
    print(f"Built knowledge base for {len(papers)} papers under {ROOT}")


if __name__ == "__main__":
    main()

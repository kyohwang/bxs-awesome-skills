#!/usr/bin/env python3
"""Discussions -> comments/*.yaml sync skeleton.

Design goal:
- Keep GitHub Discussions as user entrypoint.
- Sync approved summaries into comments/<slug>.yaml for UI display.

Current scope (skeleton):
- Supports importing a local JSON export via --input-json.
- Output is normalized YAML grouped by skill slug.
- GitHub live fetch is intentionally left as TODO for next step.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from datetime import datetime, UTC
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
COMMENTS_DIR = ROOT / "comments"


def now_iso() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def load_slugs() -> set[str]:
    skills_yaml = ROOT / "catalog" / "skills.yaml"
    data = yaml.safe_load(skills_yaml.read_text(encoding="utf-8"))
    return {item["slug"] for item in data.get("skills", [])}


def normalize_item(item: dict[str, Any]) -> dict[str, Any]:
    return {
        "comment_id": item.get("comment_id", ""),
        "author": item.get("author", "github:unknown"),
        "type": item.get("type", "review"),
        "rating": item.get("rating", 0),
        "content": item.get("content", ""),
        "source_type": "discussion",
        "source_url": item.get("source_url", ""),
        "status": item.get("status", "approved"),
        "submitted_at": item.get("submitted_at", ""),
        "reviewed_by": item.get("reviewed_by", "github:maintainer"),
        "reviewed_at": item.get("reviewed_at", now_iso()),
        "verdict": item.get("verdict", "wait_and_see"),
    }


def write_comments(slug: str, items: list[dict[str, Any]], dry_run: bool) -> None:
    out = {
        "skill_slug": slug,
        "updated_at": now_iso(),
        "comments": items,
    }
    path = COMMENTS_DIR / f"{slug}.yaml"
    if dry_run:
        print(f"[dry-run] would write {path} ({len(items)} comments)")
        return
    path.write_text(yaml.safe_dump(out, sort_keys=False, allow_unicode=True), encoding="utf-8")
    print(f"updated {path} ({len(items)} comments)")


def sync_from_json(input_json: Path, dry_run: bool) -> int:
    payload = json.loads(input_json.read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        print("Input JSON must be a list of discussion-summary objects")
        return 1

    known_slugs = load_slugs()
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)

    for item in payload:
        if not isinstance(item, dict):
            continue
        slug = item.get("skill_slug")
        if slug not in known_slugs:
            print(f"skip unknown skill_slug: {slug}")
            continue
        status = item.get("status", "approved")
        if status != "approved":
            continue
        grouped[slug].append(normalize_item(item))

    for slug in sorted(known_slugs):
        items = grouped.get(slug, [])[:3]
        write_comments(slug, items, dry_run)

    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync discussion summaries into comments YAML")
    parser.add_argument("--input-json", type=Path, help="Path to exported discussion summaries JSON")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if not args.input_json:
        print("TODO: GitHub API live fetch is not implemented in this skeleton.")
        print("Use --input-json with exported discussion summary data for now.")
        return 2

    if not args.input_json.exists():
        print(f"Input JSON not found: {args.input_json}")
        return 1

    return sync_from_json(args.input_json, args.dry_run)


if __name__ == "__main__":
    raise SystemExit(main())

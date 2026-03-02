#!/usr/bin/env python3
"""Minimal repository validation for bxs-awesome-skills.

Checks:
- YAML files are parseable.
- catalog/categories.yaml and catalog/skills.yaml required fields.
- Category references are valid.
- Local paths/profile paths/comments files exist for each skill.
- Basic README.md local markdown link sanity.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]

SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
URL_RE = re.compile(r"^https?://")

ALLOWED_STATUS = {
    "candidate",
    "under_review",
    "verified",
    "deprecated",
    "archived",
}
ALLOWED_SECURITY = {"A", "B", "C", "D"}
ALLOWED_COMPLEXITY = {"low", "medium", "high"}


class ValidationError(Exception):
    pass


def load_yaml(path: Path) -> Any:
    if not path.exists():
        raise ValidationError(f"Missing file: {path}")
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def require_key(obj: dict[str, Any], key: str, where: str) -> Any:
    if key not in obj:
        raise ValidationError(f"Missing key `{key}` in {where}")
    return obj[key]


def validate_categories() -> tuple[list[dict[str, Any]], set[str]]:
    data = load_yaml(ROOT / "catalog" / "categories.yaml")
    cats = require_key(data, "categories", "catalog/categories.yaml")
    if not isinstance(cats, list) or not cats:
        raise ValidationError("`categories` must be a non-empty list")

    ids: set[str] = set()
    zh_names: set[str] = set()

    for i, cat in enumerate(cats):
        where = f"catalog/categories.yaml categories[{i}]"
        if not isinstance(cat, dict):
            raise ValidationError(f"{where} must be object")
        cat_id = require_key(cat, "id", where)
        name = require_key(cat, "name", where)
        zh = require_key(name, "zh", where + ".name")

        if cat_id in ids:
            raise ValidationError(f"Duplicate category id: {cat_id}")
        ids.add(cat_id)

        if zh in zh_names:
            raise ValidationError(f"Duplicate category zh name: {zh}")
        zh_names.add(zh)

    return cats, zh_names


def validate_skill_entry(skill: dict[str, Any], zh_categories: set[str], idx: int) -> None:
    where = f"catalog/skills.yaml skills[{idx}]"
    required = [
        "slug",
        "name",
        "summary",
        "source_type",
        "local_path",
        "profile_path",
        "category",
        "tags",
        "status",
        "install_complexity",
        "quality_score",
        "security_grade",
    ]
    for key in required:
        require_key(skill, key, where)

    slug = skill["slug"]
    if not isinstance(slug, str) or not SLUG_RE.match(slug):
        raise ValidationError(f"Invalid slug `{slug}` in {where}")

    name = skill["name"]
    summary = skill["summary"]
    if not isinstance(name, dict) or not name.get("zh"):
        raise ValidationError(f"{where}.name.zh is required")
    if not isinstance(summary, dict) or not summary.get("zh"):
        raise ValidationError(f"{where}.summary.zh is required")

    status = skill["status"]
    if status not in ALLOWED_STATUS:
        raise ValidationError(f"Invalid status `{status}` in {where}")

    security_grade = skill["security_grade"]
    if security_grade not in ALLOWED_SECURITY:
        raise ValidationError(f"Invalid security_grade `{security_grade}` in {where}")

    complexity = skill["install_complexity"]
    if complexity not in ALLOWED_COMPLEXITY:
        raise ValidationError(f"Invalid install_complexity `{complexity}` in {where}")

    categories = skill["category"]
    if not isinstance(categories, list) or not categories:
        raise ValidationError(f"{where}.category must be non-empty list")
    for c in categories:
        if c not in zh_categories:
            raise ValidationError(f"Unknown category `{c}` in {where}")

    source_type = skill["source_type"]
    if source_type not in {"local", "external"}:
        raise ValidationError(f"Invalid source_type `{source_type}` in {where}")

    local_path = ROOT / skill["local_path"]
    profile_path = ROOT / skill["profile_path"]

    if source_type == "local":
        if not local_path.exists():
            raise ValidationError(f"Missing local_path `{local_path}` for {slug}")
        if not (local_path / "SKILL.md").exists():
            raise ValidationError(f"Missing SKILL.md in local_path for {slug}")
        if not (local_path / "skill.json").exists():
            raise ValidationError(f"Missing skill.json in local_path for {slug}")

    if source_type == "external":
        source_url = skill.get("source_url")
        if not isinstance(source_url, str) or not URL_RE.match(source_url):
            raise ValidationError(f"external skill `{slug}` must provide source_url")

    if not profile_path.exists():
        raise ValidationError(f"Missing profile_path `{profile_path}` for {slug}")

    comment_path = ROOT / "comments" / f"{slug}.yaml"
    if not comment_path.exists():
        raise ValidationError(f"Missing comment file `{comment_path}` for {slug}")


LOCAL_LINK_RE = re.compile(r"\]\(([^)]+)\)")


def validate_readme_links() -> None:
    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")

    for m in LOCAL_LINK_RE.finditer(text):
        link = m.group(1).strip()
        if not link or link.startswith("http") or link.startswith("#") or link.startswith("mailto:"):
            continue
        target = ROOT / link
        if not target.exists():
            raise ValidationError(f"Broken local link in README.md: {link}")


def main() -> int:
    try:
        _, zh_categories = validate_categories()
        skills_data = load_yaml(ROOT / "catalog" / "skills.yaml")
        skills = require_key(skills_data, "skills", "catalog/skills.yaml")
        if not isinstance(skills, list) or not skills:
            raise ValidationError("`skills` must be a non-empty list")

        seen_slugs: set[str] = set()
        for i, skill in enumerate(skills):
            if not isinstance(skill, dict):
                raise ValidationError(f"catalog/skills.yaml skills[{i}] must be object")
            slug = skill.get("slug")
            if slug in seen_slugs:
                raise ValidationError(f"Duplicate skill slug `{slug}`")
            seen_slugs.add(slug)
            validate_skill_entry(skill, zh_categories, i)

        validate_readme_links()

    except ValidationError as e:
        print(f"VALIDATION_ERROR: {e}")
        return 1

    print("Validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

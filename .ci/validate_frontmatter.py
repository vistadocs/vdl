#!/usr/bin/env python3
"""Self-contained frontmatter validator for the vistadocs/vdl corpus repo.

Zero dependencies beyond PyYAML. Mirrors the rules enforced by the vista-docs
pipeline (src/vista_docs/validate/frontmatter.py) so the published corpus is
gated independently — on every push/PR (GitHub Actions) and locally (pre-push
hook). A broken corpus can never be published.

Usage:
    python3 .ci/validate_frontmatter.py [ROOT]   # ROOT defaults to repo root

Exits non-zero if any document has a hard violation.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

REQUIRED_KEYS = ("title", "doc_type", "doc_label", "app_code", "app_name", "section", "pkg_ns")
VALID_SECTIONS = {"CLI", "FIN", "GUI", "INF", "MON"}
LEGACY_ONLY_KEYS = {
    "consolidated_title",
    "master_source",
    "prior_versions",
    "consolidated_from",
    "master_pub_date",
}
SCALAR_FIELDS = ("description", "audience", "title", "doc_subject")
SKIP_NAMES = {"INDEX.md", "README.md", "consolidation_summary.md"}

_FM_RE = re.compile(r"\A---\n(.*?)\n---\n?", re.DOTALL)
_HTML_TAG_RE = re.compile(r"<[a-zA-Z/!][^>]*>")
_HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
_C0_RE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")
_MOJIBAKE_RE = re.compile("â€|Ã[\x80-\xbf]|Â[\x80-\xbf\xa0]|�")


def _empty(v: object) -> bool:
    return v is None or (isinstance(v, str) and not v.strip())


def validate_doc(raw: bytes) -> list[str]:
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as e:
        return [f"not_utf8: {e}"]
    m = _FM_RE.match(text)
    if not m:
        return ["no_frontmatter"]
    try:
        fm = yaml.safe_load(m.group(1))
    except yaml.YAMLError as e:
        return [f"invalid_yaml: {str(e).splitlines()[0]}"]
    if not isinstance(fm, dict):
        return ["invalid_yaml: frontmatter is not a mapping"]

    out: list[str] = []
    for k in REQUIRED_KEYS:
        if _empty(fm.get(k)):
            out.append(f"missing_key:{k}")
    if fm.get("section") not in VALID_SECTIONS:
        out.append(f"bad_section:{fm.get('section')!r}")
    has_required = all(not _empty(fm.get(k)) for k in REQUIRED_KEYS)
    if (LEGACY_ONLY_KEYS & set(fm)) and not has_required:
        out.append("legacy_schema")
    for f in SCALAR_FIELDS:
        v = fm.get(f)
        if not isinstance(v, str):
            continue
        if _HTML_TAG_RE.search(v) or _HTML_COMMENT_RE.search(v):
            out.append(f"html_in_scalar:{f}")
        if _C0_RE.search(v):
            out.append(f"control_char:{f}")
        if _MOJIBAKE_RE.search(v):
            out.append(f"mojibake:{f}")
    return out


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    total = clean = 0
    failures: list[tuple[str, list[str]]] = []
    for path in sorted(root.rglob("*.md")):
        if path.name in SKIP_NAMES:
            continue
        total += 1
        vs = validate_doc(path.read_bytes())
        if vs:
            failures.append((str(path.relative_to(root)), vs))
        else:
            clean += 1
    print(f"Validated {total} documents under {root}")
    print(f"  clean:         {clean}")
    print(f"  failed:        {len(failures)}")
    if failures:
        print("\nViolations (first 50):")
        for rel, vs in failures[:50]:
            print(f"  {rel}: {', '.join(vs)}")
        print(f"\nFAILED: {len(failures)} document(s) with violations.")
        return 1
    print("OK: zero violations.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

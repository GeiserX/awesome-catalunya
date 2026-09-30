"""MkDocs hooks for the one-page site.

on_page_markdown replaces the `<!-- n:... -->` tokens in docs/index.md with
numbers counted from README.md and DELETED.md at build time, so the home page
never states a stale figure. Entries are counted inside category sections
only: a `## Mantenedores` list of GitHub profiles is not a project.

on_page_content adds loading="lazy" to every image except the banner, so a
page with hundreds of shields.io badges paints before they all arrive, and
fails the build if the list did not come through the include. A missing
section marker already fails the build in pymdownx.snippets (check_paths:
true raises SnippetMissingError); this check is for markers that exist but
enclose the wrong lines.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ENTRY = re.compile(r"^- \[[^\]]+\]\(https?://")
# DELETED.md also lists repos that no longer exist, with no link to give:
# "- `owner/repo` - reason". They are retired entries too.
RETIRED = re.compile(r"^- (?:\[[^\]]+\]\(https?://|`[^`]+` - )")
H2 = re.compile(r"^## (.+)$")
NOT_CATEGORIES = {
    "Contenido",
    "Insignia",
    "Mantenedores",
    "Contribuir",
    "Nota",
    "Descargo de responsabilidad",
}
IMG = re.compile(r"<img\b[^>]*>")
LISTED = re.compile(r"<li>\s*<a href=\"https?://")


def _entries_by_section(text, entry=ENTRY):
    """Yield (section title or None, is_entry) for every line."""
    section = None
    for line in text.splitlines():
        heading = H2.match(line)
        if heading:
            section = heading.group(1).strip()
            continue
        yield section, bool(entry.match(line))


def _counts():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    deleted = (ROOT / "DELETED.md").read_text(encoding="utf-8")
    categories = set()
    proyectos = 0
    for section, is_entry in _entries_by_section(readme):
        if section is None or section in NOT_CATEGORIES:
            continue
        categories.add(section)
        proyectos += is_entry
    return {
        "proyectos": proyectos,
        "categorias": len(categories),
        "retirados": sum(is_entry for _, is_entry in _entries_by_section(deleted, RETIRED)),
    }


def on_page_markdown(markdown, page, config, files):
    if page.file.src_uri != "index.md":
        return markdown
    for key, value in _counts().items():
        markdown = markdown.replace(f"<!-- n:{key} -->", str(value))
    if "<!-- n:" in markdown:
        raise RuntimeError("docs/index.md has a count token the hook does not know")
    return markdown


def on_page_content(html, page, config, files):
    if page.file.src_uri != "index.md":
        return html
    listed = len(LISTED.findall(html))
    expected = _counts()["proyectos"]
    if 'id="contenido"' not in html or 'id="insignia"' not in html or listed < expected:
        raise RuntimeError(
            f"docs/index.md shows {listed} of the README's {expected} projects: "
            "check the `--8<-- [start:lista]` and `[end:lista]` markers in README.md"
        )

    def lazy(match):
        tag = match.group(0)
        if "banner.svg" in tag or "loading=" in tag:
            return tag
        return tag.replace("<img", '<img loading="lazy" decoding="async"', 1)

    return IMG.sub(lazy, html)

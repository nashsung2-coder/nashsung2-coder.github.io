"""Build pages.json from navigation metadata inside index.html and pages/*.html."""
from __future__ import annotations

import json
from html.parser import HTMLParser
from pathlib import Path


class MetadataParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.metadata: dict[str, str] = {}
        self.title: str = ""
        self._in_title = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "meta" and values.get("name", "").startswith("site-nav-"):
            self.metadata[values["name"]] = values.get("content", "")
        if tag == "title":
            self._in_title = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title += data


def page_metadata(path: Path, root: Path) -> dict[str, object] | None:
    parser = MetadataParser()
    parser.feed(path.read_text(encoding="utf-8"))
    title = parser.metadata.get("site-nav-title", "").strip()
    if not title:
        return None
    order_text = parser.metadata.get("site-nav-order", "9999").strip()
    try:
        order = int(order_text)
    except ValueError:
        order = 9999
    visible = parser.metadata.get("site-nav-visible", "true").strip().lower() not in {"0", "false", "no"}
    relative = path.relative_to(root).as_posix()
    url_path = "/" if relative == "index.html" else f"/{relative}"
    return {"path": url_path, "title": title, "order": order, "visible": visible}


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    candidates = [root / "index.html", *sorted((root / "pages").glob("*.html"))]
    pages = [page for candidate in candidates if (page := page_metadata(candidate, root))]
    pages.sort(key=lambda page: (int(page["order"]), str(page["title"]).casefold()))
    output = {"format": 1, "pages": pages}
    (root / "pages.json").write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Built navigation for {len(pages)} page(s).")


if __name__ == "__main__":
    main()

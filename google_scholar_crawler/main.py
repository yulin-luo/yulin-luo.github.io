import html
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from html.parser import HTMLParser


GOOGLE_SCHOLAR_ID = (os.environ.get("GOOGLE_SCHOLAR_ID") or "SgeV4NkAAAAJ").strip()
GOOGLE_SCHOLAR_URL = (
    "https://scholar.google.com/citations?"
    + urllib.parse.urlencode(
        {
            "user": GOOGLE_SCHOLAR_ID,
            "hl": "en",
            "pagesize": "100",
        }
    )
)


class ScholarProfileParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.meta_description = ""
        self.metric_cells = []
        self.publications = []
        self._in_metric_cell = False
        self._in_publication_row = False
        self._in_publication_title = False
        self._in_publication_citations = False
        self._in_publication_year = False
        self._current_publication = None

    def handle_starttag(self, tag, attrs):
        attr = dict(attrs)
        classes = set(attr.get("class", "").split())

        if tag == "meta" and attr.get("name") == "description":
            self.meta_description = attr.get("content", "")

        if tag == "td" and "gsc_rsb_std" in classes:
            self._in_metric_cell = True

        if tag == "tr" and "gsc_a_tr" in classes:
            self._in_publication_row = True
            self._current_publication = {
                "bib": {"title": ""},
                "num_citations": 0,
                "author_pub_id": "",
                "pub_year": "",
            }

        if self._in_publication_row and tag == "a" and "gsc_a_at" in classes:
            self._in_publication_title = True
            href = attr.get("href", "")
            match = re.search(r"citation_for_view=([^&]+)", href)
            if match:
                self._current_publication["author_pub_id"] = urllib.parse.unquote(match.group(1))

        if self._in_publication_row and tag == "a" and "gsc_a_ac" in classes:
            self._in_publication_citations = True

        if self._in_publication_row and tag == "span" and "gsc_a_h" in classes:
            self._in_publication_year = True

    def handle_endtag(self, tag):
        if tag == "td":
            self._in_metric_cell = False
        if tag == "a":
            self._in_publication_title = False
            self._in_publication_citations = False
        if tag == "span":
            self._in_publication_year = False
        if tag == "tr" and self._in_publication_row:
            title = self._current_publication["bib"]["title"].strip()
            if title:
                self.publications.append(self._current_publication)
            self._current_publication = None
            self._in_publication_row = False

    def handle_data(self, data):
        text = html.unescape(data).strip()
        if not text:
            return
        if self._in_metric_cell:
            self.metric_cells.append(text)
        if self._current_publication is not None and self._in_publication_title:
            self._current_publication["bib"]["title"] += text
        if self._current_publication is not None and self._in_publication_citations:
            self._current_publication["num_citations"] = int(text) if text.isdigit() else 0
        if self._current_publication is not None and self._in_publication_year:
            self._current_publication["pub_year"] = text


def fetch_profile_html():
    request = urllib.request.Request(
        GOOGLE_SCHOLAR_URL,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"
            ),
            "Accept-Language": "en-US,en;q=0.9",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8", errors="replace")


def parse_metrics(parser):
    metrics = [int(cell) for cell in parser.metric_cells if cell.isdigit()]
    if len(metrics) < 5:
        fallback = re.search(r"Cited by\s+([0-9,]+)", parser.meta_description)
        if fallback:
            metrics.insert(0, int(fallback.group(1).replace(",", "")))
    if len(metrics) < 5:
        raise RuntimeError("Could not parse Google Scholar metrics.")
    return {
        "citedby": metrics[0],
        "citedby5y": metrics[1],
        "hindex": metrics[2],
        "hindex5y": metrics[3],
        "i10index": metrics[4],
        "i10index5y": metrics[5] if len(metrics) > 5 else metrics[4],
    }


def main():
    profile_html = fetch_profile_html()
    parser = ScholarProfileParser()
    parser.feed(profile_html)
    metrics = parse_metrics(parser)

    author = {
        "scholar_id": GOOGLE_SCHOLAR_ID,
        "name": "Yulin Luo",
        "source": GOOGLE_SCHOLAR_URL,
        "updated": datetime.now(timezone.utc).isoformat(),
        "publications": {
            publication["author_pub_id"]: publication
            for publication in parser.publications
            if publication["author_pub_id"]
        },
        **metrics,
    }

    os.makedirs("results", exist_ok=True)
    with open("results/gs_data.json", "w") as outfile:
        json.dump(author, outfile, ensure_ascii=False, indent=2)

    shieldio_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": f"{author['citedby']}",
    }
    with open("results/gs_data_shieldsio.json", "w") as outfile:
        json.dump(shieldio_data, outfile, ensure_ascii=False, indent=2)

    print(json.dumps(author, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"Google Scholar crawler failed: {exc}", file=sys.stderr)
        raise

#!/usr/bin/env python3
"""
Converts a BibTeX file to Jekyll-compatible _data/publications.yml
NO author filtering — assumes ALL entries are by Luca Martino or Óscar Barquero.
Generates both _data/publications.yml AND _pages/publications.md automatically.
OVERWRITES existing files each time.
LaTeX accents (\~n, \'{\i}) are converted to Unicode (ñ, í).
Volume and pages default to "1" if missing.
All metadata appears in one line: Journal, Volume, Pages, Year.
DOI links are clickable and open in new tab.
Requires: pip install bibtexparser
"""

import bibtexparser
from bibtexparser.bparser import BibTexParser
import yaml
import re
import os

# --- CONFIGURATION ---
INPUT_BIB = "lm_obp_10_16_2025.bib"        # ← Your BibTeX file
OUTPUT_YML = "../_data/publications.yml"  # ← Output YAML
OUTPUT_MD = "../_pages/publications.md"   # ← Output Markdown page

# --- LaTeX to Unicode mapping (covers all common cases) ---
LATEX_TO_UNICODE = {
    r'\\~n': 'ñ', r'\\~N': 'Ñ',
    r"\\'{\i}": 'í', r"\\'{\I}": 'Í',
    r"\\'{a}": 'á', r"\\'{A}": 'Á',
    r"\\'{e}": 'é', r"\\'{E}": 'É',
    r"\\'{i}": 'í', r"\\'{I}": 'Í',
    r"\\'{o}": 'ó', r"\\'{O}": 'Ó',
    r"\\'{u}": 'ú', r"\\'{U}": 'Ú',
    r"\\'{\`a}": 'à', r"\\'{\`A}": 'À',
    r"\\'{\`e}": 'è', r"\\'{\`E}": 'È',
    r"\\'{\`i}": 'ì', r"\\'{\`I}": 'Ì',
    r"\\'{\`o}": 'ò', r"\\'{\`O}": 'Ò',
    r"\\'{\`u}": 'ù', r"\\'{\`U}": 'Ù',
    r"\\^{a}": 'â', r"\\^{A}": 'Â',
    r"\\^{e}": 'ê', r"\\^{E}": 'Ê',
    r"\\^{i}": 'î', r"\\^{I}": 'Î',
    r"\\^{o}": 'ô', r"\\^{O}": 'Ô',
    r"\\^{u}": 'û', r"\\^{U}": 'Û',
    r"\\\"{a}": 'ä', r"\\\"{A}": 'Ä',
    r"\\\"{e}": 'ë', r"\\\"{E}": 'Ë',
    r"\\\"{i}": 'ï', r"\\\"{I}": 'Ï',
    r"\\\"{o}": 'ö', r"\\\"{O}": 'Ö',
    r"\\\"{u}": 'ü', r"\\\"{U}": 'Ü',
    r"\\c{c}": 'ç', r"\\c{C}": 'Ç',
    r"\\&": '&', r"\\textbackslash": '\\',
    r"\\{\\}": '{', r"\\}": '}',
    r"\{": '{', r"\}": '}',
}

def clean_latex(text):
    """Convert LaTeX accent commands to Unicode characters."""
    if not isinstance(text, str):
        return text
    result = text
    for latex, unicode_char in LATEX_TO_UNICODE.items():
        result = result.replace(latex, unicode_char)
    # Remove any remaining LaTeX braces and backslashes
    result = result.replace('{', '').replace('}', '').replace('\\', '')
    return result.strip()

def parse_bibtex(filename):
    """Read .bib file with UTF-8 encoding and parse entries."""
    with open(filename, "r", encoding="utf-8") as bibtex_file:
        parser = BibTexParser()
        parser.ignore_nonstandard_types = False
        parser.homogenise_fields = False
        bib_database = bibtexparser.load(bibtex_file, parser=parser)
    return bib_database.entries

def clean_author_list(authors_str):
    """Convert 'Author A and Author B' into list ['Author A', 'Author B'] and clean LaTeX."""
    if not authors_str:
        return []
    authors_str = authors_str.replace(" and ", " AND ")
    authors = [clean_latex(a.strip()) for a in authors_str.split("AND")]
    return authors

def extract_doi(url):
    """Extract DOI from URL like https://doi.org/10.xxxx/xxxx"""
    match = re.search(r"doi\.org/(.+)", url)
    return match.group(1) if match else url

def convert_to_yaml(entries):
    publications = []
    for entry in entries:
        if "year" not in entry or "title" not in entry:
            continue

        # Clean and set defaults
        title = clean_latex(entry["title"])
        journal = clean_latex(entry.get("journal", ""))
        volume = clean_latex(entry.get("volume", "1"))
        pages = clean_latex(entry.get("pages", "1"))
        year = entry["year"]

        pub = {
            "year": year,
            "authors": clean_author_list(entry.get("author", entry.get("editor", ""))),
            "title": title,
            "journal": journal,
            "volume": volume,
            "pages": pages,
        }

        # Handle DOI
        if "doi" in entry:
            pub["doi"] = extract_doi(clean_latex(entry["doi"]))
        elif "url" in entry and "doi.org" in entry["url"]:
            pub["doi"] = extract_doi(clean_latex(entry["url"]))

        # Handle arXiv
        if "eprint" in entry and "arxiv" in entry.get("archiveprefix", "").lower():
            pub["arxiv"] = f"https://arxiv.org/abs/{clean_latex(entry['eprint'])}"

        # Handle generic link if no DOI
        if "url" in entry and "doi.org" not in entry["url"] and "doi" not in pub:
            pub["link"] = clean_latex(entry["url"])

        publications.append(pub)

    # Sort by year descending
    publications.sort(key=lambda x: x["year"], reverse=True)
    return publications

def generate_publications_md(publications):
    md_content = """---
title: "Publications"
layout: single
author_profile: true
permalink: /publications/
css:
    - /assets/css/custom.css
---

<div style="text-align: center; margin-bottom: 2rem; font-size: 1.25rem; color: #555;">
  Selected publications by Luca Martino and Óscar Barquero
</div>

{% assign grouped_pubs = site.data.publications | group_by: "year" | sort: "name" | reverse %}

{% for group in grouped_pubs %}
  <h2 id="{{ group.name }}">{{ group.name }}</h2>
  <ul class="publications-list">
  {% for pub in group.items %}
    <li>
      <strong>{{ pub.title }}</strong><br>
      {{ pub.authors | join: ", " }}<br>
      <em>{{ pub.journal }}</em>{% if pub.volume != "1" %}, {{ pub.volume }}{% endif %}{% if pub.pages != "1" %}, {{ pub.pages }}{% endif %}, {{ pub.year }}
      <br>
      {% if pub.doi %}
        <a href="https://doi.org/{{ pub.doi }}" target="_blank" rel="noopener noreferrer" style="color: #0077cc; text-decoration: none; font-weight: 500;">
          DOI: {{ pub.doi | split: "/" | last }}
        </a>
      {% endif %}
      {% if pub.arxiv %}
        {% if pub.doi %}&nbsp;|&nbsp;{% endif %}
        <a href="{{ pub.arxiv }}" target="_blank" rel="noopener noreferrer" style="color: #0077cc; text-decoration: none; font-weight: 500;">
          arXiv
        </a>
      {% endif %}
      {% if pub.link and pub.doi == nil %}
        {% if pub.doi or pub.arxiv %}&nbsp;|&nbsp;{% endif %}
        <a href="{{ pub.link }}" target="_blank" rel="noopener noreferrer" style="color: #0077cc; text-decoration: none; font-weight: 500;">
          Link
        </a>
      {% endif %}
    </li>
  {% endfor %}
  </ul>
{% endfor %}
"""
    return md_content

# --- EXECUTION ---
if __name__ == "__main__":
    print("🔍 Reading BibTeX file...")
    entries = parse_bibtex(INPUT_BIB)
    print(f"✅ Found {len(entries)} publications.")

    publications = convert_to_yaml(entries)
    print(f"✅ Converted {len(publications)} entries to YAML format.")

    # OVERWRITE: Write YAML — replaces file entirely
    with open(OUTPUT_YML, "w", encoding="utf-8") as f:
        yaml.dump(publications, f, default_flow_style=False, allow_unicode=True, indent=2, sort_keys=False)
    print(f"🎉 Overwritten: {OUTPUT_YML}")

    # OVERWRITE: Write Markdown — replaces file entirely
    md_content = generate_publications_md(publications)
    with open(OUTPUT_MD, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"🎉 Overwritten: {OUTPUT_MD}")

    print("\n✅ DONE! Your publications page is ready.")
    print("👉 Push to GitHub — your publications page will auto-update!")
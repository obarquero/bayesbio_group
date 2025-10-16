---
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

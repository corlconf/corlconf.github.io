---
title: All Papers
has_children: true
has_toc: false
nav_order: 1
---
{%- assign children_list = site.html_pages | where_exp:"item", "item.grand_parent != nil" | sort_natural:"title" -%}

# All Papers


<ul>
    {% for child in children_list %}
        <li>
        <a href="{{ child.url | absolute_url }}">{{ child.title }}</a> 
        <a href="{{ child.pdf }}"><i class="fa fa-file-text-o" aria-hidden="true"></i></a>

        {% if child.code != nil %}
            <a href="{{ child.code }}"><i class="fa fa fa-github" aria-hidden="true"></i></a>
        {% endif %}

        </li>
    {% endfor %}
</ul>

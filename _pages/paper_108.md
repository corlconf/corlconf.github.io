---
layout: page
title: "Learning hierarchical relationships for object-goal navigation"
subtitle: 
description:
permalink: /paper_108/
grand_parent: All Papers
parent: Tuesday
supp: 
code: https://github.com/cassieqiuyd/MJOLNIR
youtube_id: eCxWwohbOd8
pdf: https://drive.google.com/file/d/1SL_pL6DjHmRrYxpAR9wyZwydGXL2_iY_/view
---

# Learning hierarchical relationships for object-goal navigation

<a href="https://drive.google.com/file/d/1SL_pL6DjHmRrYxpAR9wyZwydGXL2_iY_/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="https://github.com/cassieqiuyd/MJOLNIR" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Anwesan Pal (UC San Diego); Yiding Qiu (UC San Diego)*; Henrik Christensen (UC San Diego)**

#### Interactive Session
<a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SESSUDWGU3SSCFP7L" target="_blank" rel="noopener noreferrer"><em>2020-11-17, 11:50 - 12:20 PST </em></a>

#### Abstract
Direct search for objects as part of navigation poses a challenge for small items. Utilizing context in the form of object-object relationships enable hierarchical search for targets efficiently. Most of the current approaches tend to directly incorporate sensory input into a reward-based learning approach, without learning about object relationships in the natural environment, and thus generalize poorly across domains. We present Memory-utilized Joint hierarchical Object Learning for Navigation in Indoor Rooms (MJOLNIR), a target-driven navigation algorithm, which considers the inherent relationship between target objects, and the more salient contextual objects occurring in its surrounding. Extensive experiments conducted across multiple environment settings show an 82.9% and 93.5% gain over existing state-of-the-art navigation methods in terms of the success rate (SR), and success weighted by path length (SPL), respectively. We also show that our model learns to converge much faster than other algorithms, without suffering from the well-known overfitting problem. Additional details regarding the supplementary material and code are available at <a href="https://sites.google.com/eng.ucsd.edu/mjolnir" target="_blank">https://sites.google.com/eng.ucsd.edu/mjolnir</a>.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1rRue8uWE-slK6J0ZYLyUNfWl0caJ7lvt/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


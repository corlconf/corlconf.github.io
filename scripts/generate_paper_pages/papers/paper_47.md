---
layout: page
title: "GDN: A Coarse-To-Fine (C2F) Representation for End-To-End 6-DoF Grasp Detection"
subtitle: 
description:
permalink: /paper_47/
grand_parent: All Papers
parent: Tuesday
supp: 
code: 
youtube_id: SzgQh6QX-QM
pdf: https://drive.google.com/file/d/1yQtB0x7buOguG78THL2WmFr3Twk54zdF/view
---

# GDN: A Coarse-To-Fine (C2F) Representation for End-To-End 6-DoF Grasp Detection

<a href="https://drive.google.com/file/d/1yQtB0x7buOguG78THL2WmFr3Twk54zdF/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Kuang-Yu Jeng (National Taiwan University)*; Yueh-Cheng Liu (National Taiwan University); Zhe Yu Liu (National Taiwan University); Jen-Wei Wang (National Taiwan University); Ya-Liang Chang (National Taiwan University); Hung-Ting Su (National Taiwan University); Winston Hsu (National Taiwan University)**

#### Interactive Session
<em>2020-11-17, 11:10 - 11:40 PST </em> | <a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SESLBC3AS9IATU3CD" target="_blank" rel="noopener noreferrer"> PheedLoop Session <i class="fa fa-external-link" aria-hidden="true"></i> </a> 

#### Abstract
We proposed an end-to-end grasp detection network,  Grasp Detection Network (GDN), cooperated with a novel coarse-to-fine (C2F) grasp representation design to detect diverse and accurate 6-DoF grasps based on point clouds.   Compared to previous two-stage approaches which sample and evaluate multiple grasp candidates, our architecture is at least 20 times faster.  It is also 8% and 40% more accurate in terms of the success rate in single object scenes and the complete rate in clutter scenes, respectively. Our method shows superior results among settings with different number of views and input points.  Moreover, we propose a new AP-based metric which considers both rotation and transition errors, making it a more comprehensive evaluation tool for grasp detection models.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


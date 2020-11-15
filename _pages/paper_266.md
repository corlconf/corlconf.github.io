---
layout: page
title: "Learning to Communicate and Correct Pose Errors"
subtitle: 
description:
permalink: /paper_266/
grand_parent: All Papers
parent: Wednesday
supp: 
code: 
youtube_id: 
pdf: https://drive.google.com/file/d/1CCtpzepy4UJcHWnRmOhLUrJs6mPu8YW4/view
---

# Learning to Communicate and Correct Pose Errors

<a href="https://drive.google.com/file/d/1CCtpzepy4UJcHWnRmOhLUrJs6mPu8YW4/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Nicholas Vadivelu (Uber ATG)*; Mengye Ren (Uber ATG, University of Toronto); James Tu (Uber ATG); Jingkang Wang (Uber ATG, University of Toronto); Raquel Urtasun (Uber ATG)**

#### Interactive Session
*2020-11-18, 12:30 - 13:00 PST* 

#### Abstract
Learned communication makes multi-agent systems more effective by aggregating distributed information. However, it also exposes individual agents to the threat of erroneous messages they receive. In this paper, we study the setting proposed in V2VNet, where nearby self-driving vehicles jointly perform object detection and motion forecasting in a cooperative manner. Despite a huge performance boost when the agents solve the task together, the gain is quickly diminished in the presence of pose noise since the communication relies on spatial transformations. Hence, we propose a novel neural reasoning framework that learns to communicate, to estimate errors, and finally, to reach a consensus about those errors. Experiments confirm that our proposed framework significantly improves the robustness of multi-agent self-driving perception systems under realistic and severe localization noise.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1bvDiiI0yq6N0oxB_l44_AwV3q3-Wa6TS/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


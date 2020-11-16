---
layout: page
title: "Transporter Networks: Rearranging the Visual World for Robotic Manipulation"
subtitle: 
description:
permalink: /paper_153/
grand_parent: All Papers
parent: Monday
supp: 
code: https://transporternets.github.io/
youtube_id: QykeilrcZvc
pdf: https://drive.google.com/file/d/1bKdEOOwCXBnu5zNjw-JKuZdr2GMSD_8-/view
---

# Transporter Networks: Rearranging the Visual World for Robotic Manipulation

<a href="https://drive.google.com/file/d/1bKdEOOwCXBnu5zNjw-JKuZdr2GMSD_8-/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="https://transporternets.github.io/" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Andy Zeng (Google)*; Pete Florence (Google); Jonathan Tompson (Google); Stefan Welker (Google); Jonathan Chien (Google); Maria Attarian (Google); Travis Armstrong (Google); Ivan Krasin (Google); Dan Duong (Google); Vikas Sindhwani (Google); Johnny Lee (Google)**

#### Interactive Session
<em>2020-11-16, 11:10 - 11:40 PST </em> | <a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SESW381GJJAAWR10L" target="_blank" rel="noopener noreferrer"> PheedLoop Session <i class="fa fa-external-link" aria-hidden="true"></i> </a> 

#### Abstract
Robotic manipulation can be formulated as inducing a sequence of spatial displacements: where the space being moved can encompass an object, part of an object, or end effector. In this work, we propose the Transporter Network, a simple model architecture that rearranges deep features to infer spatial displacements from visual input - which can parameterize robot actions. It makes no assumptions of objectness (e.g. canonical poses, models, or keypoints), it exploits spatial symmetries, and is orders of magnitude more sample efficient than our benchmarked alternatives in learning vision-based manipulation tasks: from stacking a pyramid of blocks, to assembling kits with unseen objects; from manipulating deformable ropes, to pushing piles of small objects with closed-loop feedback. Our method can represent complex multi-modal policy distributions and generalizes to multi-step sequential tasks, as well as 6DoF pick-and-place. Experiments on 10 simulated tasks show that it learns faster and generalizes better than a variety of end-to-end baselines, including policies that use ground-truth object poses. We validate our methods with hardware in the real world. Experiment videos and code will be made available at <a href="https://transporternets.github.io" target="_blank">https://transporternets.github.io</a>

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1rfMBk4SrhwM4vCC1xqcaNz5qeg8XEWOR/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


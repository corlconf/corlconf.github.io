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
youtubeId: 
---

# Transporter Networks: Rearranging the Visual World for Robotic Manipulation

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1bKdEOOwCXBnu5zNjw-JKuZdr2GMSD_8-/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Andy Zeng (Google)*; Pete Florence (Google); Jonathan Tompson (Google); Stefan Welker (Google); Jonathan Chien (Google); Maria Attarian (Google); Travis Armstrong (Google); Ivan Krasin (Google); Dan Duong (Google); Vikas Sindhwani (Google); Johnny Lee (Google)**

#### Abstract
Robotic manipulation can be formulated as inducing a sequence of spatial displacements: where the space being moved can encompass an object, part of an object, or end effector. In this work, we propose the Transporter Network, a simple model architecture that rearranges deep features to infer spatial displacements from visual input - which can parameterize robot actions. It makes no assumptions of objectness (e.g. canonical poses, models, or keypoints), it exploits spatial symmetries, and is orders of magnitude more sample efficient than our benchmarked alternatives in learning vision-based manipulation tasks: from stacking a pyramid of blocks, to assembling kits with unseen objects; from manipulating deformable ropes, to pushing piles of small objects with closed-loop feedback. Our method can represent complex multi-modal policy distributions and generalizes to multi-step sequential tasks, as well as 6DoF pick-and-place. Experiments on 10 simulated tasks show that it learns faster and generalizes better than a variety of end-to-end baselines, including policies that use ground-truth object poses. We validate our methods with hardware in the real world. Experiment videos and code will be made available at <a href="https://transporternets.github.io" target="_blank">https://transporternets.github.io</a>

#### Video 

#### Reviews

#### Rebuttal

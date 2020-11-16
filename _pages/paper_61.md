---
layout: page
title: "Integrating Egocentric Localization for More Realistic Point-Goal Navigation Agents"
subtitle: 
description:
permalink: /paper_61/
grand_parent: All Papers
parent: Wednesday
supp: 
code: 
youtube_id: 8RjL627AKyA
pdf: https://drive.google.com/file/d/1Wx1GhK3CiEJLk2fTGNSJKR_syCNDrRl0/view
---

# Integrating Egocentric Localization for More Realistic Point-Goal Navigation Agents

<a href="https://drive.google.com/file/d/1Wx1GhK3CiEJLk2fTGNSJKR_syCNDrRl0/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Samyak Datta (Georgia Tech)*; Oleksandr Maksymets (Facebook AI Research); Judy Hoffman (Georgia Tech); Stefan Lee (Oregon State University); Dhruv Batra (Georgia Tech & Facebook AI Research); Devi Parikh (Georgia Tech & Facebook AI Research)**

#### Interactive Session
<a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SES2NENWN2KUL4TNB" target="_blank" rel="noopener noreferrer"><em>2020-11-18, 12:30 - 13:00 PST </em></a>

#### Abstract
Recent work has presented embodied agents that can navigate to point-goal targets in novel indoor environments with near-perfect accuracy. However, these agents are equipped with idealized sensors for localization and take deterministic actions. This setting is practically sterile by comparison to the dirty reality of noisy sensors and actuations in the real world - wheels can slip, motion sensors have error, actuations can rebound. In this work, we take a step towards this noisy reality, developing point-goal navigation agents that rely on visual estimates of egomotion under noisy action dynamics. We find these agents outperform naive adaptions of current point-goal agents to this setting as well as those incorporating classic localization baselines. Further, our model conceptually divides learning agent dynamics or odometry (where am I?) from task-specific navigation policy (where do I want to go?). This enables a seamless adaption to changing dynamics (a different robot or floor type) by simply re-calibrating the visual odometry model - circumventing the expense of re-training of the navigation policy. Our agent was the runner-up in the PointNav track of CVPR 2020 Habitat Challenge.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1ZK5Y1X0WP8nrYoqLhG_POHsQlZYyrTj2/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


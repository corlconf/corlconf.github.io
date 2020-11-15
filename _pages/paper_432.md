---
layout: page
title: "Model-Based Inverse Reinforcement Learning from Visual Demonstrations"
subtitle: 
description:
permalink: /paper_432/
grand_parent: All Papers
parent: Wednesday
supp: 
code: https://sites.google.com/view/model-based-irl-from-vision
youtube_id: sRrNhtLk12M
pdf: https://drive.google.com/file/d/1_uu4RJbAdYU_4Is_gSVTCO8KA77Mwii1/view
---

# Model-Based Inverse Reinforcement Learning from Visual Demonstrations

<a href="https://drive.google.com/file/d/1_uu4RJbAdYU_4Is_gSVTCO8KA77Mwii1/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="https://sites.google.com/view/model-based-irl-from-vision" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Neha Das (Facebook AI Research)*; Sarah Bechtle (Max Planck Institute for Intelligent Systems); Todor Davchev (University of Edinburgh); Dinesh Jayaraman (University of Pennsylvania); Akshara Rai (Facebook); Franziska Meier (Facebook AI Research)**

#### Interactive Session
*2020-11-18, 11:50 - 12:20 PST* 

#### Abstract
Scaling model-based inverse reinforcement learning (IRL) to real robotic manipulation tasks with unknown dynamics remains an open problem. The key challenges lie in learning good dynamics models, developing algorithms that scale to high-dimensional state-spaces and being able to learn from both visual and proprioceptive demonstrations. In this work, we present a gradient-based inverse reinforcement learning framework that utilizes a pre-trained visual dynamics model to learn cost functions when given only visual human demonstrations. The learned cost functions are then used to reproduce the demonstrated behavior via visual model predictive control. We evaluate our framework on hardware on two basic object manipulation tasks.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1lKgVptkQDyzos24CTZVeHwOQE0-Zx1Gi/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


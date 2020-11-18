---
layout: page
title: "Hardware as Policy: Mechanical and Computational Co-Optimization using Deep Reinforcement Learning"
subtitle: 
description:
permalink: /paper_256/
grand_parent: All Papers
parent: Wednesday
supp: 
code: https://github.com/roamlab/HWasP-toy-problem
youtube_id: E28Cu_agaoc
pdf: https://drive.google.com/file/d/1iT6r4tI_d-Nfz1jx6zBVk06fpls9aBLz/view
---

# Hardware as Policy: Mechanical and Computational Co-Optimization using Deep Reinforcement Learning

<a href="https://drive.google.com/file/d/1iT6r4tI_d-Nfz1jx6zBVk06fpls9aBLz/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="https://github.com/roamlab/HWasP-toy-problem" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Tianjian Chen (Columbia University)*; Zhanpeng He (Columbia University); Matei Ciocarlie (Columbia)**

#### Interactive Session
<em>2020-11-18, 11:50 - 12:20 PST </em> | <a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SESOBS6ONNH0FEZ8R" target="_blank" rel="noopener noreferrer"> PheedLoop Session <i class="fa fa-external-link" aria-hidden="true"></i> </a> 

#### Abstract
Deep Reinforcement Learning (RL) has shown great success in learning complex control policies for a variety of applications in robotics. However, in most such cases, the hardware of the robot has been considered immutable, modeled as part of the environment.  In this study, we explore the problem of learning hardware and control parameters together in a unified RL framework. To achieve this, we propose to model the robot body as a “hardware policy”, analogous to and optimized jointly with its computational counterpart. We show that, by modeling such hardware policies as auto-differentiable computational graphs, the ensuing optimization problem can be solved efficiently by gradient-based algorithms from the Policy Optimization family.  We present two such design examples:  a toy mass-spring problem, and a real-world problem of designing an underactuated hand.  We compare our method against traditional co-optimization approaches, and also demonstrate its effectiveness by building a physical prototype based on the learned hardware parameters.  Videos and more details are available at <a href="https://roamlab.github.io/hwasp/" target="_blank">https://roamlab.github.io/hwasp/</a>.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1xzrz_8nkOrOOGlDi1JfxIUiAD7sn39qv/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


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
youtubeId: 
---

# Hardware as Policy: Mechanical and Computational Co-Optimization using Deep Reinforcement Learning

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1iT6r4tI_d-Nfz1jx6zBVk06fpls9aBLz/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Tianjian Chen (Columbia University)*; Zhanpeng He (Columbia University); Matei Ciocarlie (Columbia)**

#### Interactive Session
*2020-11-18, 11:50 - 12:20 PST*

#### Abstract
Deep Reinforcement Learning (RL) has shown great success in learning complex control policies for a variety of applications in robotics. However, in most such cases, the hardware of the robot has been considered immutable, modeled as part of the environment.  In this study, we explore the problem of learning hardware and control parameters together in a unified RL framework. To achieve this, we propose to model the robot body as a “hardware policy”, analogous to and optimized jointly with its computational counterpart. We show that, by modeling such hardware policies as auto-differentiable computational graphs, the ensuing optimization problem can be solved efficiently by gradient-based algorithms from the Policy Optimization family.  We present two such design examples:  a toy mass-spring problem, and a real-world problem of designing an underactuated hand.  We compare our method against traditional co-optimization approaches, and also demonstrate its effectiveness by building a physical prototype based on the learned hardware parameters.  Videos and more details are available at <a href="https://roamlab.github.io/hwasp/" target="_blank">https://roamlab.github.io/hwasp/</a>.

#### Video 

#### Reviews

#### Rebuttal

---
layout: page
title: "Learning Predictive Representations for Deformable Objects Using Contrastive Estimation"
subtitle: 
description:
permalink: /paper_126/
grand_parent: All Papers
parent: Wednesday
supp: 
code: https://github.com/wilson1yan/contrastive-forward-model
youtubeId: 
---

# Learning Predictive Representations for Deformable Objects Using Contrastive Estimation

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1P2J7zA6cglYivLm21FAudBj9aeOonMGj/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Wilson Yan (UC Berkeley)*; Ashwin Vangipuram (UC Berkeley); Pieter Abbeel (UC Berkeley); Lerrel Pinto ()**

#### Interactive Session
*2020-11-18, 11:50 - 12:20 PST*

#### Abstract
Using visual model-based learning for deformable object manipulation is challenging due to difficulties in learning plannable visual representations along with complex dynamic models. In this work, we propose a new learning framework that jointly optimizes both the visual representation model and the dynamics model using contrastive estimation. Using simulation data collected by randomly perturbing deformable objects on a table, we learn latent dynamics models for these objects in an offline fashion. Then, using the learned models, we use simple model-based planning to solve challenging deformable object manipulation tasks such as spreading ropes and cloths. Experimentally, we show substantial improvements in performance over standard model-based learning techniques across our rope and cloth manipulation suite. Finally, we transfer our visual manipulation policies trained on data purely collected in simulation to a real PR2 robot through domain randomization.

#### Video 

#### Reviews

#### Rebuttal

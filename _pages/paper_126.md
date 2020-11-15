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
youtube_id: RM856fs2B18
pdf: https://drive.google.com/file/d/1P2J7zA6cglYivLm21FAudBj9aeOonMGj/view
---

# Learning Predictive Representations for Deformable Objects Using Contrastive Estimation

<a href="https://drive.google.com/file/d/1P2J7zA6cglYivLm21FAudBj9aeOonMGj/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="https://github.com/wilson1yan/contrastive-forward-model" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Wilson Yan (UC Berkeley)*; Ashwin Vangipuram (UC Berkeley); Pieter Abbeel (UC Berkeley); Lerrel Pinto ()**

#### Interactive Session
*2020-11-18, 11:50 - 12:20 PST* 

#### Abstract
Using visual model-based learning for deformable object manipulation is challenging due to difficulties in learning plannable visual representations along with complex dynamic models. In this work, we propose a new learning framework that jointly optimizes both the visual representation model and the dynamics model using contrastive estimation. Using simulation data collected by randomly perturbing deformable objects on a table, we learn latent dynamics models for these objects in an offline fashion. Then, using the learned models, we use simple model-based planning to solve challenging deformable object manipulation tasks such as spreading ropes and cloths. Experimentally, we show substantial improvements in performance over standard model-based learning techniques across our rope and cloth manipulation suite. Finally, we transfer our visual manipulation policies trained on data purely collected in simulation to a real PR2 robot through domain randomization.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1IRDNpfRdsu3tIOLDIQIOiNL7EWSO-2om/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


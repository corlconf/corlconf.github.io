---
layout: page
title: "Reactive motion planning with probabilisticsafety guarantees"
subtitle: 
description:
permalink: /paper_440/
grand_parent: All Papers
parent: Monday
supp: 
code: 
youtube_id: 316PFeUc2d8
pdf: https://drive.google.com/file/d/19Hwr4MzkOK_wUbmF5gBTwO5paCcFkHCR/view
---

# Reactive motion planning with probabilisticsafety guarantees

<a href="https://drive.google.com/file/d/19Hwr4MzkOK_wUbmF5gBTwO5paCcFkHCR/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Yuxiao Chen (California Institute of Technology)*; Ugo Rosolia (California Institute of Technology); Chuchu Fan (MIT); Aaron Ames (Caltech); Richard Murray (California Institute of Technology)**

#### Interactive Session
*2020-11-16, 11:50 - 12:20 PST* 

#### Abstract
Motion planning in environments with multiple agents is critical to many important autonomous applications such as autonomous vehicles and assistive robots. This paper considers the problem of motion planning, where the controlled agent shares the environment with multiple uncontrolled agents. First, a predictive model of the uncontrolled agents is trained to predict all possible trajectories within a short horizon based on the scenario. The prediction is then fed to a motion planning module based on model predictive control. We proved generalization bound for the predictive model using three different methods, post-bloating, support vector machine (SVM), and conformal analysis, all capable of generating stochastic guarantees of the correctness of the predictor. The proposed approach is demonstrated in simulation in a scenario emulating autonomous highway driving.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1Q_KMj2wTuhkc-GWnOBhc7JUUuIN2Zuis/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


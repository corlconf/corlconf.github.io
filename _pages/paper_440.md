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
youtubeId: 
---

# Reactive motion planning with probabilisticsafety guarantees

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/19Hwr4MzkOK_wUbmF5gBTwO5paCcFkHCR/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Yuxiao Chen (California Institute of Technology)*; Ugo Rosolia (California Institute of Technology); Chuchu Fan (MIT); Aaron Ames (Caltech); Richard Murray (California Institute of Technology)**

#### Abstract
Motion planning in environments with multiple agents is critical to many important autonomous applications such as autonomous vehicles and assistive robots. This paper considers the problem of motion planning, where the controlled agent shares the environment with multiple uncontrolled agents. First, a predictive model of the uncontrolled agents is trained to predict all possible trajectories within a short horizon based on the scenario. The prediction is then fed to a motion planning module based on model predictive control. We proved generalization bound for the predictive model using three different methods, post-bloating, support vector machine (SVM), and conformal analysis, all capable of generating stochastic guarantees of the correctness of the predictor. The proposed approach is demonstrated in simulation in a scenario emulating autonomous highway driving.

#### Video 

#### Reviews

#### Rebuttal

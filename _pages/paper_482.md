---
layout: page
title: "Differentiable Logic Layer for Rule Guided Trajectory Prediction"
subtitle: 
description:
permalink: /paper_482/
grand_parent: All Papers
parent: Monday
supp: 
code: 
youtubeId: 
---

# Differentiable Logic Layer for Rule Guided Trajectory Prediction

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1XxYxO_doBjFy70ruodwikpCJB9htrdIV/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Xiao Li (MIT)*; Guy Rosman (MIT); Igor Gilitschenski (Massachusetts Institute of Technology); Jonathan DeCastro (Toyota Research Institute); Cristian-Ioan Vasile (Lehigh University); Sertac Karaman (Massachusetts Institute of Technology); Daniela  Rus (MIT CSAIL)**

#### Abstract
In this work, we propose a method for integration of temporal logic formulas into a neural network. Our main contribution is a new logic optimization layer that uses differentiable optimization on the formulas’ robustness function. This allows incorporating traffic rules into deep learning based trajectory prediction approaches. In the forward pass, an initial prediction from a base predictor is used to initialize and guide the robustness optimization process. Backpropagation through the logic layer allows for simultaneously adjusting the parameters of the rules and the initial prediction network. The integration of a logic layer affords both improved predictions, as well as quantification rule satisfaction and violation during predictor execution. As such, it can serve as a parametric safety- envelope for black box behavior models. We demonstrate how integrating traffic rules improves the predictor performance using real traffic data from the NuScenes dataset.

#### Video 

#### Reviews

#### Rebuttal

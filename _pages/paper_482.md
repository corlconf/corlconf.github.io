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
youtube_id: BuZMY2AP9yU
pdf: https://drive.google.com/file/d/1XxYxO_doBjFy70ruodwikpCJB9htrdIV/view
---

# Differentiable Logic Layer for Rule Guided Trajectory Prediction

<a href="https://drive.google.com/file/d/1XxYxO_doBjFy70ruodwikpCJB9htrdIV/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Xiao Li (MIT)*; Guy Rosman (MIT); Igor Gilitschenski (Massachusetts Institute of Technology); Jonathan DeCastro (Toyota Research Institute); Cristian-Ioan Vasile (Lehigh University); Sertac Karaman (Massachusetts Institute of Technology); Daniela  Rus (MIT CSAIL)**

#### Interactive Session
<em>2020-11-16, 11:10 - 11:40 PST </em> | <a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SESPCYRTIQFL5FZ8Z" target="_blank" rel="noopener noreferrer"> PheedLoop Session <i class="fa fa-external-link" aria-hidden="true"></i> </a> 

#### Abstract
In this work, we propose a method for integration of temporal logic formulas into a neural network. Our main contribution is a new logic optimization layer that uses differentiable optimization on the formulas’ robustness function. This allows incorporating traffic rules into deep learning based trajectory prediction approaches. In the forward pass, an initial prediction from a base predictor is used to initialize and guide the robustness optimization process. Backpropagation through the logic layer allows for simultaneously adjusting the parameters of the rules and the initial prediction network. The integration of a logic layer affords both improved predictions, as well as quantification rule satisfaction and violation during predictor execution. As such, it can serve as a parametric safety- envelope for black box behavior models. We demonstrate how integrating traffic rules improves the predictor performance using real traffic data from the NuScenes dataset.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1pmZ4_XwamYl8X83rtT3Vl8qTKi0-7Ld4/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


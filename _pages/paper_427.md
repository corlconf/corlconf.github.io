---
layout: page
title: "Unsupervised Monocular Depth Learning in Dynamic Scenes"
subtitle: 
description:
permalink: /paper_427/
grand_parent: All Papers
parent: Monday
supp: https://drive.google.com/file/d/1aoflX9_WZdN2PAeoC9z0NS9GllZkTY2-/view
code: https://github.com/google-research/google-research/tree/master/depth_and_motion_learning
youtubeId: 
---

# Unsupervised Monocular Depth Learning in Dynamic Scenes

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/18Dt24fgdRhuAOtxU4GRGDqF0fN0V_0mk/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Hanhan Li (Google AI); Ariel Gordon (Google Research)*; Hang Zhao (Waymo); Vincent Casser (Waymo); Anelia Angelova (Google)**

#### Abstract
We present a method for jointly training the estimation of depth, ego-motion, and a dense 3D translation field of objects relative to the scene, with monocular photometric consistency being the sole source of supervision. We show that this apparently heavily underdetermined problem can be regularized by imposing the following prior knowledge about 3D translation fields: they are sparse, since most of the scene is static, and they tend to be piecewise constant for rigid moving objects. We show that this regularization alone is sufficient to train monocular depth prediction models that exceed the accuracy achieved in prior work for dynamic scenes, including methods that require semantic input.

#### Video 

#### Reviews

#### Rebuttal

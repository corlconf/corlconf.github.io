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
youtube_id: hHlU5G-ONwM
pdf: https://drive.google.com/file/d/18Dt24fgdRhuAOtxU4GRGDqF0fN0V_0mk/view
---

# Unsupervised Monocular Depth Learning in Dynamic Scenes

<a href="https://drive.google.com/file/d/18Dt24fgdRhuAOtxU4GRGDqF0fN0V_0mk/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="https://drive.google.com/file/d/1aoflX9_WZdN2PAeoC9z0NS9GllZkTY2-/view" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="https://github.com/google-research/google-research/tree/master/depth_and_motion_learning" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Hanhan Li (Google AI); Ariel Gordon (Google Research)*; Hang Zhao (Waymo); Vincent Casser (Waymo); Anelia Angelova (Google)**

#### Interactive Session
<a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SESNA52OG3SAYN5MP" target="_blank" rel="noopener noreferrer"><em>2020-11-16, 11:10 - 11:40 PST </em></a>

#### Abstract
We present a method for jointly training the estimation of depth, ego-motion, and a dense 3D translation field of objects relative to the scene, with monocular photometric consistency being the sole source of supervision. We show that this apparently heavily underdetermined problem can be regularized by imposing the following prior knowledge about 3D translation fields: they are sparse, since most of the scene is static, and they tend to be piecewise constant for rigid moving objects. We show that this regularization alone is sufficient to train monocular depth prediction models that exceed the accuracy achieved in prior work for dynamic scenes, including methods that require semantic input.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


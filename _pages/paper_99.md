---
layout: page
title: "Learning RGB-D Feature Embeddings for Unseen Object Instance Segmentation"
subtitle: 
description:
permalink: /paper_99/
grand_parent: All Papers
parent: Wednesday
supp: 
code: 
youtubeId: 
---

# Learning RGB-D Feature Embeddings for Unseen Object Instance Segmentation

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1kk4a8Lco1VnkhkxV3hDnb5qdd28uzZ06/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Yu Xiang (NVIDIA)*; Christopher Xie (University of Washington); Arsalan Mousavian (NVIDIA); Dieter Fox (NVIDIA)**

#### Abstract
Segmenting unseen objects in cluttered scenes is an important skill that robots need to acquire in order to perform tasks in new environments. In this work, we propose a new method for unseen object instance segmentation by learning RGB-D feature embeddings from synthetic data. A metric learning loss function is utilized to learn to produce pixel-wise feature embeddings such that pixels from the same object are close to each other and pixels from different objects are separated in the embedding space. With the learned feature embeddings, a mean shift clustering algorithm can be applied to discover and segment unseen objects. We further improve the segmentation accuracy with a new two-stage clustering algorithm. Our method demonstrates that non-photorealistic synthetic RGB and depth images can be used to learn feature embeddings that transfer well to real-world images for unseen object instance segmentation.

#### Video 

#### Reviews

#### Rebuttal

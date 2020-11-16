---
layout: page
title: "S3CNet: A Sparse Semantic Scene Completion Network for LiDAR Point Clouds"
subtitle: 
description:
permalink: /paper_478/
grand_parent: All Papers
parent: Monday
supp: 
code: 
youtube_id: ircJBFc5PqM
pdf: https://drive.google.com/file/d/1kBrLBZy_eXiT-K6dR8H1BA8DCrJghpxO/view
---

# S3CNet: A Sparse Semantic Scene Completion Network for LiDAR Point Clouds

<a href="https://drive.google.com/file/d/1kBrLBZy_eXiT-K6dR8H1BA8DCrJghpxO/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Ran Cheng (Huawei)*; Christopher Agia (University of Toronto); Yuan Ren (Huawei); Xinhai Li (Huawei); Liu Bingbing (Huawei Noah’s Ark Lab, Canada)**

#### Interactive Session
<a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SESOTOWXD970EO88J" target="_blank" rel="noopener noreferrer"><em>2020-11-16, 11:10 - 11:40 PST </em></a>

#### Abstract
With the increasing reliance of self-driving and similar robotic systems on robust 3D vision, the processing of LiDAR scans with deep convolutional neural networks has become a trend in academia and industry alike. Prior attempts on the challenging Semantic Scene Completion task - which entails the inference of dense 3D structure and associated semantic labels from "sparse" representations - have been, to a degree, successful in small indoor scenes when provided with dense point clouds or dense depth maps often fused with semantic segmentation maps from RGB images. However, the performance of these systems drop drastically when applied to large outdoor scenes characterized by dynamic and exponentially sparser conditions. Likewise, processing of the entire sparse volume becomes infeasible due to memory limitations and workarounds introduce computational inefficiency as practitioners are forced to divide the overall volume into multiple equal segments and infer on each individually, rendering real-time performance impossible. In this work, we formulate a method that subsumes the sparsity of large-scale environments and present S3CNet, a sparse convolution based neural network that predicts the semantically completed scene from a single, unified LiDAR point cloud. We show that our proposed method outperforms all counterparts on the 3D task, achieving state-of-the art results on the SemanticKITTI benchmark. Furthermore, we propose a 2D variant of S3CNet with a multi-view fusion strategy to complement our 3D network, providing robustness to occlusions and extreme sparsity in distant regions. We conduct experiments for the 2D semantic scene completion task and compare the results of our sparse 2D network against several leading LiDAR segmentation models adapted for bird's eye view segmentation on two open-source datasets.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1uLzAzxmdjhWDjFQyRyX_BM9j5ohTwUd7/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


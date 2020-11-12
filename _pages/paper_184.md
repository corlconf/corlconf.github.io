---
layout: page
title: "MuGNet: Multi-Resolution Graph Neural Network for Segmenting Large-Scale Pointclouds"
subtitle: 
description:
permalink: /paper_184/
grand_parent: All Papers
parent: Wednesday
supp: 
code: 
youtubeId: 
---

# MuGNet: Multi-Resolution Graph Neural Network for Segmenting Large-Scale Pointclouds

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1iyQxPL-E4v9pK8SSaYGiaDGa5qiBgbWz/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Liuyue Xie (Carnegie Mellon University)*; Tomotake Furuhata (Carnegie Mellon University); Kenji Shimada (Carnegie Mellon University	)**

#### Interactive Session
*2020-11-18, 12:30 - 13:00 PST*

#### Abstract
In this paper, we propose a multi-resolution deep-learning architecture to segment dense large-scale pointclouds semantically. Dense pointcloud data require a computationally expensive feature encoding process before semantic segmentation. Previous work has used different approaches to drastically downsample from the original pointcloud to utilize common computing hardware. While these approaches can relieve the computation burden to some extent, they are still limited in their processing capability for multiple scans. We present MuGNet, a memory-efficient, end-to-end graph neural network framework to perform semantic segmentation on large-scale pointclouds. We reduce the computation demand by utilizing a graph neural network on the preformed pointcloud graphs and retain the segmentation's precision with a bidirectional network that fuses feature embedding at different resolutions. Our framework has been validated on benchmark datasets, including Stanford Large-Scale 3D Indoor Spaces Dataset(S3DIS) and Virtual KITTI Dataset. We demonstrate that our framework can process up to 45 room scans at once on a single 11 GB GPU while still surpassing other graph-based solutions for segmentation on S3DIS with an 88.5% (+3%) overall accuracy and 69.8% (+7.7%) mIOU accuracy.

#### Video 

#### Reviews

#### Rebuttal

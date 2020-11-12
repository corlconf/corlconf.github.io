---
layout: page
title: "SelfVoxeLO: Self-supervised LiDAR Odometry with Voxel-based Deep Neural Networks"
subtitle: 
description:
permalink: /paper_33/
grand_parent: All Papers
parent: Wednesday
supp: 
code: 
youtubeId: 
---

# SelfVoxeLO: Self-supervised LiDAR Odometry with Voxel-based Deep Neural Networks

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1z3gPe9jKhQJR-JOpPnjh2vcR13n2Y5Vl/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Yan Xu (The Chinese University of Hong Kong)*; Zhaoyang Huang (Zhejiang University); Kwan-Yee Lin (SenseTime Research); Xinge Zhu (The Chinese University of Hong Kong); Jianping Shi (Sensetime Group Limited); Hujun Bao (Zhejiang University); Guofeng Zhang (Zhejiang University); Hongsheng Li (Chinese University of Hong Kong)**

#### Abstract
Recent learning-based LiDAR odometry methods have demonstrated their competitiveness. However, most methods still face two substantial challenges: 1) the 2D projection representation of LiDAR data cannot effectively encode 3D structures from the point clouds; 2) the needs for a large amount of labeled data for training limit the application scope of these methods. In this paper, we propose an self-supervised LiDAR odometry method, dubbed SelfVoxeLO, to tackle these two difficulties. Specifically, we propose a 3D convolution network to process the raw LiDAR data directly, which extracts features that better encode the 3D geometric patterns. To suit our network to self-supervised learning, we design several novel loss functions that utilize the inherent properties of LiDAR point clouds. Moreover, an uncertainty-aware mechanism is incorporated in the loss functions to alleviate the interference of moving objects/noises. We evaluate our method's performances on two large-scale datasets, i.e., KITTI and Apollo-SouthBay.Our method outperforms state-of-the-art unsupervised methods by 27%/32% in terms of translational/rotational errors on the KITTI dataset and also performs well on the Apollo-SouthBay dataset. By including more unlabelled training data, our method can further improve performance comparable to the supervised methods.

#### Video 

#### Reviews

#### Rebuttal

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
youtube_id: 6tAspqi2Xkg
pdf: https://drive.google.com/file/d/1iyQxPL-E4v9pK8SSaYGiaDGa5qiBgbWz/view
---

# MuGNet: Multi-Resolution Graph Neural Network for Segmenting Large-Scale Pointclouds

<a href="https://drive.google.com/file/d/1iyQxPL-E4v9pK8SSaYGiaDGa5qiBgbWz/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Liuyue Xie (Carnegie Mellon University)*; Tomotake Furuhata (Carnegie Mellon University); Kenji Shimada (Carnegie Mellon University	)**

#### Interactive Session
<em>2020-11-18, 12:30 - 13:00 PST </em> | <a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SESE3Q9LQHAY0XN4Z" target="_blank" rel="noopener noreferrer"> PheedLoop Session <i class="fa fa-external-link" aria-hidden="true"></i> </a> 

#### Abstract
In this paper, we propose a multi-resolution deep-learning architecture to segment dense large-scale pointclouds semantically. Dense pointcloud data require a computationally expensive feature encoding process before semantic segmentation. Previous work has used different approaches to drastically downsample from the original pointcloud to utilize common computing hardware. While these approaches can relieve the computation burden to some extent, they are still limited in their processing capability for multiple scans. We present MuGNet, a memory-efficient, end-to-end graph neural network framework to perform semantic segmentation on large-scale pointclouds. We reduce the computation demand by utilizing a graph neural network on the preformed pointcloud graphs and retain the segmentation's precision with a bidirectional network that fuses feature embedding at different resolutions. Our framework has been validated on benchmark datasets, including Stanford Large-Scale 3D Indoor Spaces Dataset(S3DIS) and Virtual KITTI Dataset. We demonstrate that our framework can process up to 45 room scans at once on a single 11 GB GPU while still surpassing other graph-based solutions for segmentation on S3DIS with an 88.5% (+3%) overall accuracy and 69.8% (+7.7%) mIOU accuracy.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1lL-28QlxYVF1-34ZILzB2u7DgB3BIjj4/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


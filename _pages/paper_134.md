---
layout: page
title: "Range Conditioned Dilated Convolutions for Scale Invariant 3D Object Detection"
subtitle: 
description:
permalink: /paper_134/
grand_parent: All Papers
parent: Monday
supp: 
code: 
youtubeId: 
---

# Range Conditioned Dilated Convolutions for Scale Invariant 3D Object Detection

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1MSUoobvqvoWOFHT1AB5_1gjm2NlWywVu/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Alex Bewley (Google)*; Pei Sun (Waymo); Thomas Mensink (Google Research / University of Amsterdam); Dragomir Anguelov (Waymo); Cristian Sminchisescu (Google)**

#### Interactive Session
*2020-11-16, 11:50 - 12:20 PST*

#### Abstract
This paper presents a novel 3D object detection framework that processes LiDAR data directly on its native representation: range images. Benefiting from the compactness of range images, 2D convolutions can efficiently process dense LiDAR data of the scene. To overcome scale sensitivity in this perspective view, a novel range-conditioned dilation (RCD) layer is proposed to dynamically adjust a continuous dilation rate as a function of the measured range. Furthermore, localized soft range gating combined with a 3D box-refinement stage improves robustness in occluded areas, and produces overall more accurate bounding box predictions. On the public large-scale Waymo Open Dataset, our method sets a new baseline for range-based 3D detection, outperforming multiview and voxel-based methods over all ranges with unparalleled performance at long range detection.

#### Video 

#### Reviews

#### Rebuttal

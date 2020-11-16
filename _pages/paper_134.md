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
youtube_id: KHXlAfxIXvE
pdf: https://drive.google.com/file/d/1MSUoobvqvoWOFHT1AB5_1gjm2NlWywVu/view
---

# Range Conditioned Dilated Convolutions for Scale Invariant 3D Object Detection

<a href="https://drive.google.com/file/d/1MSUoobvqvoWOFHT1AB5_1gjm2NlWywVu/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Alex Bewley (Google)*; Pei Sun (Waymo); Thomas Mensink (Google Research / University of Amsterdam); Dragomir Anguelov (Waymo); Cristian Sminchisescu (Google)**

#### Interactive Session
<em>2020-11-16, 11:50 - 12:20 PST </em> | <a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SESMACO1S6RLUGQNO" target="_blank" rel="noopener noreferrer"> PheedLoop Session <i class="fa fa-external-link" aria-hidden="true"></i> </a> 

#### Abstract
This paper presents a novel 3D object detection framework that processes LiDAR data directly on its native representation: range images. Benefiting from the compactness of range images, 2D convolutions can efficiently process dense LiDAR data of the scene. To overcome scale sensitivity in this perspective view, a novel range-conditioned dilation (RCD) layer is proposed to dynamically adjust a continuous dilation rate as a function of the measured range. Furthermore, localized soft range gating combined with a 3D box-refinement stage improves robustness in occluded areas, and produces overall more accurate bounding box predictions. On the public large-scale Waymo Open Dataset, our method sets a new baseline for range-based 3D detection, outperforming multiview and voxel-based methods over all ranges with unparalleled performance at long range detection.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


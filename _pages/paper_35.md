---
layout: page
title: "Learning 3D Dynamic Scene Representations for Robot Manipulation"
subtitle: 
description:
permalink: /paper_35/
grand_parent: All Papers
parent: Tuesday
supp: 
code: https://github.com/columbia-robovision/dsr
youtube_id: da2yFpHG_iw
pdf: https://drive.google.com/file/d/1DyOUmoza18MPjWaocOuLaUBQ363u8pAo/view
---

# Learning 3D Dynamic Scene Representations for Robot Manipulation

<a href="https://drive.google.com/file/d/1DyOUmoza18MPjWaocOuLaUBQ363u8pAo/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="https://github.com/columbia-robovision/dsr" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Zhenjia Xu (Columbia University)*; Zhanpeng He (Columbia University); Jiajun Wu (Stanford University); Shuran Song (Columbia University)**

#### Interactive Session
<a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SES8L13RCX3CUM53K" target="_blank" rel="noopener noreferrer"><em>2020-11-17, 11:50 - 12:20 PST </em></a>

#### Abstract
3D scene representation for robot manipulation should capture three key object properties: permanency – objects that become occluded over time continue to exist; amodal completeness – objects have 3D occupancy, even if only partial observations are available; spatiotemporal continuity – the movement of each object is continuous over space and time. In this paper, we introduce 3D Dynamic Scene Representation (DSR), a 3D volumetric scene representation that simultaneously discovers, tracks, reconstructs objects, and predicts their dynamics while capturing all three properties. We further propose DSR-Net, which learns to aggregate visual observations over multiple interactions to gradually build and refine DSR. Our model achieves state-of-the-art performance in modeling 3D scene dynamics with DSR on both simulated and real data. Combined with model predictive control, DSR-Net enables accurate planning in downstream robotic manipulation tasks such as planar pushing. Code and data are available at dsr-net.cs.columbia.edu.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1YpY-cDmWF5PwogIL0lv3jmAfPqd8UPqb/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


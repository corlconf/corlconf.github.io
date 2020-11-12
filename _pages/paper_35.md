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
youtubeId: 
---

# Learning 3D Dynamic Scene Representations for Robot Manipulation

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1DyOUmoza18MPjWaocOuLaUBQ363u8pAo/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Zhenjia Xu (Columbia University)*; Zhanpeng He (Columbia University); Jiajun Wu (Stanford University); Shuran Song (Columbia University)**

#### Abstract
3D scene representation for robot manipulation should capture three key object properties: permanency – objects that become occluded over time continue to exist; amodal completeness – objects have 3D occupancy, even if only partial observations are available; spatiotemporal continuity – the movement of each object is continuous over space and time. In this paper, we introduce 3D Dynamic Scene Representation (DSR), a 3D volumetric scene representation that simultaneously discovers, tracks, reconstructs objects, and predicts their dynamics while capturing all three properties. We further propose DSR-Net, which learns to aggregate visual observations over multiple interactions to gradually build and refine DSR. Our model achieves state-of-the-art performance in modeling 3D scene dynamics with DSR on both simulated and real data. Combined with model predictive control, DSR-Net enables accurate planning in downstream robotic manipulation tasks such as planar pushing. Code and data are available at dsr-net.cs.columbia.edu.

#### Video 

#### Reviews

#### Rebuttal

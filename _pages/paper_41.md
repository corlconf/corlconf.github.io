---
layout: page
title: "Fit2Form: 3D Generative Model for Robot Gripper Form Design"
subtitle: 
description:
permalink: /paper_41/
grand_parent: All Papers
parent: Wednesday
supp: https://drive.google.com/file/d/1spi8c-deHjEnpxERxb7fr9rXvcw6-7at/view
code: https://github.com/columbia-robovision/fit2form
youtubeId: 
---

# Fit2Form: 3D Generative Model for Robot Gripper Form Design

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1o0xq3cFVR65JSCayZSA-DkWg_VtJBVtB/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Huy Ha (Columbia University); Shubham Agrawal (Columbia University); Shuran Song (Columbia University)***

#### Interactive Session
*2020-11-18, 11:10 - 11:40 PST*

#### Abstract
The 3D shape of a robot's end-effector plays a critical role in determining it's functionality and overall performance. Many of today's industrial applications rely on highly customized gripper design for a given task to ensure the system's robustness and accuracy.  However, the process of manual hardware design is both costly and time-consuming, and the quality of the design is also dependent on the engineer's experience and domain expertise, which can easily be out-dated or inaccurate.  The goal of this paper is to use machine learning algorithms to automate this design process and generate task-specific gripper designs that satisfy a set of pre-defined design objectives. We model the design objectives by training a Fitness network to predict their values for a pair of gripper fingers and a grasp object. This Fitness network is then used to provide training supervision to a 3D Generative network that produces a pair of 3D finger geometries for the target grasp object. Our experiments demonstrate that the proposed 3D generative design framework generates parallel jaw gripper finger shapes that achieve more stable and robust grasps as compared to other general-purpose and task-specific gripper design algorithms.

#### Video 

#### Reviews

#### Rebuttal

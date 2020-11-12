---
layout: page
title: "Inverting the Pose Forecasting Pipeline with SPF2: Sequential Pointcloud Forecasting for Sequential Pose Forecasting"
subtitle: 
description:
permalink: /paper_6/
grand_parent: All Papers
parent: Tuesday
supp: 
code: https://github.com/xinshuoweng/SPF2
youtubeId: 
---

# Inverting the Pose Forecasting Pipeline with SPF2: Sequential Pointcloud Forecasting for Sequential Pose Forecasting

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1G-9Pjp4K_RVDKL7OdoX7_fCphGGHapB2/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Xinshuo Weng (Carnegie Mellon University)*; Jianren Wang (Carnegie Mellon University); Sergey Levine (UC Berkeley); Kris Kitani (Carnegie Mellon University); Nicholas Rhinehart (UC Berkeley)**

#### Abstract
Many autonomous systems forecast aspects of the future in order to aid decision-making. For example, self-driving vehicles and robotic manipulation systems often forecast future object poses by first detecting and tracking objects. However, this detect-then-forecast pipeline is expensive to scale, as pose forecasting algorithms typically require labeled sequences of object poses, which are costly to obtain in 3D space. Can we scale performance without requiring additional labels? We hypothesize yes, and propose inverting the detect-then-forecast pipeline. Instead of detecting, tracking and then forecasting the objects, we propose to first forecast 3D sensor data (e.g., point clouds with 100k points) and then detect/track objects on the predicted point cloud sequences to obtain future poses, i.e., a forecast-then-detect pipeline. This inversion makes it less expensive to scale pose forecasting, as the sensor data forecasting task requires no labels. Part of this work's focus is on the challenging first step - Sequential Pointcloud Forecasting (SPF), for which we also propose an effective approach, SPFNet. To compare our forecast-then-detect pipeline relative to the detect-then-forecast pipeline, we propose an evaluation procedure and two metrics. Through experiments on a robotic manipulation dataset and two driving datasets, we show that SPFNet is effective for the SPF task, our forecast-then-detect pipeline outperforms the detect-then-forecast approaches to which we compared, and that pose forecasting performance improves with the addition of unlabeled data. Our project website is <a href="http://www.xinshuoweng.com/projects/SPF2" target="_blank">http://www.xinshuoweng.com/projects/SPF2</a>

#### Video 

#### Reviews

#### Rebuttal

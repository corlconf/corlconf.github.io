---
layout: page
title: "Self-Supervised 3D Keypoint Learning for Ego-Motion Estimation"
subtitle: 
description:
permalink: /paper_464/
grand_parent: All Papers
parent: Monday
supp: 
code: 
youtubeId: 
---

# Self-Supervised 3D Keypoint Learning for Ego-Motion Estimation

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1ECF2dBSDd2Wmlgg1yf3J4VkPJUP0kjX9/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Jiexiong Tang (KTH Royal Institute of Technology)*; Rareș  Ambruș (Toyota Research Institute); Vitor Guizilini (Toyota Research Institute); Sudeep Pillai (Toyota Research Institute); Hanme Kim (Toyota Research Institute); Patric Jensfelt (Royal Institute of Technology); Adrien Gaidon (Toyota Research Institute)**

#### Abstract
Detecting and matching robust viewpoint-invariant keypoints is critical for visual SLAM and Structure-from-Motion. State-of-the-art learning-based methods generate training samples via homography adaptation to create 2D synthetic views with known keypoint matches from a single image. This approach does not, however, generalize to non-planar 3D scenes with illumination variations commonly seen in real-world videos. In this work, we propose self-supervised learning depth-aware keypoints from unlabeled videos directly. We jointly learn keypoint and depth estimation networks by combining appearance and geometric matching via a differentiable structure-from-motion module based on Procrustean residual pose correction. We show how our self-supervised keypoints can be trivially incorporated into state-of-the-art visual odometry frameworks for robust and accurate ego-motion estimation of autonomous vehicles in real-world conditions.

#### Video 

#### Reviews

#### Rebuttal

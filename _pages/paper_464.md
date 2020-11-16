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
youtube_id: aU5zzUeKmtg
pdf: https://drive.google.com/file/d/1ECF2dBSDd2Wmlgg1yf3J4VkPJUP0kjX9/view
---

# Self-Supervised 3D Keypoint Learning for Ego-Motion Estimation

<a href="https://drive.google.com/file/d/1ECF2dBSDd2Wmlgg1yf3J4VkPJUP0kjX9/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Jiexiong Tang (KTH Royal Institute of Technology)*; Rareș  Ambruș (Toyota Research Institute); Vitor Guizilini (Toyota Research Institute); Sudeep Pillai (Toyota Research Institute); Hanme Kim (Toyota Research Institute); Patric Jensfelt (Royal Institute of Technology); Adrien Gaidon (Toyota Research Institute)**

#### Interactive Session
<a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SESZ30XQR3WRXHDNW" target="_blank" rel="noopener noreferrer"><em>2020-11-16, 11:50 - 12:20 PST </em></a>

#### Abstract
Detecting and matching robust viewpoint-invariant keypoints is critical for visual SLAM and Structure-from-Motion. State-of-the-art learning-based methods generate training samples via homography adaptation to create 2D synthetic views with known keypoint matches from a single image. This approach does not, however, generalize to non-planar 3D scenes with illumination variations commonly seen in real-world videos. In this work, we propose self-supervised learning depth-aware keypoints from unlabeled videos directly. We jointly learn keypoint and depth estimation networks by combining appearance and geometric matching via a differentiable structure-from-motion module based on Procrustean residual pose correction. We show how our self-supervised keypoints can be trivially incorporated into state-of-the-art visual odometry frameworks for robust and accurate ego-motion estimation of autonomous vehicles in real-world conditions.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1hN6KFn0uMcJKqCBIyMzJBcglihAQZvxp/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


---
layout: page
title: "Self-Supervised Object-in-Gripper Segmentation from Robotic Motions"
subtitle: 
description:
permalink: /paper_275/
grand_parent: All Papers
parent: Wednesday
supp: 
code: 
youtube_id: LPsLYMinWKU
pdf: https://drive.google.com/file/d/1_MnPxUkNimsj8peqtuc4y-wL6-OgFvxX/view
---

# Self-Supervised Object-in-Gripper Segmentation from Robotic Motions

<a href="https://drive.google.com/file/d/1_MnPxUkNimsj8peqtuc4y-wL6-OgFvxX/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Wout Boerdijk (DLR)*; Martin Sundermeyer (German Aerospace Center (DLR)); Maximilian Durner (DLR); Rudolph Triebel (German Aerospace Center (DLR))**

#### Interactive Session
<a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SES0ELNJN2GACPZ16" target="_blank" rel="noopener noreferrer"><em>2020-11-18, 11:50 - 12:20 PST </em></a>

#### Abstract
Accurate object segmentation is a crucial task in the context of robotic manipulation. However, creating sufficient annotated training data for neural networks is particularly time consuming and often requires manual labeling. To this end, we propose a simple, yet robust solution for learning to segment unknown objects grasped by a robot. Specifically, we exploit motion and temporal cues in RGB video sequences. Using optical flow estimation we first learn to predict segmentation masks of our given manipulator. Then, these annotations are used in combination with motion cues to automatically distinguish between background, manipulator and unknown, grasped object. In contrast to existing systems our approach is fully self-supervised and independent of precise camera calibration, 3D models or potentially imperfect depth data. We perform a thorough comparison with alternative baselines and approaches from literature. The object masks and views are shown to be suitable training data for segmentation networks that generalize to novel environments and also allow for watertight 3D reconstruction.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


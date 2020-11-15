---
layout: page
title: "Reconfigurable Voxels: A New Representation for LiDAR-Based Point Clouds"
subtitle: 
description:
permalink: /paper_58/
grand_parent: All Papers
parent: Monday
supp: https://drive.google.com/file/d/1YHnFr6TTuzBZa8Bl2HvEd283YGrreSDc/view
code: 
youtube_id: qooEVl8XF9o
pdf: https://drive.google.com/file/d/1jzvkir7oheEpyGkApdf-tps-HRmezXX9/view
---

# Reconfigurable Voxels: A New Representation for LiDAR-Based Point Clouds

<a href="https://drive.google.com/file/d/1jzvkir7oheEpyGkApdf-tps-HRmezXX9/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="https://drive.google.com/file/d/1YHnFr6TTuzBZa8Bl2HvEd283YGrreSDc/view" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Tai Wang (The Chinese University of Hong Kong)*; Xinge Zhu (The Chinese University of Hong Kong); Dahua Lin (The Chinese University of Hong Kong)**

#### Interactive Session
*2020-11-16, 12:30 - 13:00 PST* 

#### Abstract
LiDAR is an important method for autonomous driving systems to sense the environment. The point clouds obtained by LiDAR typically exhibit sparse and irregular distribution, thus posing great challenges to the detection of 3D objects, especially those that are small and distant. To tackle this difficulty, we propose Reconfigurable Voxels, a new approach to constructing representations from 3D point clouds. Specifically, we devise a biased random walk scheme, which adaptively covers each neighborhood with a fixed number of voxels based on the local spatial distribution and produces a representation by integrating the points in the chosen neighbors. We found empirically that this approach effectively improves the stability of voxel features, especially for sparse regions. Experimental results on multiple benchmarks, including nuScenes, Lyft, and KITTI, show that this new representation can remarkably improve the detection performance for small and distant objects, without incurring noticeable overhead cost

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1GZ65oKsu-QYQIgI4NHYTWh3rwCQKcyOF/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


---
layout: page
title: "Recovering and Simulating Pedestrians in the Wild"
subtitle: 
description:
permalink: /paper_89/
grand_parent: All Papers
parent: Monday
supp: 
code: 
youtubeId: 
pdf: https://drive.google.com/file/d/1NyZRBrpOpdSkh1MH6mPJm5SB5GHzvORl/view
---

# Recovering and Simulating Pedestrians in the Wild

<a href="https://drive.google.com/file/d/1NyZRBrpOpdSkh1MH6mPJm5SB5GHzvORl/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Ze Yang (Uber ATG, University of Toronto)*; Sivabalan Manivasagam (Uber ATG, University of Toronto); Ming Liang (Uber); Bin Yang (Uber ATG & University of Toronto); Wei-Chiu Ma (MIT); Raquel Urtasun (Uber ATG)**

#### Interactive Session
*2020-11-16, 12:30 - 13:00 PST*

#### Abstract
Sensor simulation is a key component for testing the performance of self-driving vehicles and for data augmentation to better train perception systems. Typical approaches rely on artists to create both 3D assets and their animations to generate a new scenario. This, however, does not scale. In contrast, we propose to recover the shape and motion of pedestrians from sensor readings captured in the wild by a self-driving car driving around. Towards this goal, we formulate the problem as energy minimization in a deep structured model that exploits human shape priors, reprojection consistency with 2D poses extracted from images, and a ray-caster that encourages the reconstructed mesh to agree with the LiDAR readings. Importantly, we do not require any ground-truth 3D scans or 3D pose annotations. We then incorporate the reconstructed pedestrian assets bank in a realistic LiDAR simulation system by performing motion retargeting, and show that the simulated LiDAR data can be used to significantly reduce the amount of annotated real-world data required for visual perception tasks.

#### Video 

#### Reviews

#### Rebuttal


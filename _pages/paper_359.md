---
layout: page
title: "Volumetric Grasping Network: Real-time 6 DOF Grasp Detection in Clutter"
subtitle: 
description:
permalink: /paper_359/
grand_parent: All Papers
parent: Monday
supp: 
code: https://github.com/ethz-asl/vgn
youtubeId: 
---

# Volumetric Grasping Network: Real-time 6 DOF Grasp Detection in Clutter

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/14KKgyR-jiyyaDYzsPv7UpZaHmeVTakH9/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Michel Breyer (ETH)*; Jen Jen Chung (ETH Zurich); Lionel Ott (The University of Sydney); Roland Siegwart (ETH Zürich, Autonomous Systems Lab); Juan Nieto (ETH Zürich Autonomous Systems Lab)**

#### Abstract
General robot grasping in clutter requires the ability to synthesize grasps that work for previously unseen objects and that are also robust to physical interactions, such as collisions with other objects in the scene. In this work, we design and train a network that predicts 6 DOF grasps from 3D scene information gathered from an on-board sensor such as a wrist-mounted depth camera. Our proposed Volumetric Grasping Network (VGN) accepts a Truncated Signed Distance Function (TSDF) representation of the scene and directly outputs the predicted grasp quality and the associated gripper orientation and opening width for each voxel in the queried 3D volume. We show that our approach can plan grasps in only 10 ms and is able to clear 92% of the objects in real-world clutter removal experiments without the need for explicit collision checking. The real-time capability opens up the possibility for closed-loop grasp planning, allowing robots to handle disturbances, recover from errors and provide increased robustness.

#### Video 

#### Reviews

#### Rebuttal

---
layout: page
title: "Robust Quadrupedal Locomotion on Sloped Terrains: A Linear Policy Approach"
subtitle: 
description:
permalink: /paper_501/
grand_parent: All Papers
parent: Tuesday
supp: 
code: https://github.com/StochLab/SlopedTerrainLinearPolicy
youtubeId: 
---

# Robust Quadrupedal Locomotion on Sloped Terrains: A Linear Policy Approach

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/194fCa0jSmn2UaP_OTgawEo8IvwmE8DZz/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Kartik Paigwar (Indian Institute of Science)*; Lokesh Krishna (IISc); sashank tirumala (IISC Bangalore); naman khetan (IISc); aditya varma (iisc); ashish joglekar (IISc); Shalabh Bhatnagar (Indian Institute of Science (IISc) Bangalore); Ashitava Ghosal (Indian Institute of Science); Bharadwaj Amrutur (IISc Bangalore); Shishir Kolathaya (IISc)**

#### Abstract
In this paper, with a view toward fast deployment of locomotion gaits in low-cost hardware, we use a linear policy for realizing end-foot trajectories in the quadruped robot, Stoch 2. In particular, the parameters of the end-foot trajectories are shaped via a linear feedback policy that takes the torso orientation and the terrain slope as inputs. The corresponding desired joint angles are obtained via an inverse kinematics solver and tracked via a PID control law. Augmented Random Search, a model-free and a gradient-free learning algorithm is used to train this linear policy. Simulation results show that the resulting walking is robust to terrain slope variations and external pushes. This methodology is not only computationally light-weight but also uses minimal sensing and actuation capabilities in the robot, thereby justifying the approach.

#### Video 

#### Reviews

#### Rebuttal

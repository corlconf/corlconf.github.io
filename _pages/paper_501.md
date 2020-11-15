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
youtube_id: TKarU1bY32U
pdf: https://drive.google.com/file/d/194fCa0jSmn2UaP_OTgawEo8IvwmE8DZz/view
---

# Robust Quadrupedal Locomotion on Sloped Terrains: A Linear Policy Approach

<a href="https://drive.google.com/file/d/194fCa0jSmn2UaP_OTgawEo8IvwmE8DZz/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="https://github.com/StochLab/SlopedTerrainLinearPolicy" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Kartik Paigwar (Indian Institute of Science)*; Lokesh Krishna (IISc); sashank tirumala (IISC Bangalore); naman khetan (IISc); aditya varma (iisc); ashish joglekar (IISc); Shalabh Bhatnagar (Indian Institute of Science (IISc) Bangalore); Ashitava Ghosal (Indian Institute of Science); Bharadwaj Amrutur (IISc Bangalore); Shishir Kolathaya (IISc)**

#### Interactive Session
*2020-11-17, 12:30 - 13:00 PST* 

#### Abstract
In this paper, with a view toward fast deployment of locomotion gaits in low-cost hardware, we use a linear policy for realizing end-foot trajectories in the quadruped robot, Stoch 2. In particular, the parameters of the end-foot trajectories are shaped via a linear feedback policy that takes the torso orientation and the terrain slope as inputs. The corresponding desired joint angles are obtained via an inverse kinematics solver and tracked via a PID control law. Augmented Random Search, a model-free and a gradient-free learning algorithm is used to train this linear policy. Simulation results show that the resulting walking is robust to terrain slope variations and external pushes. This methodology is not only computationally light-weight but also uses minimal sensing and actuation capabilities in the robot, thereby justifying the approach.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1nmOa8FSjP6d_-4otvtBYwgLtFt8Zctxe/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


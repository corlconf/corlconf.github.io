---
layout: page
title: "Learning an Expert Skill-Space for Replanning Dynamic  Quadruped Locomotion over Obstacles"
subtitle: 
description:
permalink: /paper_346/
grand_parent: All Papers
parent: Monday
supp: 
code: 
youtube_id: w3v1BingoXQ
pdf: https://drive.google.com/file/d/1fKupzqWuDCtoh9Wr6_o72unDxObxmfK4/view
---

# Learning an Expert Skill-Space for Replanning Dynamic  Quadruped Locomotion over Obstacles

<a href="https://drive.google.com/file/d/1fKupzqWuDCtoh9Wr6_o72unDxObxmfK4/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**David Surovik (University of Oxford)*; Oliwier Melon (University of Oxford); Mathieu Geisert (University of Oxford); Maurice Fallon (University of Oxford); Ioannis Havoutis ("Oxford Robotics Institute, Universtity of Oxford")**

#### Interactive Session
*2020-11-16, 11:50 - 12:20 PST* 

#### Abstract
Function approximators are increasingly being considered as a tool for generating robot motions that are temporally extended and express foresight about the scenario at hand. While these longer behaviors are often necessary or beneficial, they also induce multimodality in the decision space, which complicates the training of a regression model on expert data. Motivated by the problem of quadrupedal locomotion over obstacles, we apply an approach that disentangles modal variation from task-to-solution regression by using a conditional variational autoencoder. The resulting decoder is a regression model that outputs trajectories based on the task and a real-valued latent mode vector representing a style of behavior. With the task consisting of robot-relative descriptions of the state, the goal, and nearby obstacles, this model is suitable for receding-horizon generation of structured dynamic motion. We test this approach, along with a trajectory library baseline method, for producing sustained locomotion plans that use a generalized gait. Both options strongly bias planned footholds away from obstacle regions, while the multimodal regressor is far less susceptible to violating kinematic constraints. We conclude by identifying further prospective benefits of the continuous latent mode representation, along with targets for future integration into a hardware-deployable pipeline including perception and control.


#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/129BHjGRuzXKT_z9H-BkWP256n-INvBOd/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


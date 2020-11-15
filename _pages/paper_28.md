---
layout: page
title: "From pixels to legs: Hierarchical learning of quadruped locomotion"
subtitle: 
description:
permalink: /paper_28/
grand_parent: All Papers
parent: Tuesday
supp: 
code: 
youtube_id: o4PDEnqjT0I
pdf: https://drive.google.com/file/d/1B6HiTuKc8MOA8CsY32uJSzyKSnDjCHsb/view
---

# From pixels to legs: Hierarchical learning of quadruped locomotion

<a href="https://drive.google.com/file/d/1B6HiTuKc8MOA8CsY32uJSzyKSnDjCHsb/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Deepali Jain (Google)*; Ken Caluwaerts (Google); Atil Iscen (Google)**

#### Interactive Session
*2020-11-17, 11:50 - 12:20 PST* 

#### Abstract
Legged robots navigating crowded scenes and complex terrains in the real world are required to execute dynamic leg movements while processing visual input for obstacle avoidance and path planning. We show that a quadruped robot can acquire both of these skills by means of hierarchical reinforcement learning (HRL). By virtue of their hierarchical structure, our policies learn to implicitly break down this joint problem by concurrently learning High Level (HL) and Low Level (LL) neural network policies. These two levels are connected by a low dimensional hidden layer, which we call latent command. HL receives a first-person camera view, whereas LL receives the latent command from HL and the robot's on-board sensors to control its actuators. We train policies to walk in two different environments: a curved cliff and a maze. We show that hierarchical policies can concurrently learn to locomote and navigate in these environments, and show they are more efficient than non-hierarchical neural network policies. This architecture also allows for knowledge reuse across tasks. LL networks trained on one task can be transferred to a new task in a new environment. Finally HL, which processes camera images, can be evaluated at much lower and varying frequencies compared to LL, thus reducing computation times and bandwidth requirements.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/183VGipuP_LP_J6-deZXQkqbCArFdwIiE/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


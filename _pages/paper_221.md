---
layout: page
title: "Towards General and Autonomous Learning of Core Skills: A Case Study in Locomotion"
subtitle: 
description:
permalink: /paper_221/
grand_parent: All Papers
parent: Wednesday
supp: 
code: 
youtubeId: 
---

# Towards General and Autonomous Learning of Core Skills: A Case Study in Locomotion

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1LlGrYCXlNJYRc7XzN_3CwQd_QdmDLb-F/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Roland Hafner (Google DeepMind)*; Tim Hertweck (DeepMind); Philipp Kloeppner (TU Darmstadt); Michael Bloesch (Google); Michael Neunert (Google DeepMind); Markus Wulfmeier (DeepMind); Saran  Tunyasuvunakool (DeepMind); Nicolas Heess (DeepMind); Martin Riedmiller (DeepMind)**

#### Abstract
Modern Reinforcement Learning (RL) algorithms promise to solve difficult motor control problems directly from raw sensory inputs. Their attraction is due in part to the fact that they can represent a general class of methods that allow to learn a solution with a reasonably set reward and minimal prior knowledge, even in situations where it is difficult or expensive for a human expert. For RL to truly make good on this promise, however, we need algorithms and learning setups that can work across a broad range of problems with minimal problem specific adjustments or engineering. In this paper, we study this idea of generality in the locomotion domain. We develop a learning framework that can learn sophisticated locomotion behaviour for a wide spectrum of legged robots, such as bipeds, tripeds, quadrupeds and hexapods, including wheeled variants.
Our learning framework relies on a data-efficient, off-policy multi-task RL algorithm and a small set of reward functions that are semantically identical across robots.
To underline the general applicability of the method, we keep the hyper-parameter settings and reward definitions constant across experiments and rely exclusively on on-board sensing. For nine different types of robots, including a real-world quadruped robot, we demonstrate that the same algorithm can rapidly learn diverse and reusable locomotion skills without any platform specific adjustments or additional instrumentation of the learning setup.

#### Video 

#### Reviews

#### Rebuttal

---
layout: page
title: "Assisted Perception: Optimizing Observations to Communicate State"
subtitle: 
description:
permalink: /paper_158/
grand_parent: All Papers
parent: Tuesday
supp: 
code: https://github.com/rddy/ASE
youtubeId: 
---

# Assisted Perception: Optimizing Observations to Communicate State

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1QcWJ_gLglCOmLgrRV34cbtLX1Ai9JvBX/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Siddharth Reddy (UC Berkeley)*; Sergey Levine (UC Berkeley); Anca Dragan (EECS Department, University of California, Berkeley)**

#### Abstract
We aim to help users estimate the state of the world in tasks like robotic teleoperation and navigation with visual impairment, where user may have systematic biases that lead to suboptimal behavior: they might struggle to process observations from multiple sensors simultaneously, receive delayed observations, or underestimate distances to obstacles. While we cannot directly change the user's internal beliefs or their internal state estimation process, our insight is that we can still assist them by modifying the user's observations. Instead of showing the user their true observations, ***we synthesize new observations that lead to more accurate internal state estimates when processed by the user***. We refer to this method as assistive state estimation (ASE): an automated assistant uses the true observations to infer the state of the world, then generates a modified observation for the user to consume (e.g., through an augmented reality interface), and optimizes the modification to induce the user's new beliefs to match the assistant's current beliefs. To predict the effect of the modified observation on the user's beliefs, ASE learns a model of the user's state estimation process: after each task completion, it searches for a model that would have led to beliefs that explain the user's actions. We evaluate ASE in a user study with 12 participants who each perform four tasks: two tasks with known user biases - bandwidth-limited image classification and a driving video game with observation delay - and two with unknown biases that our method has to learn - guided 2D navigation and a lunar lander teleoperation video game. ASE's general-purpose approach to synthesizing informative observations enables a different assistance strategy to emerge in each domain, such as quickly revealing informative pixels to speed up image classification, using a dynamics model to undo observation delay in driving, identifying nearby landmarks for navigation, and exaggerating a visual indicator of tilt in the lander game. The results show that ASE substantially improves the task performance of users with bandwidth constraints, observation delay, and other unknown biases.

#### Video 

#### Reviews

#### Rebuttal

---
layout: page
title: "Chaining Behaviors from Data with Model-Free Reinforcement Learning"
subtitle: 
description:
permalink: /paper_481/
grand_parent: All Papers
parent: Monday
supp: 
code: https://github.com/avisingh599/cog
youtubeId: 
---

# Chaining Behaviors from Data with Model-Free Reinforcement Learning

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/12UXSytPrxJH6yleXjyujw-sLMb0g_2Kg/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Avi Singh (UC Berkeley)*; Albert Yu (UC Berkeley); Jonathan Yang (UC Berkeley); Jesse Zhang (UC Berkeley); Aviral Kumar (UC Berkeley); Sergey Levine (UC Berkeley)**

#### Abstract
Reinforcement learning has been applied to a wide variety of robotics problems, but most of such applications involve collecting data from scratch for each new task. Since the amount of robot data we can collect for any single task is limited by time and cost considerations, the learned behavior is typically narrow: the policy can only execute the task in a handful of scenarios that it was trained on. What if there was a way to incorporate a large amount of prior data, either from previously solved tasks or from unsupervised or undirected environment interaction, to extend and generalize learned behaviors? 
While most prior work on extending robotic skills using pre-collected data focuses on building explicit hierarchies or skill decompositions, we show in this paper that we can reuse prior data to extend new skills simply through model-free reinforcement learning via dynamic programming. We show that even when the prior data does not actually succeed at solving the new task, it can still be utilized for learning a better policy, by providing the agent with a broader understanding of the mechanics of its environment. We demonstrate the effectiveness of such an approach by chaining together several behaviors seen in prior datasets for solving a new task, with our hardest experimental setting involving composing four robotic skills in a row: picking, placing, drawer opening, and grasping, where a +1/0 sparse reward is provided only on task completion. We train our policies in an end-to-end fashion, mapping high-dimensional image observations to low-level robot control commands, and present results in both simulated and real world domains.

#### Video 

#### Reviews

#### Rebuttal

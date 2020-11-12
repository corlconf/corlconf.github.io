---
layout: page
title: "Positive-Unlabeled Reward Learning"
subtitle: 
description:
permalink: /paper_45/
grand_parent: All Papers
parent: Tuesday
supp: 
code: 
youtubeId: 
---

# Positive-Unlabeled Reward Learning

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1RATFBOenj9A0gPCHq6z74u03l0WsS8Kg/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Danfei Xu (Stanford University)*; Misha Denil (DeepMind)**

#### Interactive Session
*2020-11-17, 11:50 - 12:20 PST*

#### Abstract
Learning reward functions from data is a promising path towards achieving scalable Reinforcement Learning (RL) for robotics. However, a major challenge in training agents from learned reward models is that the agent can learn to exploit errors in the reward model to achieve high reward behaviors that do not correspond to the intended task. These reward delusions can lead to unintended and even dangerous behaviors. On the other hand, adversarial imitation learning frameworks (Ho et al., 2016) tend to suffer the opposite problem, where the discriminator learns to trivially distinguish agent and expert behavior, resulting in reward models that produce low reward signal regardless of the input state.
In this paper, we connect these two classes of reward learning methods to positive-unlabeled (PU) learning, and show that by applying a large-scale PU learning algorithm to the reward learning problem, we can address both the reward under- and over-estimation problems simultaneously. Our approach drastically improves both GAIL and supervised reward learning, without any additional assumptions.

#### Video 

#### Reviews

#### Rebuttal

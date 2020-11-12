---
layout: page
title: "Safe Policy Learning for Continuous Control"
subtitle: 
description:
permalink: /paper_171/
grand_parent: All Papers
parent: Tuesday
supp: 
code: 
youtubeId: 
---

# Safe Policy Learning for Continuous Control

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1sBMJA0ekiqiNIYptNM8uqv3oapm9UW4z/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Yinlam Chow (Google AI)*; Ofir Nachum (Google); Aleksandra Faust (Google Brain); Edgar Dueñez-Guzman (DeepMind); Mohammad Ghavamzadeh (Google Research)**

#### Interactive Session
*2020-11-17, 11:10 - 11:40 PST*

#### Abstract
We study continuous action reinforcement learning problems in which it is crucial that the agent interacts with the environment only through near-safe policies, i.e.,~policies that keep the agent in desirable situations, both during training and at convergence. We formulate these problems as <em>constrained</em> Markov decision processes (CMDPs) and present safe policy optimization algorithms that are based on a Lyapunov approach to solve them. Our algorithms can use any standard policy gradient (PG) method, such as deep deterministic policy gradient (DDPG) or proximal policy optimization (PPO), to train a neural network policy, while enforcing near-constraint satisfaction for every policy update by projecting either the policy parameter or the selected action onto the set of feasible solutions induced by the state-dependent linearized Lyapunov constraints. Compared to the existing constrained PG algorithms, ours are more data efficient as they are able to utilize both on-policy and off-policy data. Moreover, in practice our action-projection algorithm often leads to less conservative policy updates and allows for natural integration into an end-to-end PG training pipeline. We evaluate our algorithms and compare them with the state-of-the-art baselines on several simulated (MuJoCo) tasks, as well as a real-world robot obstacle-avoidance problem, demonstrating their effectiveness in terms of balancing performance and constraint satisfaction.

#### Video 

#### Reviews

#### Rebuttal

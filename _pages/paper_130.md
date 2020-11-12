---
layout: page
title: "Motion Planner Augmented Reinforcement Learning for Robot Manipulation in Obstructed Environments"
subtitle: 
description:
permalink: /paper_130/
grand_parent: All Papers
parent: Tuesday
supp: 
code: https://github.com/clvrai/mopa-rl
youtubeId: 
---

# Motion Planner Augmented Reinforcement Learning for Robot Manipulation in Obstructed Environments

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1asruNpTN20J9c0D-dA-gdt-07GoCDjGF/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Jun Yamada (University of Southern California); Youngwoon Lee (University of Southern California)*; Gautam Salhotra (University of Southern California); Karl Pertsch (University of Southern California); Max Pflueger (University of Southern California); Gaurav Sukhatme (University of Southern California); Joseph Lim (USC); Peter Englert (University of Southern California)**

#### Abstract
Deep reinforcement learning (RL) agents are able to learn contact-rich manipulation tasks by maximizing a reward signal, but require large amounts of experience, especially in environments with many obstacles that complicate exploration. In contrast, motion planners use explicit models of the agent and environment to plan collision-free paths to faraway goals, but suffer from inaccurate models in tasks that require contacts with the environment. To combine the benefits of both approaches, we propose motion planner augmented RL (MoPA-RL) which augments the action space of an RL agent with the long-horizon planning capabilities of motion planners. Based on the magnitude of the action, our approach smoothly transitions between directly executing the action and invoking a motion planner. We evaluate our approach on various simulated manipulation tasks and compare it to alternative action spaces in terms of learning efficiency and safety. The experiments demonstrate that MoPA-RL increases learning efficiency, leads to a faster exploration, and results in safer policies that avoid collisions with the environment. Videos and code are available at <a href="https://clvrai.com/mopa-rl" target="_blank">https://clvrai.com/mopa-rl</a>.

#### Video 

#### Reviews

#### Rebuttal

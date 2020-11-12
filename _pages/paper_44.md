---
layout: page
title: "Accelerating Reinforcement Learning with Learned Skill Priors"
subtitle: 
description:
permalink: /paper_44/
grand_parent: All Papers
parent: Wednesday
supp: 
code: https://github.com/clvrai/spirl
youtubeId: 
---

# Accelerating Reinforcement Learning with Learned Skill Priors

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1svZaKvUrdVpBZN6XWWJC1bGUCX7pbQvw/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Karl Pertsch (University of Southern California)*; Youngwoon Lee (University of Southern California); Joseph Lim (USC)**

#### Abstract
Intelligent agents rely heavily on prior experience when learning a new task, yet most modern reinforcement learning (RL) approaches learn every task from scratch. One approach for leveraging prior knowledge is to transfer skills learned on prior tasks to the new task. However, as the amount of prior experience increases, the number of transferable skills grows too, making it challenging to explore the full set of available skills during downstream learning. Yet, intuitively, not all skills should be explored with equal probability; for example information about the current state can hint which skills are promising to explore. In this work, we propose to implement this intuition by learning a prior over skills. We propose a deep latent variable model that jointly learns an embedding space of skills and the skill prior from offline agent experience. We then extend common maximum-entropy RL approaches to use skill priors to guide downstream learning. We validate our approach, SPiRL (Skill-Prior RL), on complex navigation and robotic manipulation tasks and show that learned skill priors are essential for effective skill transfer from rich datasets. Videos and code are available at <a href="https://clvrai.com/spirl" target="_blank">https://clvrai.com/spirl</a>.

#### Video 

#### Reviews

#### Rebuttal

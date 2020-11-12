---
layout: page
title: "Learning Dexterous Manipulation from Suboptimal Experts"
subtitle: 
description:
permalink: /paper_198/
grand_parent: All Papers
parent: Tuesday
supp: 
code: 
youtubeId: 
---

# Learning Dexterous Manipulation from Suboptimal Experts

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1hkLqD-pTWEax5DDpYmzGKvNaYycfxxoC/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Rae Jeong (DeepMind)*; Jost Tobias Springenberg (DeepMind); Jackie Kay (DeepMind); Dan Zheng (DeepMind); Alexandre Galashov (DeepMind); Nicolas Heess (DeepMind); Francesco Nori (DeepMind)**

#### Abstract
Learning dexterous manipulation in high-dimensional state-action spaces is an important open challenge with exploration presenting a major bottleneck. Although in many cases the learning process could be guided by demonstrations or other suboptimal experts, current RL algorithms for continuous action spaces often fail to effectively utilize combinations of highly off-policy expert data and on-policy exploration data. As a solution, we introduce Relative Entropy Q-Learning (REQ), a simple policy iteration algorithm that combines ideas from successful offline and conventional RL algorithms. It represents the optimal policy via importance sampling from a learned prior and is well-suited to take advantage of mixed data distributions. We demonstrate experimentally that REQ outperforms several strong baselines on robotic manipulation tasks for which suboptimal experts are available. We show how suboptimal experts can be constructed effectively by composing simple waypoint tracking controllers, and we also show how learned primitives can be combined with waypoint controllers to obtain reference behaviors to bootstrap a complex manipulation task on a simulated bimanual robot with human-like hands. Finally, we show that REQ is also effective for general off-policy RL, offline RL, and RL from demonstrations. 

#### Video 

#### Reviews

#### Rebuttal

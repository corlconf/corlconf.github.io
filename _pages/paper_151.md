---
layout: page
title: "Model-based Reinforcement Learning for Decentralized Multiagent Rendezvous"
subtitle: 
description:
permalink: /paper_151/
grand_parent: All Papers
parent: Wednesday
supp: 
code: 
youtubeId: 
---

# Model-based Reinforcement Learning for Decentralized Multiagent Rendezvous

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1JWAYVIM2dCpVi6TkcSG_vFIGJr9A35p0/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Rose Wang (MIT)*; J. Chase Kew (Google Brain); Dennis Lee (Google Inc.); Tsang-Wei Lee (Google Brain); Tingnan Zhang (Google); Brian Ichter (Google Brain); Jie Tan (Google); Aleksandra Faust (Google Brain)**

#### Abstract
Collaboration requires agents to align their goals on the fly. Underlying the human ability to align goals with other agents is their ability to predict the intentions of others and actively update their own plans. We propose hierarchical predictive planning (HPP), a model-based reinforcement learning method for decentralized multiagent rendezvous. Starting with pretrained, single-agent point to point navigation policies  and using noisy, high-dimensional sensor inputs like lidar, we first learn via self-supervision motion predictions of all agents on the team. Next, HPP uses the prediction models to propose and evaluate navigation subgoals for completing the rendezvous task without explicit communication among agents. We evaluate HPP in a suite of unseen environments, with increasing complexity and numbers of obstacles. We show that HPP outperforms alternative reinforcement learning, path planning, and heuristic-based baselines on challenging, unseen environments. Experiments in the real world demonstrate successful transfer of the prediction models from sim to real world without any additional fine-tuning. Altogether, HPP removes the need for a centralized operator in multiagent systems by combining model-based RL and inference methods, enabling agents to dynamically align plans.

#### Video 

#### Reviews

#### Rebuttal

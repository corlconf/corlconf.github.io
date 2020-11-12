---
layout: page
title: "Learning a Decentralized Multi-Arm Motion Planner"
subtitle: 
description:
permalink: /paper_30/
grand_parent: All Papers
parent: Wednesday
supp: 
code: https://github.com/columbia-robovision/decentralized-multiarm
youtubeId: 
---

# Learning a Decentralized Multi-Arm Motion Planner

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1duaJ_QNvyeM5-nUI6eFaNdLwpem2-qDC/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Huy Ha (Columbia University); Jingxi Xu (Columbia University); Shuran Song (Columbia University)***

#### Abstract
We present a closed-loop multi-arm motion planner that is scalable and flexible with team size. Traditional multi-arm robotic systems have relied on centralized motion planners, whose run times often scale exponentially with team size, and thus, fail to handle dynamic environments with open-loop control. In this paper, we tackle this problem with multi-agent reinforcement learning, where a shared policy network is trained to control each individual robot arm to reach its target end-effector pose given observations of its workspace state and target end-effector pose. The policy is trained using Soft Actor-Critic with expert demonstrations from a sampling-based motion planning algorithm (i.e., BiRRT). By leveraging classical planning algorithms, we can improve the learning efficiency of the reinforcement learning algorithm while retaining the fast inference time of neural networks. The resulting policy scales sub-linearly and can be deployed on multi-arm systems with variable team sizes. Thanks to the closed-loop and decentralized formulation, our approach generalizes to 5-10 multiarm systems and dynamic moving targets (>90% success rate for a 10-arm system), despite being trained on only 1-4 arm planning tasks with static targets.

#### Video 

#### Reviews

#### Rebuttal

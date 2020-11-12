---
layout: page
title: "Learning a Decision Module by Imitating Driver’s Control Behaviors"
subtitle: 
description:
permalink: /paper_4/
grand_parent: All Papers
parent: Monday
supp: https://drive.google.com/file/d/1RlgMCv_ZFLORLHuTJ49OGPLNE5d3Lkxi/view
code: 
youtubeId: 
---

# Learning a Decision Module by Imitating Driver’s Control Behaviors

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1KjsTtEKp5Sb80XtsgISc3C2s955Zwljd/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Junning Huang (SenseTime Research); Sirui Xie (UCLA); Jiankai Sun (CUHK)*; Qiurui Ma (Hong Kong University of Science and Technology); Chunxiao Liu (SenseTime Research); Dahua Lin (The Chinese University of Hong Kong); Bolei Zhou (CUHK)**

#### Abstract
Autonomous driving systems have a pipeline of perception, decision, planning, and control. The decision module processes information from the perception module and directs the execution of downstream planning and control modules. On the other hand, the recent success of deep learning suggests that this pipeline could be replaced by end-to-end neural control policies, however, safety cannot be well guaranteed for the data-driven neural networks. In this work, we propose a hybrid framework to learn neural decisions in the classical modular pipeline through end-to-end imitation learning.  This hybrid framework can preserve the merits of the classical pipeline such as the strict enforcement of physical and logical constraints while learning complex driving decisions from data. To circumvent the ambiguous annotation of human driving decisions, our method learns high-level driving decisions by imitating low-level control behaviors. We show in the simulation experiments that our modular driving agent can generalize its driving decision and control to various complex scenarios where the rule-based programs fail. It can also generate smoother and safer driving trajectories than end-to-end neural policies. Demo and code are available at <a href="https://decisionforce.github.io/modulardecision/" target="_blank">https://decisionforce.github.io/modulardecision/</a>.

#### Video 

#### Reviews

#### Rebuttal

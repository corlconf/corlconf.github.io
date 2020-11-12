---
layout: page
title: "Never Stop Learning: The Effectiveness of Fine-Tuning in Robotic Reinforcement Learning"
subtitle: 
description:
permalink: /paper_467/
grand_parent: All Papers
parent: Wednesday
supp: 
code: 
youtubeId: 
---

# Never Stop Learning: The Effectiveness of Fine-Tuning in Robotic Reinforcement Learning

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1rNYN2i-yDc0skeUjafvAv2OIYPnSvgWC/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Ryan Julian (University of Southern California)*; Benjamin Swanson (Google); Gaurav Sukhatme (University of Southern California); Sergey Levine (Google); Chelsea Finn (Google Brain); Karol Hausman (Google Brain)**

#### Interactive Session
*2020-11-18, 11:50 - 12:20 PST*

#### Abstract
One of the great promises of robot learning systems is that they will be able to learn from their mistakes and continuously adapt to ever-changing environments. Despite this potential, most of the robot learning systems today produce static policies that are not further adapted during deployment, because the algorithms which produce those policies are not designed for continual adaptation. We present an adaptation method, and empirical evidence that it supports a robot learning framework for continual adaption. We show that this very simple method–fine-tuning off-policy reinforcement learning using offline datasets–is robust to changes in background, object shape and appearance, lighting conditions, and robot morphology. We demonstrate how to adapt vision-based robotic manipulation policies to new variations using less than 0.2% of the data necessary to learn the task from scratch. Furthermore, we demonstrate that this robustness holds in an episodic continual learning setting. We also show that pre-training via RL is essential: training from scratch or adapting from super vised ImageNet features are both unsuccessful with such small amounts of data. Our empirical conclusions are consistently supported by experiments on simulated manipulation tasks, and by 60 unique fine-tuning experiments on a real robotic grasping system pre-trained on 580,000 grasps. For video results and an overview of the methods and experiments in this study, see the project website at <a href="https://ryanjulian.me/continual-fine-tuning" target="_blank">https://ryanjulian.me/continual-fine-tuning</a>.

#### Video 

#### Reviews

#### Rebuttal

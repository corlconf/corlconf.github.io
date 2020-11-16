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
youtube_id: HLJG_lPT4y0
pdf: https://drive.google.com/file/d/1rNYN2i-yDc0skeUjafvAv2OIYPnSvgWC/view
---

# Never Stop Learning: The Effectiveness of Fine-Tuning in Robotic Reinforcement Learning

<a href="https://drive.google.com/file/d/1rNYN2i-yDc0skeUjafvAv2OIYPnSvgWC/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Ryan Julian (University of Southern California)*; Benjamin Swanson (Google); Gaurav Sukhatme (University of Southern California); Sergey Levine (Google); Chelsea Finn (Google Brain); Karol Hausman (Google Brain)**

#### Interactive Session
<a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SES9UMIWLGRPWPIO0" target="_blank" rel="noopener noreferrer"><em>2020-11-18, 11:50 - 12:20 PST </em></a>

#### Abstract
One of the great promises of robot learning systems is that they will be able to learn from their mistakes and continuously adapt to ever-changing environments. Despite this potential, most of the robot learning systems today produce static policies that are not further adapted during deployment, because the algorithms which produce those policies are not designed for continual adaptation. We present an adaptation method, and empirical evidence that it supports a robot learning framework for continual adaption. We show that this very simple method–fine-tuning off-policy reinforcement learning using offline datasets–is robust to changes in background, object shape and appearance, lighting conditions, and robot morphology. We demonstrate how to adapt vision-based robotic manipulation policies to new variations using less than 0.2% of the data necessary to learn the task from scratch. Furthermore, we demonstrate that this robustness holds in an episodic continual learning setting. We also show that pre-training via RL is essential: training from scratch or adapting from super vised ImageNet features are both unsuccessful with such small amounts of data. Our empirical conclusions are consistently supported by experiments on simulated manipulation tasks, and by 60 unique fine-tuning experiments on a real robotic grasping system pre-trained on 580,000 grasps. For video results and an overview of the methods and experiments in this study, see the project website at <a href="https://ryanjulian.me/continual-fine-tuning" target="_blank">https://ryanjulian.me/continual-fine-tuning</a>.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1HtVmqp_Dr0SIrxc_IRjn4I79lf8_uQv8/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


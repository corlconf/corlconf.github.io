---
layout: page
title: "Iterative Semi-parametric Dynamics Model Learning For Autonomous Racing"
subtitle: 
description:
permalink: /paper_112/
grand_parent: All Papers
parent: Tuesday
supp: 
code: 
youtubeId: 
---

# Iterative Semi-parametric Dynamics Model Learning For Autonomous Racing

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1hllOW2euu7p7vgkXUa6OTWjwgfP1BPLl/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Ignat Georgiev (The University of Edinburgh)*; Christoforos Chatzikomis (Arrival); Timo Voelkl (Arrival); Joshua Smith (The University of Edinburgh); Michael Mistry (U of Edinburgh)**

#### Abstract
Accurately modeling robot dynamics is crucial to safe and efficient motion control. In this paper, we develop and apply an iterative learning semi-parametric model, with a neural network, to the task of autonomous racing with a Model Predictive  Controller (MPC). We present a novel non-linear semi-parametric dynamics model where we represent the known dynamics with a parametric model, and a neural network captures the unknown dynamics. We show that our model can learn more accurately than a purely parametric model and generalize better than a purely non-parametric model, making it ideal for real-world applications where collecting data from the full state space is not feasible. We present a system where the model is bootstrapped on pre-recorded data and then updated iteratively at run time. Then we apply our iterative learning approach to the simulated problem of autonomous racing and show that it can safely adapt to modified dynamics online and even achieve better performance than models trained on data from manual driving.

#### Video 

#### Reviews

#### Rebuttal

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
youtube_id: O7DwTkDrxs8
pdf: https://drive.google.com/file/d/1hllOW2euu7p7vgkXUa6OTWjwgfP1BPLl/view
---

# Iterative Semi-parametric Dynamics Model Learning For Autonomous Racing

<a href="https://drive.google.com/file/d/1hllOW2euu7p7vgkXUa6OTWjwgfP1BPLl/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Ignat Georgiev (The University of Edinburgh)*; Christoforos Chatzikomis (Arrival); Timo Voelkl (Arrival); Joshua Smith (The University of Edinburgh); Michael Mistry (U of Edinburgh)**

#### Interactive Session
*2020-11-17, 11:50 - 12:20 PST* 

#### Abstract
Accurately modeling robot dynamics is crucial to safe and efficient motion control. In this paper, we develop and apply an iterative learning semi-parametric model, with a neural network, to the task of autonomous racing with a Model Predictive  Controller (MPC). We present a novel non-linear semi-parametric dynamics model where we represent the known dynamics with a parametric model, and a neural network captures the unknown dynamics. We show that our model can learn more accurately than a purely parametric model and generalize better than a purely non-parametric model, making it ideal for real-world applications where collecting data from the full state space is not feasible. We present a system where the model is bootstrapped on pre-recorded data and then updated iteratively at run time. Then we apply our iterative learning approach to the simulated problem of autonomous racing and show that it can safely adapt to modified dynamics online and even achieve better performance than models trained on data from manual driving.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1tZEHOq8JqNEWv02FlFpWakWuNYJdaT8u/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


---
layout: page
title: "Learning Certified Control Using Contraction Metric"
subtitle: 
description:
permalink: /paper_347/
grand_parent: All Papers
parent: Tuesday
supp: 
code: https://github.com/sundw2014/C3M
youtubeId: 
---

# Learning Certified Control Using Contraction Metric

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1ZBZsdjKi6fJNjj5aBy5VzDndZ5jd2LjL/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Dawei Sun (University of Illinois Urbana-Champaign)*; Susmit Jha (SRI International); Chuchu Fan (MIT)**

#### Abstract
In this paper, we solve the problem of finding a certified control policy that drives a robot from any given initial state and under any bounded disturbance to the desired reference trajectory, with guarantees on the convergence or bounds on the tracking error. Such a controller is crucial in safe motion planning. We leverage the advanced theory in Control Contraction Metric and design a learning framework based on neural networks to co-synthesize the contraction metric and the controller for control-affine systems. We further provide methods to validate the convergence and bounded error guarantees. We demonstrate the performance of our method using a suite of challenging robotic models, including models with learned dynamics as neural networks. We compare our approach with leading methods using sum-of-squares programming, reinforcement learning, and model predictive control. Results show that our methods indeed can handle a broader class of systems with less tracking error and faster execution speed. Code is available at <a href="https://github.com/sundw2014/C3M" target="_blank">https://github.com/sundw2014/C3M</a>.

#### Video 

#### Reviews

#### Rebuttal

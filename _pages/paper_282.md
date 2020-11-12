---
layout: page
title: "Stein Variational Model Predictive Control"
subtitle: 
description:
permalink: /paper_282/
grand_parent: All Papers
parent: Monday
supp: 
code: 
youtubeId: 
---

# Stein Variational Model Predictive Control

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1QSJQUmOZoDgvdq8l-AlMiS7gFYRi_9Jx/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Alexander Lambert (Georgia Institute of Technology)*; Fabio Ramos (NVIDIA, The University of Sydney); Byron Boots (University of Washington); Dieter Fox (NVIDIA); Adam Fishman (University of Washington)**

#### Abstract
Decision making under uncertainty is critical to real-world, autonomous systems. Model Predictive Control (MPC) methods have demonstrated favorable performance in practice, but remain limited when dealing with complex probability distributions. In this paper, we propose a generalization of MPC that represents a multitude of solutions as posterior distributions. By casting MPC as a Bayesian inference problem, we employ variational methods for posterior computation, naturally encoding the complexity and multi-modality of the decision making problem. We propose a Stein variational gradient descent method to estimate the posterior over control parameters, given a cost function and a sequence of state observations. We show that this framework leads to successful planning in challenging, non-convex optimal control problems.

#### Video 

#### Reviews

#### Rebuttal

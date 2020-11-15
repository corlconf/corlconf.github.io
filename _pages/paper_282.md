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
youtube_id: 
pdf: https://drive.google.com/file/d/1QSJQUmOZoDgvdq8l-AlMiS7gFYRi_9Jx/view
---

# Stein Variational Model Predictive Control

<a href="https://drive.google.com/file/d/1QSJQUmOZoDgvdq8l-AlMiS7gFYRi_9Jx/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Alexander Lambert (Georgia Institute of Technology)*; Fabio Ramos (NVIDIA, The University of Sydney); Byron Boots (University of Washington); Dieter Fox (NVIDIA); Adam Fishman (University of Washington)**

#### Interactive Session
*2020-11-16, 11:10 - 11:40 PST* 

#### Abstract
Decision making under uncertainty is critical to real-world, autonomous systems. Model Predictive Control (MPC) methods have demonstrated favorable performance in practice, but remain limited when dealing with complex probability distributions. In this paper, we propose a generalization of MPC that represents a multitude of solutions as posterior distributions. By casting MPC as a Bayesian inference problem, we employ variational methods for posterior computation, naturally encoding the complexity and multi-modality of the decision making problem. We propose a Stein variational gradient descent method to estimate the posterior over control parameters, given a cost function and a sequence of state observations. We show that this framework leads to successful planning in challenging, non-convex optimal control problems.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1KtDg0VNKUgP71bxB_M1Lgsz2TkwaG8Uf/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


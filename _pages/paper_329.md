---
layout: page
title: "Generative adversarial training of product of policies for robust and adaptive movement primitives"
subtitle: 
description:
permalink: /paper_329/
grand_parent: All Papers
parent: Monday
supp: 
code: https://github.com/emmanuelpignat/tf_robot_learning
youtubeId: 
pdf: https://drive.google.com/file/d/1gGAAlGw9akNdZioCWQBYWBHCa3sm3kVe/view
---

# Generative adversarial training of product of policies for robust and adaptive movement primitives

<a href="https://drive.google.com/file/d/1gGAAlGw9akNdZioCWQBYWBHCa3sm3kVe/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="https://github.com/emmanuelpignat/tf_robot_learning" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Emmanuel Pignat (Idiap Research Institute and EPFL)*; Hakan Girgin (Idiap Research Institute); Sylvain Calinon (Idiap Research Institute)**

#### Interactive Session
*2020-11-16, 11:10 - 11:40 PST*

#### Abstract
In learning from demonstrations, many generative models of trajectories make simplifying assumptions of independence. Correctness is sacrificed in the name of tractability and speed of the learning phase. 
    The ignored dependencies, which are often the kinematic and dynamic constraints of the system, are then only restored when synthesizing the motion, which introduces possibly heavy distortions. 
    In this work, we propose to use those approximate trajectory distributions as close-to-optimal discriminators in the popular generative adversarial framework to stabilize and accelerate the learning procedure. 
    The two problems of adaptability and robustness are addressed with our method. 
    In order to adapt the motions to varying contexts, we propose to use a product of Gaussian policies defined in several parametrized task spaces. Robustness to perturbations and varying dynamics is ensured with the use of stochastic gradient descent and ensemble methods to learn the stochastic dynamics. Two experiments are performed on a 7-DoF manipulator to validate the approach.

#### Video 

#### Reviews

#### Rebuttal


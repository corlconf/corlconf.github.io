---
layout: page
title: "STReSSD: Sim-To-Real from Sound for Stochastic Dynamics"
subtitle: 
description:
permalink: /paper_202/
grand_parent: All Papers
parent: Tuesday
supp: 
code: 
youtubeId: 
---

# STReSSD: Sim-To-Real from Sound for Stochastic Dynamics

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1x6cVUOfkqUoog38hckBgMMPEERB3UuwV/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Carolyn Matl (University of California, Berkeley)*; Yashraj Narang (NVIDIA); Dieter Fox (NVIDIA); Ruzena Bajcsy (UC Berkeley); Fabio Ramos (NVIDIA, The University of Sydney)**

#### Interactive Session
*2020-11-17, 11:50 - 12:20 PST*

#### Abstract
Sound is an information-rich medium that captures dynamic physical events. This work presents STReSSD, a framework that uses sound to bridge the simulation-to-reality gap for stochastic dynamics, demonstrated for the canonical case of a bouncing ball. A physically-motivated noise model is presented to capture stochastic behavior of the balls upon collision with the environment. A likelihood-free Bayesian inference framework is used to infer the parameters of the noise model, as well as a material property called the coefficient of restitution, from audio observations.  The same inference framework and the calibrated stochastic simulator are then used to learn a probabilistic model of ball dynamics.  The predictive capabilities of the dynamics model are tested in two robotic experiments. First, open-loop predictions anticipate probabilistic success of bouncing a ball into a cup. The second experiment integrates audio perception with a robotic arm to track and deflect a bouncing ball in real-time. We envision that this work is a step towards integrating audio-based inference for dynamic robotic tasks.  

#### Video 

#### Reviews

#### Rebuttal

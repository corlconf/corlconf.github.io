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
youtube_id: 
pdf: https://drive.google.com/file/d/1x6cVUOfkqUoog38hckBgMMPEERB3UuwV/view
---

# STReSSD: Sim-To-Real from Sound for Stochastic Dynamics

<a href="https://drive.google.com/file/d/1x6cVUOfkqUoog38hckBgMMPEERB3UuwV/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Carolyn Matl (University of California, Berkeley)*; Yashraj Narang (NVIDIA); Dieter Fox (NVIDIA); Ruzena Bajcsy (UC Berkeley); Fabio Ramos (NVIDIA, The University of Sydney)**

#### Interactive Session
<em>2020-11-17, 11:50 - 12:20 PST </em> | <a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SESJNX5YB4XFHGRDQ" target="_blank" rel="noopener noreferrer"> PheedLoop Session <i class="fa fa-external-link" aria-hidden="true"></i> </a> 

#### Abstract
Sound is an information-rich medium that captures dynamic physical events. This work presents STReSSD, a framework that uses sound to bridge the simulation-to-reality gap for stochastic dynamics, demonstrated for the canonical case of a bouncing ball. A physically-motivated noise model is presented to capture stochastic behavior of the balls upon collision with the environment. A likelihood-free Bayesian inference framework is used to infer the parameters of the noise model, as well as a material property called the coefficient of restitution, from audio observations.  The same inference framework and the calibrated stochastic simulator are then used to learn a probabilistic model of ball dynamics.  The predictive capabilities of the dynamics model are tested in two robotic experiments. First, open-loop predictions anticipate probabilistic success of bouncing a ball into a cup. The second experiment integrates audio perception with a robotic arm to track and deflect a bouncing ball in real-time. We envision that this work is a step towards integrating audio-based inference for dynamic robotic tasks.  

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1onVinD6S7FToue7cZRH0vkXqRSJLB2SG/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


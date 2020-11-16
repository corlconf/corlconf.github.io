---
layout: page
title: "Sim2Real Transfer for Deep Reinforcement Learning with Stochastic State Transition Delays"
subtitle: 
description:
permalink: /paper_219/
grand_parent: All Papers
parent: Monday
supp: 
code: https://github.com/nesl/Time-in-State-RL
youtube_id: rUTs2T_3A5Q
pdf: https://drive.google.com/file/d/1ysPMP6AHp6s0Dj9FB5AE9UsHmSg41zBo/view
---

# Sim2Real Transfer for Deep Reinforcement Learning with Stochastic State Transition Delays

<a href="https://drive.google.com/file/d/1ysPMP6AHp6s0Dj9FB5AE9UsHmSg41zBo/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="https://github.com/nesl/Time-in-State-RL" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Sandeep Singh Sandha (UCLA)*; Luis Garcia (USC Information Sciences Institute); Bharathan Balaji (Amazon); Fatima Anwar (University of Massachusetts, Amherst); Mani Srivastava (UC Los Angeles)**

#### Interactive Session
*2020-11-16, 11:50 - 12:20 PST* 

#### Abstract
Deep Reinforcement Learning (RL) has demonstrated to be useful for a wide variety of robotics applications. To address sample efficiency and safety during training, it is common to train Deep RL policies in a simulator and then deploy to the real world, a process called Sim2Real transfer.  For robotics applications, the deployment heterogeneities and runtime compute stochasticity results in variable timing characteristics of sensor sampling rates and end-to-end delays from sensing to actuation. Prior works have used the technique of domain randomization to enable the successful transfer of policies across domains having different state transition delays. We show that variation in sampling rates and policy execution time leads to degradation in Deep RL policy performance, and that domain randomization is insufficient to overcome this limitation. We propose the Time-in-State RL (TSRL) approach, which includes delays and sampling rate as additional agent observations at training time to improve the robustness of Deep RL policies. We demonstrate the efficacy of TSRL on HalfCheetah, Ant, and car robot in simulation and on a real robot using a 1/18th scale car.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/10RrlqunA8KU5kr85gNJeFkVrz_ouqa2a/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


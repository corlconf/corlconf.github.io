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
youtubeId: 
---

# Sim2Real Transfer for Deep Reinforcement Learning with Stochastic State Transition Delays

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1ysPMP6AHp6s0Dj9FB5AE9UsHmSg41zBo/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Sandeep Singh Sandha (UCLA)*; Luis Garcia (USC Information Sciences Institute); Bharathan Balaji (Amazon); Fatima Anwar (University of Massachusetts, Amherst); Mani Srivastava (UC Los Angeles)**

#### Interactive Session
*2020-11-16, 11:50 - 12:20 PST*

#### Abstract
Deep Reinforcement Learning (RL) has demonstrated to be useful for a wide variety of robotics applications. To address sample efficiency and safety during training, it is common to train Deep RL policies in a simulator and then deploy to the real world, a process called Sim2Real transfer.  For robotics applications, the deployment heterogeneities and runtime compute stochasticity results in variable timing characteristics of sensor sampling rates and end-to-end delays from sensing to actuation. Prior works have used the technique of domain randomization to enable the successful transfer of policies across domains having different state transition delays. We show that variation in sampling rates and policy execution time leads to degradation in Deep RL policy performance, and that domain randomization is insufficient to overcome this limitation. We propose the Time-in-State RL (TSRL) approach, which includes delays and sampling rate as additional agent observations at training time to improve the robustness of Deep RL policies. We demonstrate the efficacy of TSRL on HalfCheetah, Ant, and car robot in simulation and on a real robot using a 1/18th scale car.

#### Video 

#### Reviews

#### Rebuttal

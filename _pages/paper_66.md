---
layout: page
title: "Reinforcement Learning with Videos: Combining Offline Observations with Interaction"
subtitle: 
description:
permalink: /paper_66/
grand_parent: All Papers
parent: Wednesday
supp: 
code: 
youtubeId: 
---

# Reinforcement Learning with Videos: Combining Offline Observations with Interaction

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1V7e1DkjLILO3tvx0mnK0dYr3snJS_7S5/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Karl  Schmeckpeper (University of Pennsylvania)*; Oleh Rybkin (University of Pennsylvania); Kostas Daniilidis (University of Pennsylvania); Sergey Levine (UC Berkeley); Chelsea Finn (Stanford)**

#### Interactive Session
*2020-11-18, 11:10 - 11:40 PST*

#### Abstract
 Reinforcement learning is a powerful framework for robots to acquire skills from experience, but often requires a substantial amount of online data collection. As a result, it is difficult to collect sufficiently diverse experiences that are needed for robots to generalize broadly. Videos of humans, on the other hand, are a readily available source of broad and interesting experiences. In this paper, we consider the question: can we perform reinforcement learning directly on experience collected by humans? This problem is particularly difficult, as such videos are not annotated with actions and exhibit substantial visual domain shift relative to the robot's embodiment. To address these challenges, we propose a framework for reinforcement learning with videos (RLV).
RLV learns a policy and value function using experience collected by humans in combination with data collected by robots. In our experiments, we find that RLV is able to leverage such videos to learn challenging vision-based skills with less than half as many samples as RL methods that learn from scratch.

#### Video 

#### Reviews

#### Rebuttal

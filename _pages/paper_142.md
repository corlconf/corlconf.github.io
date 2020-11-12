---
layout: page
title: "Sim-to-Real Transfer for Vision-and-Language Navigation"
subtitle: 
description:
permalink: /paper_142/
grand_parent: All Papers
parent: Wednesday
supp: https://drive.google.com/file/d/1tiRGrTKGi_t5jGkHbnQ5wVjucp35HsTT/view
code: https://github.com/batra-mlp-lab/vln-sim2real
youtubeId: 
---

# Sim-to-Real Transfer for Vision-and-Language Navigation

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1WsJtHv9ysWWwXSS3JR8rbv8WhDC8R9Ml/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Peter Anderson (Google)*; Ayush Shrivastava (Georgia Institute of Technology); Joanne Truong (Georgia Institute of Technology); Arjun Majumdar (Georgia Tech); Devi Parikh (Georgia Tech & Facebook AI Research); Dhruv Batra (Georgia Tech & Facebook AI Research); Stefan Lee (Oregon State University)**

#### Abstract
We study the challenging problem of releasing a robot in a previously unseen environment, and having it follow unconstrained natural language navigation instructions. Recent work on the task of Vision-and-Language Navigation (VLN) has achieved significant progress in simulation. To assess the implications of this work for robotics, we transfer a VLN agent trained in simulation to a physical robot. To bridge the gap between the high-level discrete action space learned by the VLN agent, and the robot’s low-level continuous action space, we propose a subgoal model to identify nearby waypoints, and use domain randomization to mitigate visual domain differences. For accurate sim and real comparisons in parallel environments, we annotate a 325m2 office space with 1.3km of navigation instructions, and create a digitized replica in simulation. We find that sim-to-real transfer to an environment not seen in training is successful if an occupancy map and navigation graph can be collected and annotated in advance (success rate of 46.8% vs. 55.9% in sim), but much more challenging in the hardest setting with no prior mapping at all (success rate of 22.5%).

#### Video 

#### Reviews

#### Rebuttal

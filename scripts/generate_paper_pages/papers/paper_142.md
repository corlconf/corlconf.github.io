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
youtube_id: THfTK7_xLX8
pdf: https://drive.google.com/file/d/1WsJtHv9ysWWwXSS3JR8rbv8WhDC8R9Ml/view
---

# Sim-to-Real Transfer for Vision-and-Language Navigation

<a href="https://drive.google.com/file/d/1WsJtHv9ysWWwXSS3JR8rbv8WhDC8R9Ml/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="https://drive.google.com/file/d/1tiRGrTKGi_t5jGkHbnQ5wVjucp35HsTT/view" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="https://github.com/batra-mlp-lab/vln-sim2real" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Peter Anderson (Google)*; Ayush Shrivastava (Georgia Institute of Technology); Joanne Truong (Georgia Institute of Technology); Arjun Majumdar (Georgia Tech); Devi Parikh (Georgia Tech & Facebook AI Research); Dhruv Batra (Georgia Tech & Facebook AI Research); Stefan Lee (Oregon State University)**

#### Interactive Session
<em>2020-11-18, 11:10 - 11:40 PST </em> | <a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SESHMUTQ377QUM8CV" target="_blank" rel="noopener noreferrer"> PheedLoop Session <i class="fa fa-external-link" aria-hidden="true"></i> </a> 

#### Abstract
We study the challenging problem of releasing a robot in a previously unseen environment, and having it follow unconstrained natural language navigation instructions. Recent work on the task of Vision-and-Language Navigation (VLN) has achieved significant progress in simulation. To assess the implications of this work for robotics, we transfer a VLN agent trained in simulation to a physical robot. To bridge the gap between the high-level discrete action space learned by the VLN agent, and the robot’s low-level continuous action space, we propose a subgoal model to identify nearby waypoints, and use domain randomization to mitigate visual domain differences. For accurate sim and real comparisons in parallel environments, we annotate a 325m2 office space with 1.3km of navigation instructions, and create a digitized replica in simulation. We find that sim-to-real transfer to an environment not seen in training is successful if an occupancy map and navigation graph can be collected and annotated in advance (success rate of 46.8% vs. 55.9% in sim), but much more challenging in the hardest setting with no prior mapping at all (success rate of 22.5%).

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1KkTE9wmniHJvOjeURFFI6C2hrzXNJ3zT/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


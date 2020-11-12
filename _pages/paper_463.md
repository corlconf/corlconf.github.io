---
layout: page
title: "Transformers for One-Shot Visual Imitation"
subtitle: 
description:
permalink: /paper_463/
grand_parent: All Papers
parent: Wednesday
supp: 
code: https://github.com/SudeepDasari/one_shot_transformers
youtubeId: 
---

# Transformers for One-Shot Visual Imitation

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1I_n6c8Zh55POTxXHA9779sT1Ey2ZQ1WO/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Sudeep Dasari (Carnegie Mellon University)*; Abhinav Gupta (CMU/FAIR)**

#### Interactive Session
*2020-11-18, 11:10 - 11:40 PST*

#### Abstract
Humans are able to seamlessly visually imitate others, by inferring their intentions and using past experience to achieve the same end goal. In other words, we can parse complex semantic knowledge from raw video and efficiently translate that into concrete motor control. Is it possible to give a robot this same capability? Prior research in robot imitation learning has created agents which can acquire diverse skills from expert human operators. However, expanding these techniques to work with a single positive example during test time is still an open challenge. Apart from control, the difficulty stems from mismatches between the demonstrator and robot domains. For example, objects may be placed in different locations (e.g. kitchen layouts are different in every house). Additionally, the demonstration may come from an agent with different morphology and physical appearance (e.g. human), so one-to-one action correspondences are not available. This paper investigates techniques which allow robots to partially bridge these domain gaps, using their past experience. A neural network is trained to mimic ground truth robot actions given context video from another agent, and must generalize to unseen task instances when prompted with new videos during test time. We hypothesize that our policy representations must be both context driven and dynamics aware in order to perform these tasks. These assumptions are baked into the neural network using the Transformers attention mechanism and a self-supervised inverse dynamics loss. Finally, we experimentally determine that our method accomplishes a 2x improvement in terms of task success rate over prior baselines in a suite of one-shot manipulation tasks.

#### Video 

#### Reviews

#### Rebuttal

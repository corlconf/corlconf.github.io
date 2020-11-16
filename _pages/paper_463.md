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
youtube_id: LuamElhrunI
pdf: https://drive.google.com/file/d/1I_n6c8Zh55POTxXHA9779sT1Ey2ZQ1WO/view
---

# Transformers for One-Shot Visual Imitation

<a href="https://drive.google.com/file/d/1I_n6c8Zh55POTxXHA9779sT1Ey2ZQ1WO/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="https://github.com/SudeepDasari/one_shot_transformers" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Sudeep Dasari (Carnegie Mellon University)*; Abhinav Gupta (CMU/FAIR)**

#### Interactive Session
<a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SESEIVKJ0UA34MMZO" target="_blank" rel="noopener noreferrer"><em>2020-11-18, 11:10 - 11:40 PST </em></a>

#### Abstract
Humans are able to seamlessly visually imitate others, by inferring their intentions and using past experience to achieve the same end goal. In other words, we can parse complex semantic knowledge from raw video and efficiently translate that into concrete motor control. Is it possible to give a robot this same capability? Prior research in robot imitation learning has created agents which can acquire diverse skills from expert human operators. However, expanding these techniques to work with a single positive example during test time is still an open challenge. Apart from control, the difficulty stems from mismatches between the demonstrator and robot domains. For example, objects may be placed in different locations (e.g. kitchen layouts are different in every house). Additionally, the demonstration may come from an agent with different morphology and physical appearance (e.g. human), so one-to-one action correspondences are not available. This paper investigates techniques which allow robots to partially bridge these domain gaps, using their past experience. A neural network is trained to mimic ground truth robot actions given context video from another agent, and must generalize to unseen task instances when prompted with new videos during test time. We hypothesize that our policy representations must be both context driven and dynamics aware in order to perform these tasks. These assumptions are baked into the neural network using the Transformers attention mechanism and a self-supervised inverse dynamics loss. Finally, we experimentally determine that our method accomplishes a 2x improvement in terms of task success rate over prior baselines in a suite of one-shot manipulation tasks.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1hRFAUlbhn-roQfqLo4lZZjFLoS-iHTE3/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


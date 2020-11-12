---
layout: page
title: "Attention-Privileged Reinforcement Learning"
subtitle: 
description:
permalink: /paper_84/
grand_parent: All Papers
parent: Tuesday
supp: 
code: 
youtubeId: 
---

# Attention-Privileged Reinforcement Learning

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/13P_hvsDw4bUN-re2upKc4RpT1f9y2Bb5/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Sasha Salter (University of Oxford)*; Dushyant Rao (DeepMind); Markus Wulfmeier (DeepMind); Raia Hadsell (Deepmind); Ingmar Posner (Oxford University)**

#### Interactive Session
*2020-11-17, 11:10 - 11:40 PST*

#### Abstract
Image-based Reinforcement Learning is known to suffer from poor sample efficiency and generalisation to unseen visuals such as distractors (task-independent aspects of the observation space). Visual domain randomisation encourages transfer by training over visual factors of variation that may be encountered in the target domain. This increases learning complexity, can negatively impact learning rate and performance, and requires knowledge of potential variations during deployment. In this paper, we introduce Attention-Privileged Reinforcement Learning (APRiL) which uses a self-supervised attention mechanism to significantly alleviate these drawbacks: by focusing on task-relevant aspects of the observations, attention provides robustness to distractors as well as significantly increased learning efficiency. APRiL trains two attention-augmented actor-critic agents: one purely based on image observations, available across training and transfer domains; and one with access to privileged information (such as environment states) available only during training. Experience is shared between both agents and their attention mechanisms are aligned. The image-based policy can then be deployed without access to privileged information. We experimentally demonstrate accelerated and more robust learning on a diverse set of domains, leading to improved final performance for environments both within and outside the training distribution.

#### Video 

#### Reviews

#### Rebuttal

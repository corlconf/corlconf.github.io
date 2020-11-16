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
youtube_id: KEq98nf-J6o
pdf: https://drive.google.com/file/d/13P_hvsDw4bUN-re2upKc4RpT1f9y2Bb5/view
---

# Attention-Privileged Reinforcement Learning

<a href="https://drive.google.com/file/d/13P_hvsDw4bUN-re2upKc4RpT1f9y2Bb5/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Sasha Salter (University of Oxford)*; Dushyant Rao (DeepMind); Markus Wulfmeier (DeepMind); Raia Hadsell (Deepmind); Ingmar Posner (Oxford University)**

#### Interactive Session
<a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SESI5P74VLPPHMZVD" target="_blank" rel="noopener noreferrer"><em>2020-11-17, 11:10 - 11:40 PST </em></a>

#### Abstract
Image-based Reinforcement Learning is known to suffer from poor sample efficiency and generalisation to unseen visuals such as distractors (task-independent aspects of the observation space). Visual domain randomisation encourages transfer by training over visual factors of variation that may be encountered in the target domain. This increases learning complexity, can negatively impact learning rate and performance, and requires knowledge of potential variations during deployment. In this paper, we introduce Attention-Privileged Reinforcement Learning (APRiL) which uses a self-supervised attention mechanism to significantly alleviate these drawbacks: by focusing on task-relevant aspects of the observations, attention provides robustness to distractors as well as significantly increased learning efficiency. APRiL trains two attention-augmented actor-critic agents: one purely based on image observations, available across training and transfer domains; and one with access to privileged information (such as environment states) available only during training. Experience is shared between both agents and their attention mechanisms are aligned. The image-based policy can then be deployed without access to privileged information. We experimentally demonstrate accelerated and more robust learning on a diverse set of domains, leading to improved final performance for environments both within and outside the training distribution.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1R5TZEryZGe5Szhfw8pnoSIsdbembzMHF/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


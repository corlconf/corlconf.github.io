---
layout: page
title: "Positive-Unlabeled Reward Learning"
subtitle: 
description:
permalink: /paper_45/
grand_parent: All Papers
parent: Tuesday
supp: 
code: 
youtube_id: eRVr5eyRCWc
pdf: https://drive.google.com/file/d/1RATFBOenj9A0gPCHq6z74u03l0WsS8Kg/view
---

# Positive-Unlabeled Reward Learning

<a href="https://drive.google.com/file/d/1RATFBOenj9A0gPCHq6z74u03l0WsS8Kg/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Danfei Xu (Stanford University)*; Misha Denil (DeepMind)**

#### Interactive Session
<em>2020-11-17, 11:50 - 12:20 PST </em> | <a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SESCPGKZJMRI55PZA" target="_blank" rel="noopener noreferrer"> PheedLoop Session <i class="fa fa-external-link" aria-hidden="true"></i> </a> 

#### Abstract
Learning reward functions from data is a promising path towards achieving scalable Reinforcement Learning (RL) for robotics. However, a major challenge in training agents from learned reward models is that the agent can learn to exploit errors in the reward model to achieve high reward behaviors that do not correspond to the intended task. These reward delusions can lead to unintended and even dangerous behaviors. On the other hand, adversarial imitation learning frameworks (Ho et al., 2016) tend to suffer the opposite problem, where the discriminator learns to trivially distinguish agent and expert behavior, resulting in reward models that produce low reward signal regardless of the input state.
In this paper, we connect these two classes of reward learning methods to positive-unlabeled (PU) learning, and show that by applying a large-scale PU learning algorithm to the reward learning problem, we can address both the reward under- and over-estimation problems simultaneously. Our approach drastically improves both GAIL and supervised reward learning, without any additional assumptions.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1LElWoA-BSIjZo8I2pwYkDRNECTl60q6p/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


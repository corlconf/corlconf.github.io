---
layout: page
title: "MELD: Meta-Reinforcement Learning from Images via Latent State Models"
subtitle: 
description:
permalink: /paper_278/
grand_parent: All Papers
parent: Wednesday
supp: 
code: https://github.com/tonyzhaozh/meld
youtube_id: 
pdf: https://drive.google.com/file/d/1ustZc_uOdYZ3cPrfZSSUh1cnyB7QYH2E/view
---

# MELD: Meta-Reinforcement Learning from Images via Latent State Models

<a href="https://drive.google.com/file/d/1ustZc_uOdYZ3cPrfZSSUh1cnyB7QYH2E/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="https://github.com/tonyzhaozh/meld" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Zihao Zhao (UC Berkeley); Anusha Nagabandi (UC Berkeley)*; Kate Rakelly (UC Berkeley); Chelsea Finn (Stanford); Sergey Levine (UC Berkeley)**

#### Interactive Session
*2020-11-18, 11:10 - 11:40 PST* 

#### Abstract
Meta-reinforcement learning algorithms can enable autonomous agents, such as robots, to quickly acquire new behaviors by leveraging prior experience in a set of related training tasks. However, the onerous data requirements of meta-training compounded with the challenge of learning from sensory inputs such as images have made meta-RL challenging to apply to real robotic systems. Latent state models, which learn compact state representations from a sequence of observations, can accelerate representation learning from visual inputs. In this paper, we leverage the perspective of meta-learning as task inference to show that latent state models can <em>also</em> perform meta-learning given an appropriately defined observation space. Building on this insight, we develop meta-RL with latent dynamics (MELD), an algorithm for meta-RL from images that performs inference in a latent state model to quickly acquire new skills given observations and rewards. MELD outperforms prior meta-RL methods on several simulated image-based robotic control problems, and enables a real WidowX robotic arm to insert an Ethernet cable into new locations given a sparse task completion signal after only 8 hours of real world meta-training. To our knowledge, MELD is the first meta-RL algorithm trained in a real-world robotic control setting from images.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/11sn_0nTbrnKIqnt9JVjMbsK_Ki_rt0Kf/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


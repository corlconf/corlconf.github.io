---
layout: page
title: "Learning Object-conditioned Exploration using Distributed Soft Actor Critic"
subtitle: 
description:
permalink: /paper_381/
grand_parent: All Papers
parent: Wednesday
supp: 
code: 
youtube_id: QE_YMBr6ff4
pdf: https://drive.google.com/file/d/1kzbhggKNEr6pk-i3Uzck4gWeAJNjL3hV/view
---

# Learning Object-conditioned Exploration using Distributed Soft Actor Critic

<a href="https://drive.google.com/file/d/1kzbhggKNEr6pk-i3Uzck4gWeAJNjL3hV/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Ayzaan Wahid (Google)*; Austin C Stone (Google); Kevin Chen (Stanford); Brian Ichter (Google Brain); Alexander Toshev (Google)**

#### Interactive Session
*2020-11-18, 11:10 - 11:40 PST* 

#### Abstract
Object navigation is defined as navigating to an object of a given label in a complex, unexplored environment. In its general form, this problem poses several challenges for Robotics: semantic exploration of unknown environments in search of an object and low-level control. In this work we study object-guided exploration and low-level control, and present an end-to-end trained navigation policy achieving a success rate of 0.68 and SPL of 0.58 on unseen, visually complex scans of real homes. We propose a highly scalable implementation of an off-policy Reinforcement Learning algorithm, distributed Soft Actor Critic, which allows the system to utilize 98M experience steps in 24 hours on 8 GPUs. Our system learns to control a differential drive mobile base in simulation from a stack of high dimensional observations commonly used on robotic platforms. The learned policy is capable of object-guided exploratory behaviors and low-level control learned from pure experiences in realistic environments.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1uZZOIRIbrOOdPFLjtKxTqU3sLxTkovGv/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


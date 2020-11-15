---
layout: page
title: "f-IRL: Inverse Reinforcement Learning via State Marginal Matching"
subtitle: 
description:
permalink: /paper_111/
grand_parent: All Papers
parent: Monday
supp: 
code: https://github.com/twni2016/f-IRL

youtube_id: nZcUnuyegJ4
pdf: https://drive.google.com/file/d/10q7HqAekk5GS7at1j-ngW88MeWOJuJ2V/view
---

# f-IRL: Inverse Reinforcement Learning via State Marginal Matching

<a href="https://drive.google.com/file/d/10q7HqAekk5GS7at1j-ngW88MeWOJuJ2V/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="https://github.com/twni2016/f-IRL
" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Tianwei Ni (Carnegie Mellon University); Harshit Sikchi (Carnegie Mellon University)*; Yufei Wang (Carnegie Mellon University); Tejus Gupta (Carnegie Mellon University); Lisa Lee (Carnegie Mellon University); Ben Eysenbach (Carnegie Mellon University)**

#### Interactive Session
*2020-11-16, 11:10 - 11:40 PST* 

#### Abstract
Imitation learning is well-suited for robotic tasks where it is difficult to directly program the behavior or specify a cost for optimal control. 
In this work, we propose a method for learning the reward function (and the corresponding policy) to match the expert state density. 
Our main result is the analytic gradient of any f-divergence between the agent and expert state distribution w.r.t. reward parameters. Based on the derived gradient, we present an algorithm, f-IRL, that recovers a stationary reward function from the expert density by gradient descent. 
We show that f-IRL can learn behaviors from a hand-designed target state density or implicitly through expert observations. 
Our method outperforms adversarial imitation learning methods in terms of sample efficiency and the required number of expert trajectories on IRL benchmarks. 
Moreover, we show that the recovered reward function can be used to quickly solve downstream tasks, and empirically demonstrate its utility on hard-to-explore tasks and for behavior transfer across changes in dynamics. 
Project videos and code link are available at <a href="https://sites.google.com/view/f-irl/home" target="_blank">https://sites.google.com/view/f-irl/home</a>.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1FeHTb2alfwWuc5kEvEvfJM0c1QQ5tY_P/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


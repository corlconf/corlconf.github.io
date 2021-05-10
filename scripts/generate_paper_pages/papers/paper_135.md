---
layout: page
title: "High Acceleration Reinforcement Learning for Real-World Juggling with Binary Rewards"
subtitle: 
description:
permalink: /paper_135/
grand_parent: All Papers
parent: Monday
supp: 
code: 
youtube_id: zmRx2okSoAg
pdf: https://drive.google.com/file/d/1Jm8GAfy3Y1EXAjbLJQNh2_40gdQnfNE8/view
---

# High Acceleration Reinforcement Learning for Real-World Juggling with Binary Rewards

<a href="https://drive.google.com/file/d/1Jm8GAfy3Y1EXAjbLJQNh2_40gdQnfNE8/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Kai Ploeger (TU Darmstadt)*; Michael Lutter (TU Darmstadt); Jan Peters (TU Darmstadt + Max Planck Institute for Intelligent Systems)**

#### Interactive Session
<em>2020-11-16, 11:50 - 12:20 PST </em> | <a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SESTZB9N1ASD10OHZ" target="_blank" rel="noopener noreferrer"> PheedLoop Session <i class="fa fa-external-link" aria-hidden="true"></i> </a> 

#### Abstract
Robots that can learn in the physical world will be important to enable robots to escape their stiff and pre-programmed movements.  For dynamic high-acceleration tasks, such as juggling, learning in the real-world is particularly challenging  as  one  must  push  the  limits  of  the  robot  and  its  actuation  without harming the system, amplifying the necessity of sample efficiency and safety for robot learning algorithms.  In contrast to prior work which mainly focuses on the learning algorithm, we propose a learning system, that directly incorporates these requirements in the design of the policy representation,  initialization,  and optimization.  We demonstrate that this system enables the high-speed Barrett WAM manipulator to learn juggling two balls from 56 minutes of experience with a binary reward signal and finally juggles continuously for up to 33 minutes or about 4500 repeated catches. The videos documenting the learning process and the evaluation can be found at <a href="https://sites.google.com/view/jugglingbot" target="_blank">https://sites.google.com/view/jugglingbot</a>

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


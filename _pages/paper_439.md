---
layout: page
title: "Deep Reactive Planning in Dynamic Environments"
subtitle: 
description:
permalink: /paper_439/
grand_parent: All Papers
parent: Monday
supp: 
code: https://youtu.be/hE-Ew59GRPQ
youtube_id: xknoGtn9jAE
pdf: https://drive.google.com/file/d/1t8FFYXhmcARZh1x6HhCe5fSipnUxDZkG/view
---

# Deep Reactive Planning in Dynamic Environments

<a href="https://drive.google.com/file/d/1t8FFYXhmcARZh1x6HhCe5fSipnUxDZkG/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="https://youtu.be/hE-Ew59GRPQ" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Kei Ota (Mitsubishi Electric Corporation)*; Devesh Jha (MERL); Tadashi Onishi (Mitsubishi Electric); Asako Kanezaki (Tokyo Institute of Technology); Yusuke Yoshiyasu (AIST); Yoko Sasaki (National Institute of Advanced Industrial Science and Technology	); Toshisada Mariyama (Mitsubishi Electric); Daniel Nikovski ()**

#### Interactive Session
<a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SES8L84QDMBWA7EKR" target="_blank" rel="noopener noreferrer"><em>2020-11-16, 12:30 - 13:00 PST </em></a>

#### Abstract
The main novelty of the proposed approach is that it allows a robot to learn an end-to-end policy which can adapt to changes in the environment during execution. While goal conditioning of policies has been studied in the RL literature, such approaches are not easily extended to settings where the robot's goal can change during execution. This is something that humans are naturally able to do. However, it is difficult for robots to learn such reflexes (i.e., to naturally respond to dynamic environments), especially when the goal location is not explicitly provided to the robot, and instead needs to be perceived through a vision sensor. In the current work, we present a method that can achieve such behavior by combining traditional kinematic planning, deep learning, and deep reinforcement learning in a synergistic fashion to generalize to arbitrary environments. We demonstrate the proposed approach for several reaching and pick-and-place tasks in simulation, as well as on a real system of a 6-DoF industrial manipulator.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1OqbSfAeeHW9qfYG7XTms5JmyfzjIoPlA/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


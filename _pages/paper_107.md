---
layout: page
title: "Auxiliary Tasks Speed Up Learning PointGoal Navigation"
subtitle: 
description:
permalink: /paper_107/
grand_parent: All Papers
parent: Wednesday
supp: 
code: https://github.com/joel99/habitat-pointnav-aux
youtubeId: 
---

# Auxiliary Tasks Speed Up Learning PointGoal Navigation

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1okMSBRynoPny7JLqiC1yl2HWSBxD7Ioj/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Joel Ye (Georgia Institute of Technology)*; Dhruv Batra (Georgia Tech & Facebook AI Research); Erik Wijmans (Georgia Tech); Abhishek Das (Facebook AI Research)**

#### Interactive Session
*2020-11-18, 12:30 - 13:00 PST*

#### Abstract
PointGoal Navigation is an embodied task that requires agents to navigate to a specified point in an unseen environment. Wijmans et al. showed that this task is solvable in simulation but their method is computationally prohibitive – requiring 2.5 billion frames of experience and 180 GPU-days. We develop a method to significantly improve sample efficiency in learning PointNav using self-supervised auxiliary tasks (e.g. predicting the action taken between two egocentric observations, predicting the distance between two observations from a trajectory, etc.). We find that naively combining multiple auxiliary tasks improves sample efficiency, but only provides marginal gains beyond a point. To overcome this, we use attention to combine representations from individual auxiliary tasks. Our best agent is 5.5x faster to match the performance of the previous state-of-the-art, DD-PPO, at 40M frames, and improves on DD-PPO’s performance at 40M frames by 0.16 SPL. Our code is publicly available at github.com/joel99/habitat-pointnav-aux.

#### Video 

#### Reviews

#### Rebuttal

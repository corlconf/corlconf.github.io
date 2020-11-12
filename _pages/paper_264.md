---
layout: page
title: "Towards Robotic Assembly by Predicting Robust, Precise and Task-oriented Grasps"
subtitle: 
description:
permalink: /paper_264/
grand_parent: All Papers
parent: Wednesday
supp: 
code: 
youtubeId: 
---

# Towards Robotic Assembly by Predicting Robust, Precise and Task-oriented Grasps

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/17PISQYfY9Jvvg-MK4_mG89wj-J3O65Mx/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Jialiang Zhao (Carnegie Mellon University)*; Daniel Troniak (Carnegie Mellon University); Oliver Kroemer (Carnegie Mellon University)**

#### Abstract
Robust task-oriented grasp planning is vital for autonomous robotic precision assembly tasks. Knowledge of the objects' geometry and preconditions of the target task should be incorporated when determining the proper grasp to execute. However, several factors contribute to the challenges of realizing these grasps such as noise when controlling the robot, unknown object properties, and difficulties modeling complex object-object interactions. We propose a method that decomposes this problem and optimizes for grasp robustness, precision, and task performance by learning three cascaded networks. We evaluate our method in simulation on three common assembly tasks: inserting gears onto pegs, aligning brackets into corners, and inserting shapes into slots. Our policies are trained using a curriculum based on large-scale self-supervised grasp simulations with procedurally generated objects. Finally, we evaluate the performance of the first two tasks with a real robot where our method achieves 4.28mm error for bracket insertion and 1.44mm error for gear insertion.

#### Video 

#### Reviews

#### Rebuttal

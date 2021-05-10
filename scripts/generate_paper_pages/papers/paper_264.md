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
youtube_id: b9L2JVj6Olo
pdf: https://drive.google.com/file/d/17PISQYfY9Jvvg-MK4_mG89wj-J3O65Mx/view
---

# Towards Robotic Assembly by Predicting Robust, Precise and Task-oriented Grasps

<a href="https://drive.google.com/file/d/17PISQYfY9Jvvg-MK4_mG89wj-J3O65Mx/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Jialiang Zhao (Carnegie Mellon University)*; Daniel Troniak (Carnegie Mellon University); Oliver Kroemer (Carnegie Mellon University)**

#### Interactive Session
<em>2020-11-18, 11:10 - 11:40 PST </em> | <a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SESXZBV8NPTFWYNGK" target="_blank" rel="noopener noreferrer"> PheedLoop Session <i class="fa fa-external-link" aria-hidden="true"></i> </a> 

#### Abstract
Robust task-oriented grasp planning is vital for autonomous robotic precision assembly tasks. Knowledge of the objects' geometry and preconditions of the target task should be incorporated when determining the proper grasp to execute. However, several factors contribute to the challenges of realizing these grasps such as noise when controlling the robot, unknown object properties, and difficulties modeling complex object-object interactions. We propose a method that decomposes this problem and optimizes for grasp robustness, precision, and task performance by learning three cascaded networks. We evaluate our method in simulation on three common assembly tasks: inserting gears onto pegs, aligning brackets into corners, and inserting shapes into slots. Our policies are trained using a curriculum based on large-scale self-supervised grasp simulations with procedurally generated objects. Finally, we evaluate the performance of the first two tasks with a real robot where our method achieves 4.28mm error for bracket insertion and 1.44mm error for gear insertion. 

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1MzGDI3LO2MbbrgL6Sr8nQkIjk8X-UBrv/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


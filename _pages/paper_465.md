---
layout: page
title: "Self-Supervised Learning of Scene-Graph Representations for Robotic Sequential Manipulation Planning"
subtitle: 
description:
permalink: /paper_465/
grand_parent: All Papers
parent: Wednesday
supp: 
code: https://github.com/sontung/location-based-generative
youtubeId: 
---

# Self-Supervised Learning of Scene-Graph Representations for Robotic Sequential Manipulation Planning

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1Pe_5WDbMg9UsaPR5GWXJKut7E1c5Vgw-/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Son Nguyen (University Stuttgart)*; Ozgur Oguz (Uni. of Stuttgart & Max Planck Inst. for Intelligent Systems ); Valentin Hartmann (University of Stuttgart); Marc Toussaint (Technische Universität Berlin)**

#### Abstract
We present a self-supervised representation learning approach for visual reasoning and integrate it into a nonlinear program formulation for motion optimization to tackle sequential manipulation tasks. Such problems have usually been addressed by combined task and motion planning approaches, for which spatial relations and logical rules that rely on symbolic representations have to be predefined by the user. We propose to learn relational structures by leveraging visual perception to alleviate the resulting knowledge acquisition bottleneck. In particular, we learn constructing <em>scene-graphs</em>, that represent objects ("red box"), and their spatial relationships ("yellow cylinder on red box"). This representation allows us to plan high-level discrete decisions effectively using graph search algorithms. We integrate the visual reasoning module with a nonlinear optimization method for robot motion planning and verify its feasibility on the classic blocks-world domain. Our proposed framework successfully finds the sequence of actions and enables the robot to execute feasible motion plans to realize the given tasks.  


#### Video 

#### Reviews

#### Rebuttal

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
youtube_id: 
pdf: https://drive.google.com/file/d/1Pe_5WDbMg9UsaPR5GWXJKut7E1c5Vgw-/view
---

# Self-Supervised Learning of Scene-Graph Representations for Robotic Sequential Manipulation Planning

<a href="https://drive.google.com/file/d/1Pe_5WDbMg9UsaPR5GWXJKut7E1c5Vgw-/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="https://github.com/sontung/location-based-generative" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Son Nguyen (University Stuttgart)*; Ozgur Oguz (Uni. of Stuttgart & Max Planck Inst. for Intelligent Systems ); Valentin Hartmann (University of Stuttgart); Marc Toussaint (Technische Universität Berlin)**

#### Interactive Session
<a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SES3FTTH7QASZ2HQQ" target="_blank" rel="noopener noreferrer"><em>2020-11-18, 12:30 - 13:00 PST </em></a>

#### Abstract
We present a self-supervised representation learning approach for visual reasoning and integrate it into a nonlinear program formulation for motion optimization to tackle sequential manipulation tasks. Such problems have usually been addressed by combined task and motion planning approaches, for which spatial relations and logical rules that rely on symbolic representations have to be predefined by the user. We propose to learn relational structures by leveraging visual perception to alleviate the resulting knowledge acquisition bottleneck. In particular, we learn constructing <em>scene-graphs</em>, that represent objects ("red box"), and their spatial relationships ("yellow cylinder on red box"). This representation allows us to plan high-level discrete decisions effectively using graph search algorithms. We integrate the visual reasoning module with a nonlinear optimization method for robot motion planning and verify its feasibility on the classic blocks-world domain. Our proposed framework successfully finds the sequence of actions and enables the robot to execute feasible motion plans to realize the given tasks.  


#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1qCWFQ2LvUl4-FaTGOFaWwFm4FOs-L1SZ/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


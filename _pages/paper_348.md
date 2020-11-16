---
layout: page
title: "Same Object, Different Grasps: Data and Semantic Knowledge for Task-Oriented Grasping"
subtitle: 
description:
permalink: /paper_348/
grand_parent: All Papers
parent: Monday
supp: 
code: https://github.com/adithyamurali/TaskGrasp
youtube_id: eV-KyT6OK14
pdf: https://drive.google.com/file/d/1XsG_zlvTPY878TNVLBn2iR1EOhse4SmV/view
---

# Same Object, Different Grasps: Data and Semantic Knowledge for Task-Oriented Grasping

<a href="https://drive.google.com/file/d/1XsG_zlvTPY878TNVLBn2iR1EOhse4SmV/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="https://github.com/adithyamurali/TaskGrasp" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Adithyavairavan Murali (Carnegie Mellon University Robotics Institute)*; Weiyu Liu (Georgia Institute of Technology); Kenneth Marino (Carnegie Mellon University); Sonia Chernova (Georgia Institute of Technology	); Abhinav Gupta (CMU/FAIR)**

#### Interactive Session
<a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SES4PCKRYYQTLBUBK" target="_blank" rel="noopener noreferrer"><em>2020-11-16, 11:10 - 11:40 PST </em></a>

#### Abstract
Despite the enormous progress and generalization in robotic grasping in recent years, existing methods have yet to scale and generalize task-oriented grasping to the same extent. This is largely due to the scale of the datasets both in terms of the number of objects and tasks studied. We address these concerns with the TaskGrasp dataset which is more diverse both in terms of objects and tasks, and an order of magnitude larger than previous datasets. The dataset contains 250K task-oriented grasps for 56 tasks and 191 objects along with their RGB-D information. We take advantage of this new breadth and diversity in the data and present the GCNGrasp framework which uses the semantic knowledge of objects and tasks encoded in a knowledge graph to generalize to new object instances, classes and even new tasks. Our framework shows a significant improvement of around 12% on held-out settings compared to baseline methods which do not use semantics. We demonstrate that our dataset and model are applicable for the real world by executing task-oriented grasps on a real robot on unknown objects. Code, data and supplementary video could be found at <a href="https://github.com/adithyamurali/TaskGrasp" target="_blank">https://github.com/adithyamurali/TaskGrasp</a>.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1feYlR_G-VZNwQA7EpQNWWZOfrvVL-3DV/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


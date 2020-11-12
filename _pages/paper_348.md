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
youtubeId: 
---

# Same Object, Different Grasps: Data and Semantic Knowledge for Task-Oriented Grasping

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1XsG_zlvTPY878TNVLBn2iR1EOhse4SmV/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Adithyavairavan Murali (Carnegie Mellon University Robotics Institute)*; Weiyu Liu (Georgia Institute of Technology); Kenneth Marino (Carnegie Mellon University); Sonia Chernova (Georgia Institute of Technology	); Abhinav Gupta (CMU/FAIR)**

#### Abstract
Despite the enormous progress and generalization in robotic grasping in recent years, existing methods have yet to scale and generalize task-oriented grasping to the same extent. This is largely due to the scale of the datasets both in terms of the number of objects and tasks studied. We address these concerns with the TaskGrasp dataset which is more diverse both in terms of objects and tasks, and an order of magnitude larger than previous datasets. The dataset contains 250K task-oriented grasps for 56 tasks and 191 objects along with their RGB-D information. We take advantage of this new breadth and diversity in the data and present the GCNGrasp framework which uses the semantic knowledge of objects and tasks encoded in a knowledge graph to generalize to new object instances, classes and even new tasks. Our framework shows a significant improvement of around 12% on held-out settings compared to baseline methods which do not use semantics. We demonstrate that our dataset and model are applicable for the real world by executing task-oriented grasps on a real robot on unknown objects. Code, data and supplementary video could be found at <a href="https://github.com/adithyamurali/TaskGrasp" target="_blank">https://github.com/adithyamurali/TaskGrasp</a>.

#### Video 

#### Reviews

#### Rebuttal

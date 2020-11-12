---
layout: page
title: "TartanVO: A Generalizable Learning-based VO"
subtitle: 
description:
permalink: /paper_395/
grand_parent: All Papers
parent: Wednesday
supp: 
code: https://github.com/castacks/tartanvo
youtubeId: 
---

# TartanVO: A Generalizable Learning-based VO

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1W7Y0yPGBICpADbm79xQ1-PL2JDBbkTdu/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Wenshan Wang (CMU)*; Yaoyu Hu (Carnegie Mellon University); Sebastian Scherer (Carnegie Mellon University)**

#### Abstract
We present the first learning-based visual odometry (VO) model, which generalizes to multiple datasets and real-world scenarios and outperforms geometry-based methods in challenging scenes. We achieve this by leveraging the SLAM dataset TartanAir, which provides a large amount of diverse synthetic data in challenging environments. Furthermore, to make our VO model generalize across datasets, we propose an up-to-scale loss function and incorporate the camera intrinsic parameters into the model. Experiments show that a single model, TartanVO, trained only on synthetic data, without any finetuning, can be generalized to real-world datasets such as KITTI and EuRoC, demonstrating significant advantages over the geometry-based methods on challenging trajectories. Our code is available at <a href="https://github.com/castacks/tartanvo" target="_blank">https://github.com/castacks/tartanvo</a>.

#### Video 

#### Reviews

#### Rebuttal

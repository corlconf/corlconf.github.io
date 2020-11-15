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
youtube_id: KinJAUKeLOY
pdf: https://drive.google.com/file/d/1W7Y0yPGBICpADbm79xQ1-PL2JDBbkTdu/view
---

# TartanVO: A Generalizable Learning-based VO

<a href="https://drive.google.com/file/d/1W7Y0yPGBICpADbm79xQ1-PL2JDBbkTdu/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="https://github.com/castacks/tartanvo" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Wenshan Wang (CMU)*; Yaoyu Hu (Carnegie Mellon University); Sebastian Scherer (Carnegie Mellon University)**

#### Interactive Session
*2020-11-18, 11:50 - 12:20 PST* 

#### Abstract
We present the first learning-based visual odometry (VO) model, which generalizes to multiple datasets and real-world scenarios and outperforms geometry-based methods in challenging scenes. We achieve this by leveraging the SLAM dataset TartanAir, which provides a large amount of diverse synthetic data in challenging environments. Furthermore, to make our VO model generalize across datasets, we propose an up-to-scale loss function and incorporate the camera intrinsic parameters into the model. Experiments show that a single model, TartanVO, trained only on synthetic data, without any finetuning, can be generalized to real-world datasets such as KITTI and EuRoC, demonstrating significant advantages over the geometry-based methods on challenging trajectories. Our code is available at <a href="https://github.com/castacks/tartanvo" target="_blank">https://github.com/castacks/tartanvo</a>.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1nm5jeB8SN5QmiLK8S_AoVPWY0lr8SYc6/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


---
layout: page
title: "S3K: Self-Supervised Semantic Keypoints for Robotic Manipulation via Multi-View Consistency"
subtitle: 
description:
permalink: /paper_96/
grand_parent: All Papers
parent: Wednesday
supp: 
code: 
youtube_id: FB3p-LUEOBE
pdf: https://drive.google.com/file/d/15lZ0nPZeV5zFY2heTU2ZZUpaXQkuJPH8/view
---

# S3K: Self-Supervised Semantic Keypoints for Robotic Manipulation via Multi-View Consistency

<a href="https://drive.google.com/file/d/15lZ0nPZeV5zFY2heTU2ZZUpaXQkuJPH8/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Mel Vecerik (University College London, Deepmind)*; Jean-Baptiste Regli (Deepmind); Oleg Sushkov (DeepMind); David Barker (DeepMind); Rugile Pevceviciute (DeepMind); Thomas Roth ̈orl (DeepMind); Raia Hadsell (Deepmind); Lourdes Agapito (University College London); Jonathan Scholz (DeepMind)**

#### Interactive Session
<a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SESXTNUC8EHD5TZTR" target="_blank" rel="noopener noreferrer"><em>2020-11-18, 11:10 - 11:40 PST </em></a>

#### Abstract
A robot’s ability to act is fundamentally constrained by what it can perceive. Many existing approaches to visual representation learning utilize general-purpose training criteria, e.g. image reconstruction, smoothness in latent space, or usefulness for control, or else make use of large datasets annotated with specific features (bounding boxes, segmentations, etc.). However, both approaches often struggle to capture the fine-detail required for precision tasks on specific objects, e.g. grasping and mating a plug and socket. We argue that these difficulties arise from a lack of geometric structure in these models. In this work we advocate semantic 3D keypoints as a visual representation, and present a semi-supervised training objective that can allow instance or category-level keypoints to be trained to 1-5 millimeter-accuracy with minimal supervision. Furthermore, unlike local texture-based approaches, our model integrates contextual information from a large area and is therefore robust to occlusion, noise, and lack of discernible texture. We demonstrate that this ability to locate semantic keypoints enables high level scripting of human understandable behaviours. Finally we show that these keypoints provide a good way to define reward functions for reinforcement learning and area good representation for training agents.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1hO2F_yAWVvBJEr4ou9tqjkyB1QRkz8zq/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


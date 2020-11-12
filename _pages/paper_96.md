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
youtubeId: 
---

# S3K: Self-Supervised Semantic Keypoints for Robotic Manipulation via Multi-View Consistency

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/15lZ0nPZeV5zFY2heTU2ZZUpaXQkuJPH8/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Mel Vecerik (University College London, Deepmind)*; Jean-Baptiste Regli (Deepmind); Oleg Sushkov (DeepMind); David Barker (DeepMind); Rugile Pevceviciute (DeepMind); Thomas Roth ̈orl (DeepMind); Raia Hadsell (Deepmind); Lourdes Agapito (University College London); Jonathan Scholz (DeepMind)**

#### Abstract
A robot’s ability to act is fundamentally constrained by what it can perceive. Many existing approaches to visual representation learning utilize general-purpose training criteria, e.g. image reconstruction, smoothness in latent space, or usefulness for control, or else make use of large datasets annotated with specific features (bounding boxes, segmentations, etc.). However, both approaches often struggle to capture the fine-detail required for precision tasks on specific objects, e.g. grasping and mating a plug and socket. We argue that these difficulties arise from a lack of geometric structure in these models. In this work we advocate semantic 3D keypoints as a visual representation, and present a semi-supervised training objective that can allow instance or category-level keypoints to be trained to 1-5 millimeter-accuracy with minimal supervision. Furthermore, unlike local texture-based approaches, our model integrates contextual information from a large area and is therefore robust to occlusion, noise, and lack of discernible texture. We demonstrate that this ability to locate semantic keypoints enables high level scripting of human understandable behaviours. Finally we show that these keypoints provide a good way to define reward functions for reinforcement learning and area good representation for training agents.

#### Video 

#### Reviews

#### Rebuttal

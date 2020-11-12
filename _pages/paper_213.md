---
layout: page
title: "Tactile Object Pose Estimation from the First Touch with Geometric Contact Rendering"
subtitle: 
description:
permalink: /paper_213/
grand_parent: All Papers
parent: Wednesday
supp: 
code: 
youtubeId: 
---

# Tactile Object Pose Estimation from the First Touch with Geometric Contact Rendering

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1UffNYaHKLG7ZjsYLxNsYJO_ioszEbmBq/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Maria Bauza Villalonga (MIT)*; Alberto Rodriguez (MIT); Bryan Lim (MIT); Eric  Valls (MIT); Theo  Sechopoulos (MIT)**

#### Abstract
In this paper, we present an approach to tactile pose estimation from the first touch for known objects. First, we create an object-agnostic map from real tactile observations to contact shapes. Next, for a new object with known geometry, we learn a tailored perception model completely in simulation. To do so, we simulate the contact shapes that a dense set of object poses would produce on the sensor. Then, given a new contact shape obtained from the sensor output, we match it against the pre-computed set using the object-specific embedding learned purely in simulation using contrastive learning.

This results in a perception model that can localize objects from a single tactile observation. It also allows reasoning over pose distributions and including additional pose constraints coming from other perception systems or multiple contacts.

We provide quantitative results for four objects. Our approach provides high accuracy pose estimations from distinctive tactile observations while regressing pose distributions to account for those contact shapes that could result from different object poses. We further extend and test our approach in multi-contact scenarios where several tactile sensors are simultaneously in contact with the object.
Keywords: Tactile Sensing, Object Pose Estimation, Manipulation, Learning

#### Video 

#### Reviews

#### Rebuttal

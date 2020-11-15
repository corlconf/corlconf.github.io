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
youtube_id: 
pdf: https://drive.google.com/file/d/1UffNYaHKLG7ZjsYLxNsYJO_ioszEbmBq/view
---

# Tactile Object Pose Estimation from the First Touch with Geometric Contact Rendering

<a href="https://drive.google.com/file/d/1UffNYaHKLG7ZjsYLxNsYJO_ioszEbmBq/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Maria Bauza Villalonga (MIT)*; Alberto Rodriguez (MIT); Bryan Lim (MIT); Eric  Valls (MIT); Theo  Sechopoulos (MIT)**

#### Interactive Session
*2020-11-18, 11:50 - 12:20 PST* 

#### Abstract
In this paper, we present an approach to tactile pose estimation from the first touch for known objects. First, we create an object-agnostic map from real tactile observations to contact shapes. Next, for a new object with known geometry, we learn a tailored perception model completely in simulation. To do so, we simulate the contact shapes that a dense set of object poses would produce on the sensor. Then, given a new contact shape obtained from the sensor output, we match it against the pre-computed set using the object-specific embedding learned purely in simulation using contrastive learning.

This results in a perception model that can localize objects from a single tactile observation. It also allows reasoning over pose distributions and including additional pose constraints coming from other perception systems or multiple contacts.

We provide quantitative results for four objects. Our approach provides high accuracy pose estimations from distinctive tactile observations while regressing pose distributions to account for those contact shapes that could result from different object poses. We further extend and test our approach in multi-contact scenarios where several tactile sensors are simultaneously in contact with the object.
Keywords: Tactile Sensing, Object Pose Estimation, Manipulation, Learning

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1CDHtYLQKwvGDHnCbXs6L48U73aymvfGG/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


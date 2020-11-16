---
layout: page
title: "Map-Adaptive Goal-Based Trajectory Prediction"
subtitle: 
description:
permalink: /paper_296/
grand_parent: All Papers
parent: Monday
supp: 
code: 
youtube_id: 2PLcvgv_EzM
pdf: https://drive.google.com/file/d/1Gwd2P1div60UHxHa3eq373ZDrwbzkQzG/view
---

# Map-Adaptive Goal-Based Trajectory Prediction

<a href="https://drive.google.com/file/d/1Gwd2P1div60UHxHa3eq373ZDrwbzkQzG/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Lingyao Zhang (Uber ATG)*; Po-Hsun Su (UATC LLC); Jerrick Hoang (Uber ATG); Galen Clark  Haynes (Uber ATC); Micol Marchetti-Bowick (Uber ATG)**

#### Interactive Session
<em>2020-11-16, 11:50 - 12:20 PST </em> | <a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SESCVX2F5JUU66U88" target="_blank" rel="noopener noreferrer"> PheedLoop Session <i class="fa fa-external-link" aria-hidden="true"></i> </a> 

#### Abstract
We present a new method for multi-modal, long-term vehicle trajectory prediction. Our approach relies on using lane centerlines captured in rich maps of the environment to generate a set of proposed goal paths for each vehicle. Using these paths - which are generated at run time and therefore dynamically adapt to the scene - as spatial anchors, we predict a set of goal-based trajectories along with a categorical distribution over the goals. This approach allows us to directly model the goal-directed behavior of traffic actors, which unlocks the potential for more accurate long-term prediction. Our experimental results on both a large-scale internal driving dataset and on the public nuScenes dataset show that our model outperforms state-of-the-art approaches for vehicle trajectory prediction over a 6-second horizon. We also empirically demonstrate that our model is better able to generalize to road scenes from a completely new city than existing methods.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1BwMou9eKT5wYLa-YuVDkuNyHv0L4bqWL/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


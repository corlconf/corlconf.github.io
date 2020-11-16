---
layout: page
title: "LiRaNet: End-to-End Trajectory Prediction using Spatio-Temporal Radar Fusion"
subtitle: 
description:
permalink: /paper_17/
grand_parent: All Papers
parent: Tuesday
supp: 
code: 
youtube_id: nRum-4hqRGU
pdf: https://drive.google.com/file/d/1DHcWIcLQpJAozpHQT1XRzkNP2MR3Ilja/view
---

# LiRaNet: End-to-End Trajectory Prediction using Spatio-Temporal Radar Fusion

<a href="https://drive.google.com/file/d/1DHcWIcLQpJAozpHQT1XRzkNP2MR3Ilja/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Meet Shah (Uber ATG)*; Zhiling Huang (Uber ATG); Ankit Laddha (Uber); Matthew Langford (UberATG); Blake Barber (Uber ATG); sida zhang (Uber); Carlos Vallespi-Gonzalez (Uber); Raquel Urtasun (Uber ATG)**

#### Interactive Session
<a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SESER5YG1KCZWTQH4" target="_blank" rel="noopener noreferrer"><em>2020-11-17, 11:10 - 11:40 PST </em></a>

#### Abstract
In this paper, we present LiRaNet, a novel end-to-end trajectory prediction method which utilizes radar sensor information along with widely used lidar and HD maps. Automotive radar provides rich, complementary information, allowing for longer range vehicle detection as well as instantaneous radial velocity measurements. However, there are factors that make the fusion of lidar and radar information challenging, such as the relatively low angular resolution of radar measurements, their sparsity and the lack of exact time synchronization with lidar. To overcome these challenges, we propose an efficient spatio-temporal radar feature extraction scheme which achieves state-of-the-art performance on multiple large-scale datasets. Further, by incorporating radar information, we show a 52% reduction in prediction error for objects with high acceleration and a 16% reduction in prediction error for objects at longer range.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


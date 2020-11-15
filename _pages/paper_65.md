---
layout: page
title: "PLOP: Probabilistic poLynomial Objects trajectory Prediction for autonomous driving"
subtitle: 
description:
permalink: /paper_65/
grand_parent: All Papers
parent: Monday
supp: https://drive.google.com/file/d/1RvKJHIuPhdpdA5aUb2ahWhRXjl9jXAQv/view
code: 
youtube_id: NFqxj_JyGxY
pdf: https://drive.google.com/file/d/1--QAL2sR7KMk9R4DwxyfJAT5iGCheFrn/view
---

# PLOP: Probabilistic poLynomial Objects trajectory Prediction for autonomous driving

<a href="https://drive.google.com/file/d/1--QAL2sR7KMk9R4DwxyfJAT5iGCheFrn/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="https://drive.google.com/file/d/1RvKJHIuPhdpdA5aUb2ahWhRXjl9jXAQv/view" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Thibault Buhet (Valeo); Emilie Wirbel (Valeo)*; Andrei Bursuc (valeo.ai); Xavier Perrotton (Valeo)**

#### Interactive Session
*2020-11-16, 11:10 - 11:40 PST* 

#### Abstract
To navigate safely in urban environments, an autonomous vehicle (ego vehicle) must understand and anticipate its surroundings, in particular the behavior and intents of other road users (neighbors). Most of the times, multiple decision choices are acceptable for all road users (e.g., turn right or left, or different ways of avoiding an obstacle), leading to a highly uncertain and multi-modal decision space. We focus here on predicting multiple feasible future trajectories for both ego vehicle and neighbors through a probabilistic framework. We rely on a conditional imitation learning algorithm, conditioned by a navigation command for the ego vehicle (e.g., “turn right”). Our model processes ego vehicle front-facing camera images and bird-eye view grid, computed from Lidar point clouds, with detections of past and present objects, in order to generate multiple trajectories for both ego vehicle and its neighbors. Our approach is computationally efficient and relies only on on-board sensors. We evaluate our method offline on the publicly available dataset nuScenes, achieving state-of-the-art performance, investigate the impact of our architecture choices on online simulated experiments and show preliminary insights for real vehicle control.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1W2Xjii9pdYbDKZ9wXyj2ee9kMq88fjNF/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


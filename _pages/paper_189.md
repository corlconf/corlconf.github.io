---
layout: page
title: "TNT: Target-driveN Trajectory Prediction"
subtitle: 
description:
permalink: /paper_189/
grand_parent: All Papers
parent: Wednesday
supp: 
code: 
youtubeId: 
pdf: https://drive.google.com/file/d/1Ol40GkiELqcechS9eWINoacMb5ebDUkD/view
---

# TNT: Target-driveN Trajectory Prediction

<a href="https://drive.google.com/file/d/1Ol40GkiELqcechS9eWINoacMb5ebDUkD/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Hang Zhao (Waymo)*; Jiyang Gao (Waymo); Tian Lan (Waymo); Chen Sun (Google); Ben Sapp (Waymo); Balakrishnan Varadarajan (Google Research); Yue Shen (Waymo, LLC); Yi Shen (Waymo); Yuning Chai (Waymo); Cordelia Schmid (Google); Congcong Li (Waymo); Dragomir Anguelov (Waymo)**

#### Interactive Session
*2020-11-18, 12:30 - 13:00 PST*

#### Abstract
Predicting the future behavior of moving agents is essential for real world applications. It is challenging as the intent of the agent and the corresponding behavior is unknown and intrinsically multimodal. Our key insight is that for prediction within a moderate time horizon, the future modes can be effectively captured by a set of target states. This leads to our target-driven trajectory prediction (TNT) framework. TNT has three stages which are trained end-to-end. It
first predicts an agent's potential target states T steps into the future, by encoding its interactions with the environment and the other agents. TNT then generates trajectory state sequences conditioned on targets. A final stage estimates trajectory likelihoods and a final compact set of trajectory predictions is selected. This is in contrast to previous work which models agent intents as latent variables, and relies on test-time sampling to generate diverse trajectories. We benchmark TNT on trajectory prediction of vehicles and pedestrians, where we achieve better than state-of-the-art performance on Argoverse Forecasting, INTERACTION, Stanford Drone and an in-house Pedestrian-at-Intersection dataset.


#### Video 

#### Reviews

#### Rebuttal


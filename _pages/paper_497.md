---
layout: page
title: "Multimodal Trajectory Prediction via Topological Invariance for Navigation at Uncontrolled Intersections"
subtitle: 
description:
permalink: /paper_497/
grand_parent: All Papers
parent: Wednesday
supp: 
code: https://github.com/rohjunha/multiple-topologies-prediction
youtube_id: RpIu3yVArmA
pdf: https://drive.google.com/file/d/1mzKW09aNW683bCveX8bKjUYRo5sVq3fH/view
---

# Multimodal Trajectory Prediction via Topological Invariance for Navigation at Uncontrolled Intersections

<a href="https://drive.google.com/file/d/1mzKW09aNW683bCveX8bKjUYRo5sVq3fH/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="https://github.com/rohjunha/multiple-topologies-prediction" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Junha Roh (University of Washington); Christoforos Mavrogiannis (University of Washington)*; Rishabh Madan (Indian Institute of Technology Kharagpur); Dieter Fox (NVIDIA Research / University of Washington); Siddhartha Srinivasa (University of Washington)**

#### Interactive Session
<a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SESA1JM2DT75H969T" target="_blank" rel="noopener noreferrer"><em>2020-11-18, 11:10 - 11:40 PST </em></a>

#### Abstract
We focus on decentralized navigation among multiple non-communicating rational agents at <em>uncontrolled</em> intersections, i.e., street intersections without traffic signs or signals. Avoiding collisions in such domains relies on the ability of agents to predict each others' intentions reliably, and react quickly. Multiagent trajectory prediction is NP-hard whereas the sample complexity of existing data-driven approaches limits their applicability. Our key insight is that the geometric structure of the intersection and the incentive of agents to move efficiently and avoid collisions (rationality) reduces the space of likely behaviors, effectively relaxing the problem of trajectory prediction. In this paper, we collapse the space of multiagent trajectories at an intersection into a set of modes representing different classes of multiagent behavior, formalized using a notion of topological invariance. Based on this formalism, we design Multiple Topologies Prediction (MTP), a data-driven trajectory-prediction mechanism that reconstructs trajectory representations of high-likelihood modes in multiagent intersection scenes. We show that MTP outperforms a state-of-the-art multimodal trajectory prediction baseline (MFP) in terms of prediction accuracy by 78.24% on a challenging simulated dataset. Finally, we show that MTP enables our optimization-based planner, MTPnav, to achieve collision-free and time-efficient navigation across a variety of challenging intersection scenarios on the CARLA simulator.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1GFksoXIwEPvNqewZzEdi8-6ad6qpZUz1/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


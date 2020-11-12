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
youtubeId: 
---

# Multimodal Trajectory Prediction via Topological Invariance for Navigation at Uncontrolled Intersections

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1mzKW09aNW683bCveX8bKjUYRo5sVq3fH/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Junha Roh (University of Washington); Christoforos Mavrogiannis (University of Washington)*; Rishabh Madan (Indian Institute of Technology Kharagpur); Dieter Fox (NVIDIA Research / University of Washington); Siddhartha Srinivasa (University of Washington)**

#### Abstract
We focus on decentralized navigation among multiple non-communicating rational agents at <em>uncontrolled</em> intersections, i.e., street intersections without traffic signs or signals. Avoiding collisions in such domains relies on the ability of agents to predict each others' intentions reliably, and react quickly. Multiagent trajectory prediction is NP-hard whereas the sample complexity of existing data-driven approaches limits their applicability. Our key insight is that the geometric structure of the intersection and the incentive of agents to move efficiently and avoid collisions (rationality) reduces the space of likely behaviors, effectively relaxing the problem of trajectory prediction. In this paper, we collapse the space of multiagent trajectories at an intersection into a set of modes representing different classes of multiagent behavior, formalized using a notion of topological invariance. Based on this formalism, we design Multiple Topologies Prediction (MTP), a data-driven trajectory-prediction mechanism that reconstructs trajectory representations of high-likelihood modes in multiagent intersection scenes. We show that MTP outperforms a state-of-the-art multimodal trajectory prediction baseline (MFP) in terms of prediction accuracy by 78.24% on a challenging simulated dataset. Finally, we show that MTP enables our optimization-based planner, MTPnav, to achieve collision-free and time-efficient navigation across a variety of challenging intersection scenarios on the CARLA simulator.

#### Video 

#### Reviews

#### Rebuttal

---
layout: page
title: "The EMPATHIC Framework for Task Learning from Implicit Human Feedback"
subtitle: 
description:
permalink: /paper_132/
grand_parent: All Papers
parent: Tuesday
supp: 
code: https://github.com/Pearl-UTexas/EMPATHIC
youtubeId: 
---

# The EMPATHIC Framework for Task Learning from Implicit Human Feedback

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1oSSQbj9Oclzek4A5CrW4fWffQLFdZPeC/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Yuchen Cui (University of Texas at Austin)*; Qiping Zhang (The University of Texas at Austin); Brad Knox (Bosch); Alessandro Allievi (Bosch); Peter Stone (University of Texas at Austin and Sony AI); Scott Niekum (UT Austin)**

#### Interactive Session
*2020-11-17, 11:10 - 11:40 PST*

#### Abstract
Reactions such as gestures, facial expressions, and vocalizations are an abundant, naturally occurring channel of information that humans provide during interactions. A robot or other agent could leverage an understanding of such implicit human feedback to improve its task performance at no cost to the human. This approach contrasts with common agent teaching methods based on demonstrations, critiques, or other guidance that need to be attentively and intentionally provided. In this paper, we first define the general problem of learning from implicit human feedback and then propose to address this problem through a novel data-driven framework, EMPATHIC. This two-stage method consists of (1) mapping implicit human feedback to relevant task statistics such as reward, optimality, and advantage; and (2) using such a mapping to learn a task. We instantiate the first stage and three second-stage evaluations of the learned mapping. To do so, we collect a dataset of human facial reactions while subjects observe an agent execute a sub-optimal policy for a prescribed training task. We train a deep neural network on this data and demonstrate its ability to (1) infer relative reward ranking of events in the training task from prerecorded human facial reactions; (2) improve the policy of an agent in the training task using live human facial reactions; and (3) transfer to a novel domain in which it evaluates robot manipulation trajectories.

#### Video 

#### Reviews

#### Rebuttal

---
layout: page
title: "Learning Equality Constraints for Motion Planning on Manifolds"
subtitle: 
description:
permalink: /paper_515/
grand_parent: All Papers
parent: Tuesday
supp: 
code: https://github.com/gsutanto/smp_manifold_learning
youtubeId: 
---

# Learning Equality Constraints for Motion Planning on Manifolds

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1EWQLYvUUi52kRA5Cu5LcpwdTO43hqDLB/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Giovanni Sutanto (USC); Isabel Rayas Fernández (University of Southern California)*; Peter Englert (University of Southern California); Ragesh Kumar Ramachandran (University of Southern California); Gaurav Sukhatme (University of Southern California)**

#### Abstract
Constrained robot motion planning is a widely used technique to solve complex robot tasks. We consider the problem of learning representations of constraints from demonstrations with a deep neural network, which we call Equality Constraint Manifold Neural Network (ECoMaNN). The key idea is to learn a level-set function of the constraint suitable for integration into a constrained sampling-based motion planner. Learning proceeds by aligning subspaces in the network with subspaces of the data. We combine both learned constraints and analytically described constraints into the planner and use a projection-based strategy to find valid points. We evaluate ECoMaNN on its representation capabilities of constraint manifolds, the impact of its individual loss terms, and the motions produced when incorporated into a planner.

#### Video 

#### Reviews

#### Rebuttal

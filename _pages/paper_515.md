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
youtube_id: dxIkL88DFk0
pdf: https://drive.google.com/file/d/1EWQLYvUUi52kRA5Cu5LcpwdTO43hqDLB/view
---

# Learning Equality Constraints for Motion Planning on Manifolds

<a href="https://drive.google.com/file/d/1EWQLYvUUi52kRA5Cu5LcpwdTO43hqDLB/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="https://github.com/gsutanto/smp_manifold_learning" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Giovanni Sutanto (USC); Isabel Rayas Fernández (University of Southern California)*; Peter Englert (University of Southern California); Ragesh Kumar Ramachandran (University of Southern California); Gaurav Sukhatme (University of Southern California)**

#### Interactive Session
<em>2020-11-17, 12:30 - 13:00 PST </em> | <a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SES8K6QAE2MMVLH7P" target="_blank" rel="noopener noreferrer"> PheedLoop Session <i class="fa fa-external-link" aria-hidden="true"></i> </a> 

#### Abstract
Constrained robot motion planning is a widely used technique to solve complex robot tasks. We consider the problem of learning representations of constraints from demonstrations with a deep neural network, which we call Equality Constraint Manifold Neural Network (ECoMaNN). The key idea is to learn a level-set function of the constraint suitable for integration into a constrained sampling-based motion planner. Learning proceeds by aligning subspaces in the network with subspaces of the data. We combine both learned constraints and analytically described constraints into the planner and use a projection-based strategy to find valid points. We evaluate ECoMaNN on its representation capabilities of constraint manifolds, the impact of its individual loss terms, and the motions produced when incorporated into a planner.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1xlkXAoxx848KMF4SqsGlq6KTlnuFfSoL/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


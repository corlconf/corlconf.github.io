---
layout: page
title: "A Long Horizon Planning Framework for Manipulating Rigid Pointcloud Objects"
subtitle: 
description:
permalink: /paper_358/
grand_parent: All Papers
parent: Tuesday
supp: 
code: 
youtube_id: 
pdf: https://drive.google.com/file/d/1quDURs-x9x02tfxmCnxoi210dumoErf2/view
---

# A Long Horizon Planning Framework for Manipulating Rigid Pointcloud Objects

<a href="https://drive.google.com/file/d/1quDURs-x9x02tfxmCnxoi210dumoErf2/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Anthony Simeonov (Massachusetts Institute of Technology)*; Yilun Du (MIT); Beomjoon Kim (MIT); Francois Hogan (MIT); Joshua Tenenbaum (MIT); Pulkit Agrawal (UC Berkeley); Alberto Rodriguez (MIT)**

#### Interactive Session
<em>2020-11-17, 12:30 - 13:00 PST </em> | <a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SESUGB87CMKQPSALA" target="_blank" rel="noopener noreferrer"> PheedLoop Session <i class="fa fa-external-link" aria-hidden="true"></i> </a> 

#### Abstract
We present a framework for solving long-horizon planning problems involving manipulation of rigid objects that operates directly from a point-cloud observation. Our method plans in the space of object subgoals and frees the planner from reasoning about robot-object interaction dynamics. We show that for rigid-bodies, this abstraction can be realized using low-level manipulation skills that maintain sticking-contact with the object and represent subgoals as 3D transformations. To enable generalization to unseen objects and improve planning performance, we propose a novel way of representing subgoals for rigid-body manipulation and a graph-attention based neural network architecture for processing point-cloud inputs. We experimentally validate these choices using simulated and real-world experiments on the YuMi robot. Results demonstrate that our method can successfully manipulate new objects into target configurations requiring long-term planning. Overall, our framework realizes the best of the worlds of task-and-motion planning (TAMP) and learning-based approaches. Project website: <a href="https://anthonysimeonov.github.io/rpo-planning-framework/" target="_blank">https://anthonysimeonov.github.io/rpo-planning-framework/</a>.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1jx3IWb72Q9UrlEQS2h_m_PYWCZdK4wQ6/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


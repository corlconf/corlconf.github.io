---
layout: page
title: "Learning to Compose Hierarchical Object-Centric Controllers for Robotic Manipulation"
subtitle: 
description:
permalink: /paper_176/
grand_parent: All Papers
parent: Monday
supp: 
code: 
youtube_id: pC8RbComKP0
pdf: https://drive.google.com/file/d/1_AmvLIdfusAQ3NDt0fr8taGfAImFobxe/view
---

# Learning to Compose Hierarchical Object-Centric Controllers for Robotic Manipulation

<a href="https://drive.google.com/file/d/1_AmvLIdfusAQ3NDt0fr8taGfAImFobxe/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Mohit Sharma (Carnegie Mellon University)*; Jacky  Liang (Carnegie Mellon University)*; Jialiang Zhao (Carnegie Mellon University); Alex  Lagrassa (Carnegie Mellon University); Oliver Kroemer (Carnegie Mellon University)**

#### Interactive Session
*2020-11-16, 11:50 - 12:20 PST* 

#### Abstract
Manipulation tasks can often be decomposed into multiple subtasks performed in parallel, e.g., sliding an object to a goal pose while maintaining contact with a table.  Individual subtasks can be achieved by task-axis controllers defined relative to the objects being manipulated, and a set of object-centric controllers can be combined in an hierarchy. In prior works, such combinations are defined manually or learned from demonstrations. By contrast, we propose using reinforcement learning to dynamically compose hierarchical object-centric controllers for manipulation tasks. Experiments in both simulation and real world show how the proposed approach leads to improved sample efficiency, zero-shot generalization to novel test environments, and simulation-to-reality transfer without fine-tuning.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/118WeayIJBIufmZmMf58wdYA7G7D9o26N/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


---
layout: page
title: "Relational Learning for Skill Preconditions"
subtitle: 
description:
permalink: /paper_178/
grand_parent: All Papers
parent: Monday
supp: 
code: 
youtube_id: Fq4cjbJBk-8
pdf: https://drive.google.com/file/d/1mKL5JjbXxOJ-SMIEHEXO5Zps9l7-2Kr7/view
---

# Relational Learning for Skill Preconditions

<a href="https://drive.google.com/file/d/1mKL5JjbXxOJ-SMIEHEXO5Zps9l7-2Kr7/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Mohit Sharma (Carnegie Mellon University)*; Oliver Kroemer (Carnegie Mellon University)**

#### Interactive Session
<a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SESJ0HA0IT1FYO3SH" target="_blank" rel="noopener noreferrer"><em>2020-11-16, 11:10 - 11:40 PST </em></a>

#### Abstract
To determine if a skill can be executed in any given environment, a robot needs to learn the preconditions for the skill. As robots begin to operate in dynamic and unstructured environments, these precondition models will need to generalize to variable number of objects with different shapes and sizes. In this work, we focus on learning precondition models for manipulation skills in unconstrained environments.
Our work is motivated by the intuition that many complex manipulation tasks, with multiple objects, can be simplified by focusing on less complex pairwise object relations. We propose an object-relation model that learns continuous representations for these pairwise object relations.  Our object-relation model is trained completely in simulation, and once learned, is used by a separate precondition model to predict skill preconditions for real world tasks. We evaluate our precondition model on 3 different manipulation tasks: sweeping, cutting, and unstacking.  We show that our approach leads to significant improvements in predicting preconditions for all 3 tasks, across objects of different shapes and sizes.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1GW4o2pNQYbP1SETzoDZKKK_-H4TmSm26/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


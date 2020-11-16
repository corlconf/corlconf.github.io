---
layout: page
title: "Learning Arbitrary-Goal Fabric Folding with One Hour of Real Robot Experience"
subtitle: 
description:
permalink: /paper_518/
grand_parent: All Papers
parent: Wednesday
supp: 
code: 
youtube_id: me_02NhUs1Q
pdf: https://drive.google.com/file/d/1-yrBea9Ra9sYOEjG8iDQXgzqvB97u-vK/view
---

# Learning Arbitrary-Goal Fabric Folding with One Hour of Real Robot Experience

<a href="https://drive.google.com/file/d/1-yrBea9Ra9sYOEjG8iDQXgzqvB97u-vK/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Robert Lee (Queensland University of Technology)*; Daniel Ward (The University of Queensland); Vibhavari Dasagi (Queensland University of Technology); Akansel Cosgun (Monash University); Juxi Leitner (QUT); Peter Corke (Queensland University of Technology)**

#### Interactive Session
<a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SESPC9DRQK9B5B28R" target="_blank" rel="noopener noreferrer"><em>2020-11-18, 11:50 - 12:20 PST </em></a>

#### Abstract
Manipulating deformable objects, such as fabric, is a long standing problem in robotics, with state estimation and control posing a significant challenge for traditional methods. In this paper, we show that it is possible to learn fabric folding skills in only an hour of self-supervised real robot experience, without human supervision or simulation. Our approach relies on fully convolutional networks and the manipulation of visual inputs to exploit learned features, allowing us to create an expressive goal-conditioned pick and place policy that can be trained efficiently with real world robot data only. Folding skills are learned with only a sparse reward function and thus do not require reward function engineering, merely an image of the goal configuration. We demonstrate our method on a set of towel-folding tasks, and show that our approach is able to discover sequential folding strategies, purely from trial-and-error. We achieve state-of-the-art results without the need for demonstrations or simulation, used in prior approaches.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1b-uxESDGWVVdujlZ1cJ8A3Ac_NnDk3yw/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


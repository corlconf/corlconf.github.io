---
layout: page
title: "Learning to Improve Multi-Robot Hallway Navigation"
subtitle: 
description:
permalink: /paper_424/
grand_parent: All Papers
parent: Tuesday
supp: 
code: 
youtube_id: i4QGXfNSJSo
pdf: https://drive.google.com/file/d/12k_ABxmEE62_A6aXsL_ZS1ESjeNtK0Qr/view
---

# Learning to Improve Multi-Robot Hallway Navigation

<a href="https://drive.google.com/file/d/12k_ABxmEE62_A6aXsL_ZS1ESjeNtK0Qr/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Jin Soo Park (The University of Texas at Austin)*; Brian Tsang (University of Texas at Austin); Harel Yedidsion (UT Austin); Garrett Warnell (US Army Research Lab); Daehyun Kyoung (The University of Texas at Austin); Peter Stone (University of Texas at Austin and Sony AI)**

#### Interactive Session
<em>2020-11-17, 11:50 - 12:20 PST </em> | <a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SES4BXQBFPM6C5C0P" target="_blank" rel="noopener noreferrer"> PheedLoop Session <i class="fa fa-external-link" aria-hidden="true"></i> </a> 

#### Abstract
As multi-robot applications become more prevalent, it becomes necessary to develop navigation systems which allow autonomous mobile robots to efficiently and safely pass each other in confined spaces. Existing navigation systems, such as the widely used ROS Navigation Stack, usually produce safe, collision free paths in static environments. However, these systems are not perfect, and when multiple mobile robots simultaneously navigate in narrow spaces, collisions and turnarounds are not uncommon. Fine-tuning and enhancing such navigation stacks is not as simple as it looks since they are made up of multiple layers of code, and there exists a tradeoff between optimizing for efficiency, i.e. minimizing time to destination (TTD) vs. optimizing for safety, i.e. minimizing collisions, with each objective leading to a different combination of parameter values. In this paper we develop a methodology to improve existing navigation stacks with regards to both objectives, without tuning their parameters, while preserving their inherent safety control properties. Our proposed approach is a decentralized learning-based approach that is geared toward real world robotic deployment, by requiring little computing resources. It is agnostic of the underlying navigation stack and can adapt to different types of environmental layouts (i.e., hallway structures).

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1guMxAc-CeX1jUeBn-5uv3gpqVnCYl9mb/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


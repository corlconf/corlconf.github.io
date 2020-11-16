---
layout: page
title: "Belief-Grounded Networks for Accelerated Robot Learning under Partial Observability"
subtitle: 
description:
permalink: /paper_364/
grand_parent: All Papers
parent: Wednesday
supp: 
code: https://github.com/hai-h-nguyen/belief-grounded-network
youtube_id: 
pdf: https://drive.google.com/file/d/1uLbHW9VgbgvD_QKHUbY1UB2zbOREFm7B/view
---

# Belief-Grounded Networks for Accelerated Robot Learning under Partial Observability

<a href="https://drive.google.com/file/d/1uLbHW9VgbgvD_QKHUbY1UB2zbOREFm7B/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="https://github.com/hai-h-nguyen/belief-grounded-network" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Hai Nguyen (Northeastern University)*; Brett Daley (Northeastern University); Xinchao Song (Northeastern University); Christopher Amato (Northeastern University); Robert Platt (Northeastern University)**

#### Interactive Session
<em>2020-11-18, 11:10 - 11:40 PST </em> | <a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SESARRVX7M3EN8WN2" target="_blank" rel="noopener noreferrer"> PheedLoop Session <i class="fa fa-external-link" aria-hidden="true"></i> </a> 

#### Abstract
Many important robotics problems are partially observable where a single visual or force-feedback measurement is insufficient to reconstruct the state. Standard approaches involve learning a policy over beliefs or observation-action histories.    However, both of these have drawbacks; it is expensive to track the belief online, and it is hard to learn policies directly over histories. We propose a method for policy learning under partial observability called the Belief-Grounded Network (BGN) in which an auxiliary belief-reconstruction loss incentivizes a neural network to concisely summarize its input history. Since the resulting policy is a function of the history rather than the belief, it can be executed easily at runtime. We compare BGN against several baselines on classic benchmark tasks as well as three novel robotic force-feedback tasks. BGN outperforms all other tested methods and its learned policies work well when transferred onto a physical robot.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1iLJIY5OCNQdA7MYiT9K_NDiqmG0c6bpm/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


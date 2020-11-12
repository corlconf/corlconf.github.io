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
youtubeId: 
---

# Belief-Grounded Networks for Accelerated Robot Learning under Partial Observability

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1uLbHW9VgbgvD_QKHUbY1UB2zbOREFm7B/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Hai Nguyen (Northeastern University)*; Brett Daley (Northeastern University); Xinchao Song (Northeastern University); Christopher Amato (Northeastern University); Robert Platt (Northeastern University)**

#### Abstract
Many important robotics problems are partially observable where a single visual or force-feedback measurement is insufficient to reconstruct the state. Standard approaches involve learning a policy over beliefs or observation-action histories.    However, both of these have drawbacks; it is expensive to track the belief online, and it is hard to learn policies directly over histories. We propose a method for policy learning under partial observability called the Belief-Grounded Network (BGN) in which an auxiliary belief-reconstruction loss incentivizes a neural network to concisely summarize its input history. Since the resulting policy is a function of the history rather than the belief, it can be executed easily at runtime. We compare BGN against several baselines on classic benchmark tasks as well as three novel robotic force-feedback tasks. BGN outperforms all other tested methods and its learned policies work well when transferred onto a physical robot.

#### Video 

#### Reviews

#### Rebuttal

---
layout: page
title: "Time-Bounded Mission Planning in Time-Varying Domains with Semi-MDPs and Gaussian Processes"
subtitle: 
description:
permalink: /paper_368/
grand_parent: All Papers
parent: Tuesday
supp: 
code: 
youtube_id: 
pdf: https://drive.google.com/file/d/1UlA5pxn6hE2zGdkCGnP25jxPVx-GhplA/view
---

# Time-Bounded Mission Planning in Time-Varying Domains with Semi-MDPs and Gaussian Processes

<a href="https://drive.google.com/file/d/1UlA5pxn6hE2zGdkCGnP25jxPVx-GhplA/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Paul Duckworth (University of Oxford)*; Bruno Lacerda (University of Oxford); Nick Hawes (Oxford Robotics Institute)**

#### Interactive Session
<em>2020-11-17, 11:50 - 12:20 PST </em> | <a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SESVUZKJKD2LGFFL7" target="_blank" rel="noopener noreferrer"> PheedLoop Session <i class="fa fa-external-link" aria-hidden="true"></i> </a> 

#### Abstract
Uncertain, time-varying dynamic environments are ubiquitous in real world robotics. We propose an online planning framework to address time-bounded missions under time-varying dynamics, where those dynamics affect the duration and outcome of actions. We pose such problems as semi-Markov decision processes, where actions have a duration distributed according to an a priori unknown time-varying function. Our approach maintains a belief over this function, and time is propagated through a discrete search tree that efficiently maintains a subset of reachable states. We show improved mission performance on a marine vehicle simulator acting under real-world spatio-temporal ocean currents, and demonstrate the ability to solve co-safe linear temporal logic problems, which are more complex than the reachability problems tackled in previous approaches.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1fbSdzT20juZHKSM4DT0H6xgnfJVu_bmY/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


---
layout: page
title: "Asynchronous Deep Model Reference Adaptive Control"
subtitle: 
description:
permalink: /paper_206/
grand_parent: All Papers
parent: Wednesday
supp: 
code: 
youtube_id: TWlE4ioCd_o
pdf: https://drive.google.com/file/d/1e9rrmapuhqNvWukXTyzf7Xl4KjjkiVXt/view
---

# Asynchronous Deep Model Reference Adaptive Control

<a href="https://drive.google.com/file/d/1e9rrmapuhqNvWukXTyzf7Xl4KjjkiVXt/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Girish Joshi (University of Illinois Urbana-Champaign)*; Jasvir Virdi (University of Illinois at Urbana-Champaign); Girish Chowdhary (University of Illinois at Urbana Champaign)**

#### Interactive Session
<em>2020-11-18, 12:30 - 13:00 PST </em> | <a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SES4AR7HXJ6F9L2BA" target="_blank" rel="noopener noreferrer"> PheedLoop Session <i class="fa fa-external-link" aria-hidden="true"></i> </a> 

#### Abstract
In this paper, we present Asynchronous implementation of Deep Neural Network-based Model Reference Adaptive Control (DMRAC). We evaluate this new neuro-adaptive control architecture through flight tests on a small quadcopter. We demonstrate that a single DMRAC controller can handle significant nonlinearities due to severe system faults and deliberate wind disturbances while executing high-bandwidth attitude control. We also show that the architecture has long-term learning abilities across different flight regimes, and can generalize to fly different flight trajectories than those on which it was trained. These results demonstrating the efficacy of this architecture for high bandwidth closed-loop attitude control of unstable and nonlinear robots operating in adverse situations. To achieve these results, we designed a software+communication architecture to ensure online real-time inference of the deep network on a high-bandwidth computation-limited platform. We expect that this architecture will benefit other deep learning in the closed-loop experiments on robots.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1POSRlv8NA9HmK4EGFn6HK-OqmFoZWSns/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


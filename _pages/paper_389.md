---
layout: page
title: "Unsupervised Metric Relocalization Using Transform Consistency Loss"
subtitle: 
description:
permalink: /paper_389/
grand_parent: All Papers
parent: Wednesday
supp: 
code: 
youtube_id: 5eAIwpXQ7RY
pdf: https://drive.google.com/file/d/14IYZ1oKJT3Uw1K9U8GB_AMcAMX-NqQJr/view
---

# Unsupervised Metric Relocalization Using Transform Consistency Loss

<a href="https://drive.google.com/file/d/14IYZ1oKJT3Uw1K9U8GB_AMcAMX-NqQJr/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Mike Kasper (University of Colorado)*; Fernando Nobre (Amazon); Christoffer Heckman (University of Colorado); Nima Keivan (Amazon)**

#### Interactive Session
*2020-11-18, 11:50 - 12:20 PST* 

#### Abstract
Training networks to perform metric relocalization traditionally requires accurate image correspondences. In practice, these are obtained by restricting domain coverage, employing additional sensors, or capturing large multi-view datasets. We instead propose a self-supervised solution, which exploits a key insight: localizing a query image within a map should yield the same absolute pose, regardless of the reference image used for registration. Guided by this intuition, we derive a novel transform consistency loss. Using this loss function, we train a deep neural network to infer dense feature and saliency maps to perform robust metric relocalization in dynamic environments.  We evaluate our framework on synthetic and real-world data, showing our approach outperforms other supervised methods when a limited amount of ground-truth information is available.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1pYTA-2e_9qR-brkB0ZxhYcloRh0rXNvj/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


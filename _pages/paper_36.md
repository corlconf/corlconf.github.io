---
layout: page
title: "CoT-AMFlow: Adaptive Modulation Network with Co-Teaching Strategy for Unsupervised Optical Flow Estimation"
subtitle: 
description:
permalink: /paper_36/
grand_parent: All Papers
parent: Monday
supp: 
code: https://sites.google.com/view/cot-amflow
youtube_id: 3GlxUZ_NuaQ
pdf: https://drive.google.com/file/d/1ILmJrP87J5qb5lu8lx8yPkLdPD7xpAqX/view
---

# CoT-AMFlow: Adaptive Modulation Network with Co-Teaching Strategy for Unsupervised Optical Flow Estimation

<a href="https://drive.google.com/file/d/1ILmJrP87J5qb5lu8lx8yPkLdPD7xpAqX/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="https://sites.google.com/view/cot-amflow" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Hengli Wang (Hong Kong University of Science and Technology)*; Rui Fan (UC San Diego); Ming Liu (HKUST)**

#### Interactive Session
*2020-11-16, 12:30 - 13:00 PST* 

#### Abstract
The interpretation of ego motion and scene change is a fundamental task for mobile robots. Optical flow information can be employed to estimate motion in the surroundings. Recently, unsupervised optical flow estimation has become a research hotspot.  However, unsupervised approaches are often easy to be unreliable on partially occluded or texture-less regions. To deal with this problem, we propose CoT-AMFlow in this paper, an unsupervised optical flow estimation approach. In terms of the network architecture, we develop an adaptive modulation network that employs two novel module types, flow modulation modules (FMMs) and cost volume modulation modules (CMMs), to remove outliers in challenging regions. As for the training paradigm, we adopt a co-teaching strategy, where two networks simultaneously teach each other about challenging regions to further improve accuracy. Experimental results on the MPI Sintel, KITTI Flow and Middlebury Flow benchmarks demonstrate that our CoT-AMFlow outperforms all other state-of-the-art unsupervised approaches, while still running in real time. Our project page is available at <a href="https://sites.google.com/view/cot-amflow" target="_blank">https://sites.google.com/view/cot-amflow</a>.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


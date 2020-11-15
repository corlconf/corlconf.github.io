---
layout: page
title: "Guaranteeing Safety of Learned Perception Modules via Measurement-Robust Control Barrier Functions"
subtitle: 
description:
permalink: /paper_140/
grand_parent: All Papers
parent: Tuesday
supp: 
code: https://github.com/rkcosner/cyberpod_sim_ros
youtube_id: x7L6Sz2lxOA
pdf: https://drive.google.com/file/d/1b2-B7GqG-pbuBSEgzIsFs6unbaY2rIT9/view
---

# Guaranteeing Safety of Learned Perception Modules via Measurement-Robust Control Barrier Functions

<a href="https://drive.google.com/file/d/1b2-B7GqG-pbuBSEgzIsFs6unbaY2rIT9/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="https://github.com/rkcosner/cyberpod_sim_ros" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Sarah Dean (UC Berkeley)*; Andrew Taylor (Caltech); Ryan Cosner (Caltech); Benjamin Recht (UC Berkeley); Aaron Ames (Caltech)**

#### Interactive Session
*2020-11-17, 11:10 - 11:40 PST* 

#### Abstract
Modern nonlinear control theory seeks to develop feedback controllers that endow systems with properties such as safety and stability. The guarantees ensured by these controllers often rely on accurate estimates of the system state for determining control actions. In practice, measurement model uncertainty can lead to error in state estimates that degrades these guarantees. In this paper, we seek to unify techniques from control theory and machine learning to synthesize controllers that achieve safety in the presence of measurement model uncertainty. We define the notion of a Measurement-Robust Control Barrier Function (MR-CBF) as a tool for determining safe control inputs when facing measurement model uncertainty. Furthermore, MR-CBFs are used to inform sampling methodologies for learning-based perception systems and quantify tolerable error in the resulting learned models. We demonstrate the efficacy of MR-CBFs in achieving safety with measurement model uncertainty on a simulated Segway system.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/17xXZTkTWR_nEcw4pNcJbL_Xx416toSWU/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


---
layout: page
title: "MATS: An Interpretable Trajectory Forecasting Representation for Planning and Control"
subtitle: 
description:
permalink: /paper_499/
grand_parent: All Papers
parent: Tuesday
supp: 
code: 
youtube_id: ZFJKyZ8-MgE
pdf: https://drive.google.com/file/d/1kQ3I2AYhC01Pc-BNBu7I_J54m85H82a-/view
---

# MATS: An Interpretable Trajectory Forecasting Representation for Planning and Control

<a href="https://drive.google.com/file/d/1kQ3I2AYhC01Pc-BNBu7I_J54m85H82a-/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Boris Ivanovic (Stanford University)*; Amine Elhafsi (Stanford University); Guy Rosman (Toyota Research Institute); Adrien Gaidon (Toyota Research Institute); Marco Pavone (Stanford University)**

#### Interactive Session
<a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SES02TIHWDIJQWIMM" target="_blank" rel="noopener noreferrer"><em>2020-11-17, 12:30 - 13:00 PST </em></a>

#### Abstract
Reasoning about human motion is a core component of modern human-robot interactive systems. In particular, one of the main uses of behavior prediction in autonomous systems is to inform robot motion planning and control. However, a majority of planning and control algorithms reason about system dynamics rather than the predicted agent tracklets (i.e., ordered sets of waypoints) that are commonly output by trajectory forecasting methods, which can hinder their integration. Towards this end, we propose Mixtures of Affine Time-varying Systems (MATS) as an output representation for trajectory forecasting that is more amenable to downstream planning and control use. Our approach leverages successful ideas from probabilistic trajectory forecasting works to learn dynamical system representations that are well-studied in the planning and control literature. We integrate our predictions with a proposed multimodal planning methodology and demonstrate significant computational efficiency improvements on a large-scale autonomous driving dataset.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1MaaE7xAuwTP8fDfrvYaxTViiTtIrE772/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


---
layout: page
title: "Deep Phase Correlation for End-to-End Heterogeneous Sensor Measurements Matching"
subtitle: 
description:
permalink: /paper_530/
grand_parent: All Papers
parent: Monday
supp: 
code: https://github.com/jessychen1016/DPCN
youtube_id: 
pdf: https://drive.google.com/file/d/1SmAayWXB2J5A2AkgwNB-yyejxAjG-6HH/view
---

# Deep Phase Correlation for End-to-End Heterogeneous Sensor Measurements Matching

<a href="https://drive.google.com/file/d/1SmAayWXB2J5A2AkgwNB-yyejxAjG-6HH/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="https://github.com/jessychen1016/DPCN" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Zexi Chen (Zhejiang University); Xuecheng Xu (Zhejiang University); Yue Wang (Zhejiang University)*; Rong Xiong (Zhejiang University)**

#### Interactive Session
*2020-11-16, 12:30 - 13:00 PST* 

#### Abstract
The crucial step for localization is to match the current observation to the map. When the two sensor modalities are significantly different, matching becomes challenging. In this paper, we present an end-to-end deep phase correlation network (DPCN) to match heterogeneous sensor measurements. In DPCN, the primary component is a differentiable correlation-based estimator that back-propagates the pose error to learnable feature extractors, which addresses the problem that there are no direct common features for supervision. In addition, it eliminates the exhaustive evaluation in some previous methods, improving efficiency. With the interpretable modeling, the network is light-weighted and promising for better generalization. We evaluate the system on both the simulation data and Aero-Ground Dataset which consists of heterogeneous sensor images and aerial images acquired by satellites or aerial robots. The results show that our method is able to match the heterogeneous sensor measurements, outperforming the comparative traditional phase correlation and other learning-based methods. Code is available at <a href="https://github.com/jessychen1016/DPCN" target="_blank">https://github.com/jessychen1016/DPCN</a>.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/19hjMXJgqxjIejUD1bn_JD3CKYHSZ-IUE/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


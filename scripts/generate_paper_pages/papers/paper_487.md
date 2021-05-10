---
layout: page
title: "Attentional Separation-and-Aggregation Network for Self-supervised Depth-Pose Learning in Dynamic Scenes"
subtitle: 
description:
permalink: /paper_487/
grand_parent: All Papers
parent: Tuesday
supp: 
code: 
youtube_id: LGAw_nVD8MA
pdf: https://drive.google.com/file/d/1YJqIyvliAnBM3BYiOcewm8WdF1UN2Lcm/view
---

# Attentional Separation-and-Aggregation Network for Self-supervised Depth-Pose Learning in Dynamic Scenes

<a href="https://drive.google.com/file/d/1YJqIyvliAnBM3BYiOcewm8WdF1UN2Lcm/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Feng Gao (Tsinghua University)*; Jincheng Yu (Tsinghua University); Hao Shen (Meituan); Yu Wang (Tsinghua University); Huazhong Yang (Tsinghua University)**

#### Interactive Session
<em>2020-11-17, 11:10 - 11:40 PST </em> | <a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SES1GY13LZD45FCWR" target="_blank" rel="noopener noreferrer"> PheedLoop Session <i class="fa fa-external-link" aria-hidden="true"></i> </a> 

#### Abstract
Learning depth and ego-motion from unlabeled videos via self-supervision from epipolar projection can improve the robustness and accuracy of the 3D perception and localization of vision-based robots. However, the rigid projection computed by ego-motion cannot represent all scene points, such as points on moving objects, leading to false guidance in these regions. To address this problem, we propose an Attentional Separation-and-Aggregation Network (ASANet), which can learn to distinguish and extract the scene's static and dynamic characteristics via the attention mechanism. We further propose a novel MotionNet with an ASANet as the encoder, followed by two separate decoders, to estimate the camera's ego-motion and the scene's dynamic motion field. Then, we introduce an auto-selecting approach to detect the moving objects for dynamic-aware learning automatically. Empirical experiments demonstrate that our method can achieve the state-of-the-art performance on the KITTI benchmark.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


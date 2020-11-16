---
layout: page
title: "Visual Localization and Mapping with Hybrid SFA"
subtitle: 
description:
permalink: /paper_267/
grand_parent: All Papers
parent: Tuesday
supp: 
code: 
youtube_id: RZ8aVVRmKRg
pdf: https://drive.google.com/file/d/1nOPmetmFFdceWi7h-D2F4vJg0Hw48-5Z/view
---

# Visual Localization and Mapping with Hybrid SFA

<a href="https://drive.google.com/file/d/1nOPmetmFFdceWi7h-D2F4vJg0Hw48-5Z/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Muhammad Haris (Frankfurt University of Applied Sciences)*; Mathias Franzius (Honda Research Institute Europe GmbH); Ute Bauer-Wersing (Frankfurt University of Applied Sciences); Sai Krishna Kaushik Karanam  (Frankfurt University of Applied Sciences)**

#### Interactive Session
<a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SES4FME4FAGV6YPNN" target="_blank" rel="noopener noreferrer"><em>2020-11-17, 11:10 - 11:40 PST </em></a>

#### Abstract
Visual localization is a crucial requirement in mobile robotics, field and service robotics, and self-driving cars. Recently, unsupervised learning with Slow Feature Analysis (SFA) has shown to produce spatial representations that enable localization from holistic images. The approach is faster and much less complex than state-of-the-art monocular visual SLAM methods while achieving similar localization performance in small-scale environments. However, the holistic approach's performance drops significantly for highly complex, large-scale environments due to scene variations occurring during a training phase. Instead of using holistic images, an alternative is to perform localization relative to unique regions present in a scene. Therefore, in this paper, we add a new component to the SFA localization pipeline that leverages state-of-the-art CNN to identify unique image regions. Hence we propose a hybrid approach that first learns such regions with a pre-trained CNN and then uses SFA for unsupervised pose estimation relative to each region. We present the experimental results from an autonomous robot in two different outdoor environments of varying complexity and size. The experiments show the proposed hybrid approach outperforms holistic SFA w.r.t localization accuracy in both environments, but benefits are more pronounced in the large-scale environment. 

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1lzZtED3G1jCB8nScar6nAyr9-3G7_Sil/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


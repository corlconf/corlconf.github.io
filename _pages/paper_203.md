---
layout: page
title: "Contrastive Variational Reinforcement Learning for Complex Observations"
subtitle: 
description:
permalink: /paper_203/
grand_parent: All Papers
parent: Wednesday
supp: 
code: https://github.com/Yusufma03/CVRL
youtube_id: 
pdf: https://drive.google.com/file/d/1A7DE9xPwZJjnPh_qol8gJW0RFWBlYyG3/view
---

# Contrastive Variational Reinforcement Learning for Complex Observations

<a href="https://drive.google.com/file/d/1A7DE9xPwZJjnPh_qol8gJW0RFWBlYyG3/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="https://github.com/Yusufma03/CVRL" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Xiao Ma (National University of Singapore)*; SIWEI CHEN (National University of Singapore); David Hsu (NUS); Wee Sun Lee (National University of Singapore)**

#### Interactive Session
<a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SESHFCYOAQYDAR0VB" target="_blank" rel="noopener noreferrer"><em>2020-11-18, 12:30 - 13:00 PST </em></a>

#### Abstract
Deep reinforcement learning (DRL) has achieved significant success in various robot tasks: manipulation, navigation, etc. However, complex visual observations in natural environments remains a major challenge. This paper presents Contrastive Variational Reinforcement Learning (CVRL), a model-based method that tackles complex visual observations in  DRL.  CVRL learns a contrastive variational model by maximizing the mutual information between latent states and observations discriminatively, through contrastive learning. It avoids modeling the complex observation space unnecessarily, as the commonly used generative observation model often does,  and is significantly more robust. CVRL achieves comparable performance with state-of-the-art model-based DRL methods on standard Mujoco tasks. It significantly outperforms them on Natural Mujoco tasks and a robot box-pushing task with complex observations, e.g., dynamic shadows. The CVRL code is available publicly at <a href="https://github.com/Yusufma03/CVRL" target="_blank">https://github.com/Yusufma03/CVRL</a>.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1iAcvTSzGPihdgXucUx4j-7Ac44hbhX_I/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


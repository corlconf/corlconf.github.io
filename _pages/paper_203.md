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
youtubeId: 
---

# Contrastive Variational Reinforcement Learning for Complex Observations

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1A7DE9xPwZJjnPh_qol8gJW0RFWBlYyG3/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Xiao Ma (National University of Singapore)*; SIWEI CHEN (National University of Singapore); David Hsu (NUS); Wee Sun Lee (National University of Singapore)**

#### Abstract
Deep reinforcement learning (DRL) has achieved significant success in various robot tasks: manipulation, navigation, etc. However, complex visual observations in natural environments remains a major challenge. This paper presents Contrastive Variational Reinforcement Learning (CVRL), a model-based method that tackles complex visual observations in  DRL.  CVRL learns a contrastive variational model by maximizing the mutual information between latent states and observations discriminatively, through contrastive learning. It avoids modeling the complex observation space unnecessarily, as the commonly used generative observation model often does,  and is significantly more robust. CVRL achieves comparable performance with state-of-the-art model-based DRL methods on standard Mujoco tasks. It significantly outperforms them on Natural Mujoco tasks and a robot box-pushing task with complex observations, e.g., dynamic shadows. The CVRL code is available publicly at <a href="https://github.com/Yusufma03/CVRL" target="_blank">https://github.com/Yusufma03/CVRL</a>.

#### Video 

#### Reviews

#### Rebuttal

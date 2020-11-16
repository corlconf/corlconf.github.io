---
layout: page
title: "PLAS: Latent Action Space for Offline Reinforcement Learning"
subtitle: 
description:
permalink: /paper_386/
grand_parent: All Papers
parent: Wednesday
supp: 
code: https://github.com/Wenxuan-Zhou/PLAS
youtube_id: Hpke10yRwVk
pdf: https://drive.google.com/file/d/1zmL1sLnEqFv2lSNqdqJpjE8V7gUtaOMa/view
---

# PLAS: Latent Action Space for Offline Reinforcement Learning

<a href="https://drive.google.com/file/d/1zmL1sLnEqFv2lSNqdqJpjE8V7gUtaOMa/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="https://github.com/Wenxuan-Zhou/PLAS" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Wenxuan Zhou (Carnegie Mellon University)*; Sujay Bajracharya (Carnegie Mellon University); David Held (CMU)**

#### Interactive Session
<em>2020-11-18, 11:10 - 11:40 PST </em> | <a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SESNL7FZR03IQDGVC" target="_blank" rel="noopener noreferrer"> PheedLoop Session <i class="fa fa-external-link" aria-hidden="true"></i> </a> 

#### Abstract
The goal of offline reinforcement learning is to learn a policy from a fixed dataset, without further interactions with the environment. This setting will be an increasingly more important paradigm for real-world applications of reinforcement learning such as robotics, in which data collection is slow and potentially dangerous. Existing off-policy algorithms have limited performance on static datasets due to extrapolation errors from out-of-distribution actions. This leads to the challenge of constraining the policy to select actions within the support of the dataset during training. We propose to simply learn the Policy in the Latent Action Space (PLAS) such that this requirement is naturally satisfied. We evaluate our method on continuous control benchmarks in simulation and a deformable object manipulation task with a physical robot. We demonstrate that our method provides competitive performance consistently across various continuous control tasks and different types of datasets, outperforming existing offline reinforcement learning methods with explicit constraints.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1P9zA19ylL8BT0xlbQlgBlSANhyv3m6Cf/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


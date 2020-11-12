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
youtubeId: 
---

# PLAS: Latent Action Space for Offline Reinforcement Learning

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1zmL1sLnEqFv2lSNqdqJpjE8V7gUtaOMa/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Wenxuan Zhou (Carnegie Mellon University)*; Sujay Bajracharya (Carnegie Mellon University); David Held (CMU)**

#### Abstract
The goal of offline reinforcement learning is to learn a policy from a fixed dataset, without further interactions with the environment. This setting will be an increasingly more important paradigm for real-world applications of reinforcement learning such as robotics, in which data collection is slow and potentially dangerous. Existing off-policy algorithms have limited performance on static datasets due to extrapolation errors from out-of-distribution actions. This leads to the challenge of constraining the policy to select actions within the support of the dataset during training. We propose to simply learn the Policy in the Latent Action Space (PLAS) such that this requirement is naturally satisfied. We evaluate our method on continuous control benchmarks in simulation and a deformable object manipulation task with a physical robot. We demonstrate that our method provides competitive performance consistently across various continuous control tasks and different types of datasets, outperforming existing offline reinforcement learning methods with explicit constraints.

#### Video 

#### Reviews

#### Rebuttal

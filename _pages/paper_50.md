---
layout: page
title: "Task-Relevant Adversarial Imitation Learning"
subtitle: 
description:
permalink: /paper_50/
grand_parent: All Papers
parent: Monday
supp: 
code: 
youtubeId: 
---

# Task-Relevant Adversarial Imitation Learning

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1Mj4Tm3fnnRkQTwLelsCCCj_7SAd7g1Yt/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Konrad Zolna (DeepMind)*; Scott Reed (DeepMind); Alexander Novikov (DeepMind); Sergio Gómez Colmenarejo (DeepMind); David Budden (DeepMind); Serkan Cabi (DeepMind); Misha Denil (DeepMind); Nando de Freitas (DeepMind); Ziyu Wang (Google Research, Brain Team)**

#### Abstract
We show that a critical vulnerability in adversarial imitation is the tendency of discriminator networks to learn spurious associations between visual features and expert labels. When the discriminator focuses on task-irrelevant features, it does not provide an informative reward signal, leading to poor task performance. We analyze this problem in detail and propose a solution that outperforms standard Generative Adversarial Imitation Learning (GAIL). Our proposed method, Task-Relevant Adversarial Imitation Learning (TRAIL), uses constrained discriminator optimization to learn informative rewards. In comprehensive experiments, we show that TRAIL can solve challenging robotic manipulation tasks from pixels by imitating human operators without access to any task rewards, and clearly outperforms comparable baseline imitation agents, including those trained via behaviour cloning and conventional GAIL.

#### Video 

#### Reviews

#### Rebuttal

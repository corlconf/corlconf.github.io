---
layout: page
title: "Learning from Suboptimal Demonstration via Self-Supervised Reward Regression"
subtitle: 
description:
permalink: /paper_281/
grand_parent: All Papers
parent: Tuesday
supp: 
code: 
youtubeId: 
---

# Learning from Suboptimal Demonstration via Self-Supervised Reward Regression

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1wmN00JKqxvbm4C1Li6e3l4m6nycFgMYb/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Letian Chen (Georgia Institute of Technology)*; Rohan Paleja (Georgia Institute of Technology); Matthew Gombolay (Georgia Institute of Technology)**

#### Abstract
Learning from Demonstration (LfD) seeks to democratize robotics by enabling non-roboticist end-users to teach robots to perform a task by providing a human demonstration. However, modern LfD techniques, e.g. inverse reinforcement learning (IRL), assume users provide at least stochastically optimal demonstrations. This assumption fails to hold in most real-world scenarios. Recent attempts to learn from sub-optimal demonstration leverage pairwise rankings and following the Luce-Shepard rule. However, we show these approaches make incorrect assumptions and thus suffer from brittle, degraded performance. We overcome these limitations in developing a novel approach that bootstraps off suboptimal demonstrations to synthesize optimality-parameterized data to train an idealized reward function. We empirically validate we learn an idealized reward function with ~0.95 correlation with ground-truth reward versus  ~0.75 for prior work. We can then train policies achieving ~200% improvement over the suboptimal demonstration and ~90% improvement over prior work. We present a physical demonstration of teaching a robot a topspin strike in table tennis that achieves 32% faster returns and 40% more topspin than user demonstration.

#### Video 

#### Reviews

#### Rebuttal

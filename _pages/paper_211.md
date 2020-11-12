---
layout: page
title: "Probably Approximately Correct Vision-Based Planning using Motion Primitives"
subtitle: 
description:
permalink: /paper_211/
grand_parent: All Papers
parent: Wednesday
supp: 
code: https://github.com/irom-lab/PAC-Vision-Planning
youtubeId: 
---

# Probably Approximately Correct Vision-Based Planning using Motion Primitives

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1CS6DL-BcQVhtZIY39rLc-aTr64Jq8vp2/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Sushant Veer (Princeton University)*; Anirudha Majumdar (Princeton University)**

#### Interactive Session
*2020-11-18, 11:50 - 12:20 PST*

#### Abstract
This paper presents an approach for learning vision-based planners that provably generalize to novel environments (i.e., environments unseen during training). We leverage the Probably Approximately Correct (PAC)-Bayes framework to obtain an upper bound on the expected cost of policies across all environments. Minimizing the PAC-Bayes upper bound thus trains policies that are accompanied by a certificate of performance on novel environments. The training pipeline we propose provides strong generalization guarantees for deep neural network policies by (a) obtaining a good prior distribution on the space of policies using Evolutionary Strategies (ES) followed by (b) formulating the PAC-Bayes optimization as an efficiently-solvable parametric convex optimization problem. We demonstrate the efficacy of our approach for producing strong generalization guarantees for learned vision-based motion planners through two simulated examples: (1) an Unmanned Aerial Vehicle (UAV) navigating obstacle fields with an onboard vision sensor, and (2) a dynamic quadrupedal robot traversing rough terrains with proprioceptive and exteroceptive sensors.

#### Video 

#### Reviews

#### Rebuttal

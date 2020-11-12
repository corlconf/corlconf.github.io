---
layout: page
title: "Learning Stability Certificates from Data"
subtitle: 
description:
permalink: /paper_290/
grand_parent: All Papers
parent: Tuesday
supp: 
code: 
youtubeId: 
---

# Learning Stability Certificates from Data

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1W9mC4CWT1tFJGWZC0lKeDwFLnfIifxjM/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Nicholas Boffi (Harvard University); Stephen Tu (Google)*; Nikolai Matni (University of Pennsylvania); Jean-Jacques Slotine (MIT); Vikas Sindhwani (Google)**

#### Abstract
Many existing tools in nonlinear control theory for establishing stability or safety of a dynamical system can be distilled to the construction of a certificate function which guarantees a desired property. However, algorithms for synthesizing certificate functions typically require a closed-form analytical expression of the underlying dynamics, which rules out their use on many modern robotic platforms. To circumvent this issue, we develop algorithms for learning certificate functions only from trajectory data. We establish bounds on the generalization error - the probability that a certificate will not certify a new, unseen trajectory - when learning from trajectories, and we convert such generalization error bounds into global stability guarantees. We demonstrate empirically that certificates for complex dynamics can be efficiently learned, and that the learned certificates can be used for downstream tasks such as adaptive control.

#### Video 

#### Reviews

#### Rebuttal

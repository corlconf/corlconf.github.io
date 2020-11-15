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
youtube_id: 
pdf: https://drive.google.com/file/d/1W9mC4CWT1tFJGWZC0lKeDwFLnfIifxjM/view
---

# Learning Stability Certificates from Data

<a href="https://drive.google.com/file/d/1W9mC4CWT1tFJGWZC0lKeDwFLnfIifxjM/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Nicholas Boffi (Harvard University); Stephen Tu (Google)*; Nikolai Matni (University of Pennsylvania); Jean-Jacques Slotine (MIT); Vikas Sindhwani (Google)**

#### Interactive Session
*2020-11-17, 12:30 - 13:00 PST* 

#### Abstract
Many existing tools in nonlinear control theory for establishing stability or safety of a dynamical system can be distilled to the construction of a certificate function which guarantees a desired property. However, algorithms for synthesizing certificate functions typically require a closed-form analytical expression of the underlying dynamics, which rules out their use on many modern robotic platforms. To circumvent this issue, we develop algorithms for learning certificate functions only from trajectory data. We establish bounds on the generalization error - the probability that a certificate will not certify a new, unseen trajectory - when learning from trajectories, and we convert such generalization error bounds into global stability guarantees. We demonstrate empirically that certificates for complex dynamics can be efficiently learned, and that the learned certificates can be used for downstream tasks such as adaptive control.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1Z_1ZixaST6eFxAqZRaRHQUm3r-bJot4v/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


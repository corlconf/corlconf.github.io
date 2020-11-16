---
layout: page
title: "ContactNets: Learning Discontinuous Contact Dynamics with Smooth, Implicit Representations"
subtitle: 
description:
permalink: /paper_506/
grand_parent: All Papers
parent: Monday
supp: 
code: https://github.com/DAIRLab/contact-nets
youtube_id: ir6Gdmi9s4A
pdf: https://drive.google.com/file/d/1X67-j0xG-92MDLvv7w8FHGXrIdkGmy-8/view
---

# ContactNets: Learning Discontinuous Contact Dynamics with Smooth, Implicit Representations

<a href="https://drive.google.com/file/d/1X67-j0xG-92MDLvv7w8FHGXrIdkGmy-8/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="https://github.com/DAIRLab/contact-nets" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Samuel Pfrommer (University of Pennsylvania); Mathew Halm (University of Pennsylvania)*; Michael Posa (University of Pennsylvania)**

#### Interactive Session
<a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SESDKK6NB9PPDRMVU" target="_blank" rel="noopener noreferrer"><em>2020-11-16, 11:10 - 11:40 PST </em></a>

#### Abstract
Common methods for learning robot dynamics assume motion is continuous, causing unrealistic model predictions for systems undergoing discontinuous impact and stiction behavior. In this work, we resolve this conflict with a smooth, implicit encoding of the structure inherent to contact-induced discontinuities. Our method, ContactNets, learns parameterizations of inter-body signed distance and contact-frame Jacobians, a representation that is compatible with many simulation, control, and planning environments for robotics. We furthermore circumvent the need to differentiate through stiff or non-smooth dynamics with a novel loss function inspired by the principles of complementarity and maximum dissipation. Our method can predict realistic impact, non-penetration, and stiction when trained on 60 seconds of real-world data.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1034c36z6XdFmMXURoremDgEP5t3Rcc69/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


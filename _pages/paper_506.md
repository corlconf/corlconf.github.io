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
youtubeId: 
---

# ContactNets: Learning Discontinuous Contact Dynamics with Smooth, Implicit Representations

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1X67-j0xG-92MDLvv7w8FHGXrIdkGmy-8/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Samuel Pfrommer (University of Pennsylvania); Mathew Halm (University of Pennsylvania)*; Michael Posa (University of Pennsylvania)**

#### Interactive Session
*2020-11-16, 11:10 - 11:40 PST*

#### Abstract
Common methods for learning robot dynamics assume motion is continuous, causing unrealistic model predictions for systems undergoing discontinuous impact and stiction behavior. In this work, we resolve this conflict with a smooth, implicit encoding of the structure inherent to contact-induced discontinuities. Our method, ContactNets, learns parameterizations of inter-body signed distance and contact-frame Jacobians, a representation that is compatible with many simulation, control, and planning environments for robotics. We furthermore circumvent the need to differentiate through stiff or non-smooth dynamics with a novel loss function inspired by the principles of complementarity and maximum dissipation. Our method can predict realistic impact, non-penetration, and stiction when trained on 60 seconds of real-world data.

#### Video 

#### Reviews

#### Rebuttal

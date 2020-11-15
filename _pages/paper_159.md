---
layout: page
title: "Action-Conditional Recurrent Kalman Networks For Forward and Inverse Dynamics Learning"
subtitle: 
description:
permalink: /paper_159/
grand_parent: All Papers
parent: Wednesday
supp: 
code: 
youtube_id: fNHtSqLYLFs
pdf: https://drive.google.com/file/d/1pyzHYRa0iRYSh-TTZLJ2CF2YlbO7BUqq/view
---

# Action-Conditional Recurrent Kalman Networks For Forward and Inverse Dynamics Learning

<a href="https://drive.google.com/file/d/1pyzHYRa0iRYSh-TTZLJ2CF2YlbO7BUqq/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Vaisakh Shaj (Karlsruhe Institute Of Technology)*; Philipp Becker (Karlsruhe Institute of Technology (KIT)); Dieter Büchler (MPI for Intelligent Systems Tübingen); Harit Pandya (University of Lincoln); Niels van Duijkeren (Bosch Corporate Research); C. James  Taylor (Lancaster University); Marc Hanheide (University of Lincoln); Gerhard Neumann (KIT)**

#### Interactive Session
*2020-11-18, 11:10 - 11:40 PST* 

#### Abstract
Estimating accurate forward and inverse dynamics models is a crucial component of model-based control for sophisticated robots such as robots driven by hydraulics, artificial muscles, or robots dealing with different contact situations.
Analytic models to such processes are often unavailable or inaccurate due to complex hysteresis effects, unmodelled friction and stiction phenomena, and unknown effects during contact situations. A promising approach is to obtain spatio-temporal models in a data-driven way using recurrent neural networks, as they can overcome those issues. However, such models often do not meet accuracy demands sufficiently, degenerate in performance for the required high sampling frequencies and cannot provide uncertainty estimates.  

We adopt a recent probabilistic recurrent neural network architecture, called Recurrent Kalman Networks (RKNs), to model learning by conditioning its transition dynamics on the control actions. RKNs outperform standard recurrent networks such as LSTMs on many state estimation tasks.Inspired by Kalman filters, the RKN provides an elegant way to achieve action conditioning within its recurrent cell by leveraging additive interactions between the current latent state and the action variables. We present two architectures, one for forward model learning and one for inverse model learning. Both architectures significantly outperform existing model learning frameworks as well as analytical models in terms of prediction performance on a variety of real robot dynamics models.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1Tr0DU5p2mI5tmDlH3EjyBTMq3IpWfKQv/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


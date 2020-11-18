---
layout: page
title: "Robot Action Selection Learning via Layered Dimension Informed Program Synthesis"
subtitle: 
description:
permalink: /paper_331/
grand_parent: All Papers
parent: Wednesday
supp: 
code: 
youtube_id: 5ci0PrbD5cs
pdf: https://drive.google.com/file/d/1yfQSu1JA_s5fhwQ3DmcoHy6gecegqQwh/view
---

# Robot Action Selection Learning via Layered Dimension Informed Program Synthesis

<a href="https://drive.google.com/file/d/1yfQSu1JA_s5fhwQ3DmcoHy6gecegqQwh/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Jarrett Holtz (Univ of Texas)*; Arjun Guha (Northeastern University); Joydeep Biswas (University of Texas at Austin)**

#### Interactive Session
<em>2020-11-18, 11:50 - 12:20 PST </em> | <a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SESCA9KH19MJ4Z9RY" target="_blank" rel="noopener noreferrer"> PheedLoop Session <i class="fa fa-external-link" aria-hidden="true"></i> </a> 

#### Abstract
Action selection policies (ASPs), used to compose low-level robot
skills into complex high-level tasks are commonly represented as neural networks
(NNs) in the state of the art. Such a paradigm, while very effective, suffers from
a few key problems: 1) NNs are opaque to the user and hence not amenable to
verification, 2) they require significant amounts of training data, and 3) they are
hard to repair when the domain changes. We present two key insights about ASPs
for robotics. First, ASPs need to reason about physically meaningful quantities
derived from the state of the world, and second, there exists a layered structure
for composing these policies. Leveraging these insights, we introduce layered
dimension-informed program synthesis (LDIPS) – by reasoning about the physical
dimensions of state variables, and dimensional constraints on operators, LDIPS
directly synthesizes ASPs in a human-interpretable domain-specific language that
is amenable to program repair. We present empirical results to demonstrate that
LDIPS 1) can synthesize effective ASPs for robot soccer and autonomous driving domains, 2) requires two orders of magnitude fewer training examples than a
comparable NN representation, and 3) can repair the synthesized ASPs with only
a small number of corrections when transferring from simulation to real robots.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1HSB3mnv7C3u1HWFS1k529UTDblBBHwbh/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


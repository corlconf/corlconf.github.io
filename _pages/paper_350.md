---
layout: page
title: "DIRL: Domain-Invariant Representation Learning for Sim-to-Real Transfer"
subtitle: 
description:
permalink: /paper_350/
grand_parent: All Papers
parent: Tuesday
supp: 
code: https://github.com/ajaytanwani/DIRL
youtube_id: 
pdf: https://drive.google.com/file/d/1pWcLD07dhLrtsJwhArg6w6AYfuYmSSpb/view
---

# DIRL: Domain-Invariant Representation Learning for Sim-to-Real Transfer

<a href="https://drive.google.com/file/d/1pWcLD07dhLrtsJwhArg6w6AYfuYmSSpb/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="https://github.com/ajaytanwani/DIRL" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Ajay Tanwani (UC Berkeley)***

#### Interactive Session
<a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SESQBNS2C0Y2SYHTL" target="_blank" rel="noopener noreferrer"><em>2020-11-17, 11:10 - 11:40 PST </em></a>

#### Abstract
Generating large-scale synthetic data in simulation is a feasible alternative to collecting/labelling real data for training vision-based deep learning models, albeit the modelling inaccuracies do not generalize to the physical world. In this paper, we present a domain-invariant representation learning (DIRL) algorithm to adapt deep models to the physical environment with a small amount of real data. Existing approaches that only mitigate the covariate shift by aligning the marginal distributions across the domains and assume the conditional distributions to be domain-invariant can lead to ambiguous transfer in real scenarios. We propose to jointly align the marginal (input domains) and the conditional (output labels) distributions to mitigate the covariate and the conditional shift across the domains with adversarial learning, and combine it with a triplet distribution loss to make the conditional distributions disjoint in the shared feature space. Experiments on digit domains yield state-of-the-art performance on challenging benchmarks, while sim-to-real transfer of object recognition for vision-based decluttering with a mobile robot improves from 26.8% to 91.0%, resulting in 86.5% grasping accuracy of a wide variety of objects. Code and supplementary details are available at: <a href="https://sites.google.com/view/dirl" target="_blank">https://sites.google.com/view/dirl</a>

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1TqOhyrpkJiCXbTywwcuS81fXiaplAp3I/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


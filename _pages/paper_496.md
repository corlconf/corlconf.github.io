---
layout: page
title: "Harnessing Distribution Ratio Estimators for Learning Agents with Quality and Diversity"
subtitle: 
description:
permalink: /paper_496/
grand_parent: All Papers
parent: Monday
supp: https://drive.google.com/file/d/156UKwuWjQecm72HFZot6ZlX9oxJICgQv/view
code: https://github.com/tgangwani/QDAgents
youtube_id: VeiJupkUzAM
pdf: https://drive.google.com/file/d/19pkVtyd0tFpNehomYRpskevGf6uvBKTb/view
---

# Harnessing Distribution Ratio Estimators for Learning Agents with Quality and Diversity

<a href="https://drive.google.com/file/d/19pkVtyd0tFpNehomYRpskevGf6uvBKTb/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="https://drive.google.com/file/d/156UKwuWjQecm72HFZot6ZlX9oxJICgQv/view" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="https://github.com/tgangwani/QDAgents" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Tanmay Gangwani (University of Illinois, Urbana Champaign)*; Jian Peng (University of Illinois at Urbana-Champaign); Yuan Zhou (UIUC)**

#### Interactive Session
<em>2020-11-16, 11:10 - 11:40 PST </em> | <a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SESVRXLYJH34U314N" target="_blank" rel="noopener noreferrer"> PheedLoop Session <i class="fa fa-external-link" aria-hidden="true"></i> </a> 

#### Abstract
Quality-Diversity (QD) is a concept from Neuroevolution with some intriguing applications to Reinforcement Learning. It facilitates learning a population of agents where each member is optimized to simultaneously accumulate high task-returns and exhibit behavioral diversity compared to other members. In this paper, we build on a recent kernel-based method for training a QD policy ensemble with Stein variational gradient descent. With kernels based on <em>f</em>-divergence between the stationary distributions of policies, we convert the problem to that of efficient estimation of the ratio of these stationary distributions. We then study various distribution ratio estimators used previously for off-policy evaluation and imitation and re-purpose them to compute the gradients for policies in an ensemble such that the resultant population is diverse and of high-quality.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1J_wb9xoiALAPHZ-LiXUYdxXL5S2kXGAm/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


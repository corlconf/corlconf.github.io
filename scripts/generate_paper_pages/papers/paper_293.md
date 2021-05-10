---
layout: page
title: "Learning Hybrid Control Barrier Functions from Data"
subtitle: 
description:
permalink: /paper_293/
grand_parent: All Papers
parent: Tuesday
supp: 
code: https://github.com/unstable-zeros/learning-hcbfs
youtube_id: NAhzeBxUvhI
pdf: https://drive.google.com/file/d/1Aic58kKFuu1Ik1uOduePc1G1k8IF4upE/view
---

# Learning Hybrid Control Barrier Functions from Data

<a href="https://drive.google.com/file/d/1Aic58kKFuu1Ik1uOduePc1G1k8IF4upE/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="https://github.com/unstable-zeros/learning-hcbfs" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Lars Lindemann (KTH Royal Institute of Technology)*; Haimin Hu (University of Pennsylvania); Alexander Robey (University of Pennsylvania); Hanwen Zhang (University of Pennsylvania); Dimos Dimarogonas (KTH Royal Institute of Technology, Sweden); Stephen Tu (Google); Nikolai Matni (University of Pennsylvania)**

#### Interactive Session
<em>2020-11-17, 11:50 - 12:20 PST </em> | <a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SESZZME3GMGUCOE5Q" target="_blank" rel="noopener noreferrer"> PheedLoop Session <i class="fa fa-external-link" aria-hidden="true"></i> </a> 

#### Abstract
Motivated by the lack of systematic tools to obtain safe control laws for hybrid systems, we propose an optimization-based framework for learning certifiably safe control laws from data. In particular, we assume a setting in which the system dynamics are known and in which data exhibiting safe system behavior is available. We propose hybrid control barrier functions for hybrid systems as a means to synthesize safe control inputs. Based on this notion, we present an optimization-based framework to learn such hybrid control barrier functions from data. Importantly, we identify sufficient conditions on the data such that feasibility of the optimization problem ensures correctness of the learned hybrid control barrier functions, and hence the safety of the system. We illustrate our findings in two simulations studies, including a compass gait walker.


#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1pUeRw8r2mTtOsIrtU01hutNk3Z4Zj1gJ/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


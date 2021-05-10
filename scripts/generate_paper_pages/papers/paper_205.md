---
layout: page
title: "Universal Embeddings for Spatio-Temporal Tagging of Self-Driving Logs"
subtitle: 
description:
permalink: /paper_205/
grand_parent: All Papers
parent: Monday
supp: https://drive.google.com/file/d/1a9Cy7dD-IHcom5s3MrlqpYQuje1aRS81/view
code: 
youtube_id: IeOwVqXYLck
pdf: https://drive.google.com/file/d/1MYWfq9d2tpJuRwFFhzUjZf-mhgQGdB_h/view
---

# Universal Embeddings for Spatio-Temporal Tagging of Self-Driving Logs

<a href="https://drive.google.com/file/d/1MYWfq9d2tpJuRwFFhzUjZf-mhgQGdB_h/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="https://drive.google.com/file/d/1a9Cy7dD-IHcom5s3MrlqpYQuje1aRS81/view" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Sean Segal (Uber ATG)*; Eric Kee (Uber ATG); Wenjie Luo (University of Toronto); Abbas Sadat (Uber ATG); Ersin Yumer (Uber ATG); Raquel Urtasun (Uber ATG)**

#### Interactive Session
<em>2020-11-16, 12:30 - 13:00 PST </em> | <a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SESB7X73PHEG0BN0Q" target="_blank" rel="noopener noreferrer"> PheedLoop Session <i class="fa fa-external-link" aria-hidden="true"></i> </a> 

#### Abstract
In this paper, we tackle the problem of spatio-temporal tagging of self-driving scenes from raw sensor data. Our approach learns a universal embedding for all tags, enabling efficient tagging of many attributes and faster learning of new attributes with limited data. Importantly, the embedding is spatio-temporally aware, allowing the model to naturally output spatio-temporal tag values. Values can then be pooled over arbitrary regions, in order to, for example, compute the pedestrian density in front of the SDV, or determine if a car is blocking another car at a 4-way intersection. We demonstrate the effectiveness of our approach on a new large scale self-driving dataset, SDVScenes, containing 15 attributes relating to vehicle and pedestrian density, the actions of each actor, the speed of each actor, interactions between actors, and the topology of the road map. 

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1czZrfj508Bz1N7qSNKjPQi6ECxbF9sXy/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


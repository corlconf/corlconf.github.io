---
layout: page
title: "Learning from Demonstrations using Signal Temporal Logic"
subtitle: 
description:
permalink: /paper_498/
grand_parent: All Papers
parent: Wednesday
supp: 
code: 
youtube_id: tCzu2fKb45s
pdf: https://drive.google.com/file/d/1MH8KV1kIVSzJ4pFU4tLV0iUP163NIxV1/view
---

# Learning from Demonstrations using Signal Temporal Logic

<a href="https://drive.google.com/file/d/1MH8KV1kIVSzJ4pFU4tLV0iUP163NIxV1/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Aniruddh Puranic (University of Southern California)*; Jyotirmoy Deshmukh (USC); Stefanos Nikolaidis (University of Southern California)**

#### Interactive Session
*2020-11-18, 12:30 - 13:00 PST* 

#### Abstract
Learning-from-demonstrations is an emerging paradigm to obtain effective robot control policies for complex tasks via reinforcement learning without the need to explicitly design reward functions. However, it is susceptible to imperfections in demonstrations and also raises concerns of safety and interpretability in the learned control policies. To address these issues, we use Signal Temporal Logic to evaluate and rank the quality of demonstrations. Temporal logic-based specifications allow us to create non-Markovian rewards, and also define interesting causal dependencies between tasks such as sequential task specifications. We validate our approach through experiments on discrete-world and OpenAI Gym environments, and show that our approach outperforms the state-of-the-art Maximum Causal Entropy Inverse Reinforcement Learning.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1lAaD2uFVIgyYPApTdifKc-ppbQNErQmM/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


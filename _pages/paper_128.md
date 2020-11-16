---
layout: page
title: "Learning Latent Representations to Influence Multi-Agent Interaction"
subtitle: 
description:
permalink: /paper_128/
grand_parent: All Papers
parent: Tuesday
supp: 
code: 
youtube_id: -gCFcgb08jo
pdf: https://drive.google.com/file/d/1_ezqLLEv4HLtj9vflRj0sq3PNOhaSnJm/view
---

# Learning Latent Representations to Influence Multi-Agent Interaction

<a href="https://drive.google.com/file/d/1_ezqLLEv4HLtj9vflRj0sq3PNOhaSnJm/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Annie Xie (Stanford University)*; Dylan Losey (Stanford University); Ryan Tolsma (Stanford University); Chelsea Finn (Stanford); Dorsa Sadigh (Stanford)**

#### Interactive Session
<a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SESKUERXVII83SVEN" target="_blank" rel="noopener noreferrer"><em>2020-11-17, 11:10 - 11:40 PST </em></a>

#### Abstract
Seamlessly interacting with humans or robots is hard because these agents are non-stationary. They update their policy in response to the ego agent's behavior, and the ego agent must anticipate these changes to co-adapt. Inspired by humans, we recognize that robots do not need to explicitly model every low-level action another agent will make; instead, we can capture the latent strategy of other agents through high-level representations. We propose a reinforcement learning-based framework for learning latent representations of an agent's policy, where the ego agent identifies the relationship between its behavior and the other agent's future strategy. The ego agent then leverages these latent dynamics to influence the other agent, purposely guiding them towards policies suitable for co-adaptation. Across several simulated domains and a real-world air hockey game, our approach outperforms the alternatives and learns to influence the other agent.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1R1L8PKySb7nlMOhOiyeObHEYyFfxVzsI/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


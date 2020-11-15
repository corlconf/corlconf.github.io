---
layout: page
title: "The Emergence of Adversarial Communication in Multi-Agent Reinforcement Learning"
subtitle: 
description:
permalink: /paper_306/
grand_parent: All Papers
parent: Tuesday
supp: 
code: https://github.com/proroklab/adversarial_comms
youtube_id: 
pdf: https://drive.google.com/file/d/1uyZ1tDggGPPXMm6zWyWDXd986IWOzHCx/view
---

# The Emergence of Adversarial Communication in Multi-Agent Reinforcement Learning

<a href="https://drive.google.com/file/d/1uyZ1tDggGPPXMm6zWyWDXd986IWOzHCx/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="https://github.com/proroklab/adversarial_comms" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Jan Blumenkamp (University of Cambridge)*; Amanda Prorok (University of Cambridge)**

#### Interactive Session
*2020-11-17, 11:10 - 11:40 PST* 

#### Abstract
Many real-world problems require the coordination of multiple autonomous agents. Recent work has shown the promise of Graph Neural Networks (GNNs) to learn explicit communication strategies that enable complex multi-agent coordination. These works use models of cooperative multi-agent systems whereby agents strive to achieve a shared global goal. When considering agents with self-interested local objectives, the standard design choice is to model these as separate learning systems (albeit sharing the same environment). Such a design choice, however, precludes the existence of a single, differentiable communication channel, and consequently prohibits the learning of inter-agent communication strategies. In this work, we address this gap by presenting a learning model that accommodates individual non-shared rewards and a differentiable communication channel that is common among all agents. We focus on the case where agents have self-interested objectives, and develop a learning algorithm that elicits the emergence of adversarial communications. We perform experiments on multi-agent coverage and path planning problems, and employ a post-hoc interpretability technique to visualize the messages that agents communicate to each other. We show how a single self-interested agent is capable of learning highly manipulative communication strategies that allows it to significantly outperform a cooperative team of agents.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1ZTFSIhy5AFmzI0JLqBX8Mqn7obvHqttK/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


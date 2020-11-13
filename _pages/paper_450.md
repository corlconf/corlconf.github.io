---
layout: page
title: "Deep Reinforcement Learning with Population-Coded Spiking Neural Network for Continuous Control"
subtitle: 
description:
permalink: /paper_450/
grand_parent: All Papers
parent: Tuesday
supp: https://drive.google.com/file/d/1jX0b0gAfkXs6M2QAwnZesgSlzOHtxQta/view
code: https://github.com/combra-lab/pop-spiking-deep-rl
youtubeId: 
pdf: https://drive.google.com/file/d/1ISjZ00GBnvJ8GE3K10aN91iphURPP5e2/view
---

# Deep Reinforcement Learning with Population-Coded Spiking Neural Network for Continuous Control

<a href="https://drive.google.com/file/d/1ISjZ00GBnvJ8GE3K10aN91iphURPP5e2/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="https://drive.google.com/file/d/1jX0b0gAfkXs6M2QAwnZesgSlzOHtxQta/view" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="https://github.com/combra-lab/pop-spiking-deep-rl" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Guangzhi Tang (Rutgers University); Neelesh Kumar (Rutgers University); Raymond Yoo (Rutgers University); Konstantinos  Michmizos (Rutgers University)***

#### Interactive Session
*2020-11-17, 11:50 - 12:20 PST*

#### Abstract
The energy-efficient control of mobile robots has become crucial as the complexity of their real-world applications increasingly involves high-dimensional observation and action spaces, which cannot be offset by their limited on-board resources. An emerging non-Von Neumann model of intelligence, where spiking neural networks (SNNs) are executed on neuromorphic processors, is now considered as an energy-efficient and robust alternative to the state-of-the-art real-time robotic controllers for low dimensional control tasks. The challenge now for this new computing paradigm is to scale so that it can keep up with real-world applications. To do so, SNNs need to overcome the inherent limitations of their training, namely the limited ability of their spiking neurons to represent information and the lack of effective learning algorithms. Here, we propose a population-coded spiking actor network (PopSAN) that was trained in conjunction with a deep critic network using deep reinforcement learning (DRL). The population coding scheme, which is prevalent across brain networks, dramatically increased the representation capacity of the network and the hybrid learning combined the training advantages of deep networks with the energy-efficient inference of spiking networks. To show that our approach can be used for general-purpose spike-based reinforcement learning, we demonstrated its integration with a wide spectrum of policy-gradient based DRL methods covering both on-policy and off-policy DRL algorithms. We deployed the trained PopSAN on Intel's Loihi neuromorphic chip and benchmarked our method against the mainstream DRL algorithms for continuous control. To allow for a fair comparison among all methods, we validated them on OpenAI gym tasks. Our Loihi-run PopSAN consumed 140 times less energy per inference when compared against the deep actor network on Jetson TX2, and achieved the same level of performance. Our results demonstrate the overall efficiency of neuromorphic controllers and suggest the hybrid reinforcement learning approach as an alternative to deep learning, when both energy-efficiency and robustness are important.

#### Video 

#### Reviews

#### Rebuttal


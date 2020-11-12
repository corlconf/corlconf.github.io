---
layout: page
title: "Exploratory Grasping: Asymptotically Optimal Algorithms for Grasping Challenging Polyhedral Objects"
subtitle: 
description:
permalink: /paper_79/
grand_parent: All Papers
parent: Wednesday
supp: 
code: 
youtubeId: 
---

# Exploratory Grasping: Asymptotically Optimal Algorithms for Grasping Challenging Polyhedral Objects

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1SSksotROmwgiFoYWsb1XE4IHdu4aEOhv/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Michael Danielczuk (UC Berkeley); Ashwin Balakrishna (UC Berkeley)*; Daniel Brown (University of Texas at Austin); Ken Goldberg (UC Berkeley)**

#### Abstract
There has been significant recent work on data-driven algorithms for learning general-purpose grasping policies.  However, these policies can consistently fail to grasp challenging objects which are significantly out of the distribution of objects in the training data or which have very few high quality grasps. Motivated by such objects, we propose a novel problem setting, Exploratory Grasping, for efficiently discovering reliable grasps on an unknown polyhedral object via sequential grasping, releasing, and toppling. We formalize Exploratory Grasping as a Markov Decision Process where we assume that the robot can (1) distinguish stable poses of a polyhedral object of unknown geometry, (2) generate grasp candidates on these poses and execute them, (3) determine whether each grasp is successful, and (4) release the object into a random new pose after a grasp successor topple the object after a grasp failure.  We study the theoretical complexity of Exploratory Grasping in the context of reinforcement learning and present an efficient bandit-style algorithm, Bandits for Online Rapid Grasp ExplorationStrategy (BORGES), which leverages the structure of the problem to efficiently discover high performing grasps for each object stable pose. BORGES can be used to complement any general-purpose grasping algorithm with any grasp modality (parallel-jaw, suction, multi-fingered, etc) to learn policies for objects in which they exhibit persistent failures. Simulation experiments suggest that BORGES can significantly outperform both general-purpose grasping pipelines and two other online learning algorithms and achieves performance within 5% of the optimal policy within 1000 and 8000 timesteps on average across 46 challenging objects from the Dex-Net adversarial and EGAD! object datasets, respectively. Initial physical experiments suggesting that BORGES can improve grasp success rate on average over two challenging 3D printed objects by 45% over a Dex-Net baseline. See <a href="https://tinyurl.com/exp-grasping" target="_blank">https://tinyurl.com/exp-grasping</a> for supplementary material and videos.

#### Video 

#### Reviews

#### Rebuttal

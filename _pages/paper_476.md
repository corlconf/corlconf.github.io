---
layout: page
title: "Explicitly Encouraging Low Fractional Dimensional Trajectories Via Reinforcement Learning"
subtitle: 
description:
permalink: /paper_476/
grand_parent: All Papers
parent: Wednesday
supp: 
code: https://github.com/sgillen/fractal_rl
youtubeId: 
pdf: https://drive.google.com/file/d/1OryWMUs-HbZL5wbDOg0ynZc1crtHj3R4/view
---

# Explicitly Encouraging Low Fractional Dimensional Trajectories Via Reinforcement Learning

<a href="https://drive.google.com/file/d/1OryWMUs-HbZL5wbDOg0ynZc1crtHj3R4/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="https://github.com/sgillen/fractal_rl" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Sean Gillen (UCSB)*; Katie Byl (UCSB)**

#### Interactive Session
*2020-11-18, 12:30 - 13:00 PST*

#### Abstract
A key limitation in using various modern methods of machine learning in developing feedback control policies is the lack of appropriate methodologies to analyze their long-term dynamics, in terms of making any sort of guarantees (even statistically) about robustness.  The central reasons for this are largely due to the so-called curse of dimensionality, combined with the black-box nature of the resulting control policies themselves. This paper aims at the first of these issues. Although the full state space of a system may be quite large in dimensionality, it is a common feature of most model-based control methods that the resulting closed-loop systems demonstrate dominant dynamics that are rapidly driven to some lower-dimensional sub-space within. In this work we argue that the dimensionality of this subspace is captured by tools from fractal geometry, namely various notions of a fractional dimension. We then show that the dimensionality of trajectories induced by model free reinforcement learning agents can be influenced adding a post processing function to the agents reward signal. We verify that the dimensionality reduction is robust to noise being added to the system and show that that the modified agents are more actually more robust to noise and push disturbances in general for the systems we examined.

#### Video 

#### Reviews

#### Rebuttal


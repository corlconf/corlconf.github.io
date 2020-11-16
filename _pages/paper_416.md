---
layout: page
title: "Multiagent Rollout and Policy Iteration for POMDP with Application to Multi-Robot Repair Problems"
subtitle: 
description:
permalink: /paper_416/
grand_parent: All Papers
parent: Monday
supp: 
code: 
youtube_id: eBEDxtEcLUk
pdf: https://drive.google.com/file/d/1fZ9f0AJkgkIyWWYOJOcIQI_q3pyjcreL/view
---

# Multiagent Rollout and Policy Iteration for POMDP with Application to Multi-Robot Repair Problems

<a href="https://drive.google.com/file/d/1fZ9f0AJkgkIyWWYOJOcIQI_q3pyjcreL/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Sushmita Bhattacharya (Harvard University)*; Siva Kailas (Arizona State University); Sahil Badyal (Arizona State University); Stephanie Gil (Harvard University); Dimitri Bertsekas (Massachusetts Institute of Technology (MIT))**

#### Interactive Session
<a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SESG08UFZ2P1446MN" target="_blank" rel="noopener noreferrer"><em>2020-11-16, 11:50 - 12:20 PST </em></a>

#### Abstract
In this paper we consider infinite horizon discounted dynamic programming problems with finite state and control spaces, partial state observations, and a multiagent structure. We discuss and compare algorithms that simultaneously or sequentially optimize the agents' controls by using multistep lookahead, truncated rollout with a known base policy, and a terminal cost function approximation. Our methods specifically address the computational challenges of partially observable multiagent problems. In particular: 1) We consider rollout algorithms that dramatically reduce required computation while preserving the key cost improvement property of the standard rollout method. The per-step computational requirements for our methods are on the order of <em>O(Cm)</em> as compared with <em>O(C^m)</em> for standard rollout, where <em>C</em> is the maximum cardinality of the constraint set for the control component of each agent, and <em>m<em> is the number of agents. 2) We show that our methods can be applied to challenging problems with a graph structure, including a class of robot repair problems whereby multiple robots collaboratively inspect and repair a system under partial information. 3) We provide a simulation study that compares our methods with existing methods, and demonstrate that our methods can handle larger and more complex partially observable multiagent problems (state space size 1E37 and control space size 1E7, respectively). In particular, we verify experimentally that our multiagent rollout methods perform nearly as well as standard rollout for problems with few agents, and produce satisfactory policies for problems with a larger number of agents that are intractable by standard rollout and other state of the art methods. Finally, we incorporate our multiagent rollout algorithms as building blocks in an approximate policy iteration scheme, where successive rollout policies are approximated by using neural network classifiers. While this scheme requires a strictly off-line implementation, it works well in our computational experiments and produces additional significant performance improvement over the single online rollout iteration method.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1yDvnF91CPGz7IHqzEdimUHYqZ963JReP/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


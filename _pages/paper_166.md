---
layout: page
title: "Untangling Dense Knots by Learning Task-Relevant Keypoints"
subtitle: 
description:
permalink: /paper_166/
grand_parent: All Papers
parent: Monday
supp: 
code: 
youtube_id: bR6Co9cDJWU
pdf: https://drive.google.com/file/d/1m-9qiFup0_u6bcM4ZH6cssy5mwECFjey/view
---

# Untangling Dense Knots by Learning Task-Relevant Keypoints

<a href="https://drive.google.com/file/d/1m-9qiFup0_u6bcM4ZH6cssy5mwECFjey/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Jennifer Grannen (UC Berkeley)*; Priya Sundaresan (UC Berkeley)*; Brijen Thananjeyan (UC Berkeley); Jeffrey Ichnowski (University of California, Berkeley); Ashwin Balakrishna (UC Berkeley); Minho Hwang (UC Berkeley); Vainavi Viswanath (UC Berkeley); Michael Laskey (UC Berkeley); Joseph Gonzalez (UC Berkeley); Ken Goldberg (UC Berkeley)**

#### Interactive Session
<a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SESDSMREXWA7LBB6Y" target="_blank" rel="noopener noreferrer"><em>2020-11-16, 12:30 - 13:00 PST </em></a>

#### Abstract
Untangling ropes, wires, and cables is a challenging task for robots due to the high-dimensional configuration space, visual homogeneity, self-occlusions, and complex dynamics. We consider dense (tight) knots that lack space between self-intersections and present an iterative approach that uses learned geometric structure in configurations. We instantiate this into an algorithm, HULK: Hierarchical Untangling from Learned Keypoints, which combines learning-based perception with a geometric planner into a policy that guides a bilateral robot to untangle knots. To evaluate the policy, we perform experiments both in a novel simulation environment modelling cables with varied knot types and textures and in a physical system using the da Vinci surgical robot. We find that HULK is able to untangle cables with dense figure-eight and overhand knots and generalize to varied textures and appearances. We compare two variants of HULK to three baselines and observe that HULK achieves 43.3% higher success rates on a physical system compared to the next best baseline. HULK successfully untangles a cable from a dense initial configuration containing up to two overhand and figure-eight knots in 97.9% of 378 simulation experiments with an average of 12.1 actions per trial. In physical experiments, HULK achieves 61.7% untangling success, averaging 8.48 actions per trial. Supplementary material, code, and videos can be found at <a href="https://tinyurl.com/y3a88ycu" target="_blank">https://tinyurl.com/y3a88ycu</a>.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1nvJbhI26wyLkCjSHnJNLxIWZoJEmw_8N/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


---
layout: page
title: "Augmenting GAIL with BC for sample efficient imitation learning"
subtitle: 
description:
permalink: /paper_25/
grand_parent: All Papers
parent: Monday
supp: 
code: https://github.com/rohitrango/BC-regularized-GAIL
youtubeId: 
---

# Augmenting GAIL with BC for sample efficient imitation learning

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1Dd571oHIddZrVnP4S9AWYWLVEaIpcRf4/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Rohit Jena (Carnegie Mellon University)*; Changliu Liu (Carnegie Mellon University); Katia Sycara (Carnegie Mellon University)**

#### Interactive Session
*2020-11-16, 11:10 - 11:40 PST*

#### Abstract
Imitation learning is the problem of recovering an expert policy without access to a reward signal. Behavior cloning and GAIL are two widely used methods for performing imitation learning. Behavior cloning converges in a few iterations, but doesn't achieve peak performance due to its inherent iid assumption about the state-action distribution. GAIL addresses the issue by accounting for the temporal dependencies when performing a state distribution matching between the agent and the expert. Although GAIL is sample efficient in the number of expert trajectories required, it is still not very sample efficient in terms of the environment interactions needed for convergence of the policy. Given the complementary benefits of both methods, we present a simple and elegant method to combine both methods to enable stable and sample efficient learning. Our algorithm is very simple to implement and integrates with different policy gradient algorithms. We demonstrate the effectiveness of the algorithm in low dimensional control tasks, gridworlds and in high dimensional image-based tasks.

#### Video 

#### Reviews

#### Rebuttal

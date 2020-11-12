---
layout: page
title: "Learning a Contact-Adaptive Controller for Robust, Efficient Legged Locomotion"
subtitle: 
description:
permalink: /paper_187/
grand_parent: All Papers
parent: Monday
supp: 
code: 
youtubeId: 
---

# Learning a Contact-Adaptive Controller for Robust, Efficient Legged Locomotion

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/185kNH9zATbt95j3mTCuM-2rcy30TWbFq/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Xingye Da (Nvidia)*; Zhaoming Xie (University of British Columbia); David Hoeller (Nvidia); Byron Boots (Nvidia); Anima Anandkumar (); Yuke Zhu (University of Texas - Austin); Buck Babich (NVIDIA); Animesh Garg (University of Toronto, Vector Institute, Nvidia)**

#### Abstract
We present a hierarchical framework that combines model-based control and reinforcement learning (RL) to synthesize robust controllers for a quadruped (the Unitree Laikago). The system consists of a high-level controller that learns to choose from a set of primitives in response to changes in the environment and a low-level controller that utilizes an established control method to robustly execute the primitives. Our framework learns a controller that can adapt to challenging environmental changes on the fly, including novel scenarios not seen during training. The learned controller is up to 85~percent more energy efficient and is more robust compared to baseline methods. We also deploy the controller on a physical robot without any randomization or adaptation scheme.

#### Video 

#### Reviews

#### Rebuttal

---
layout: page
title: "Tolerance-Guided Policy Learning for Adaptable and Transferrable Delicate Industrial Insertion"
subtitle: 
description:
permalink: /paper_452/
grand_parent: All Papers
parent: Wednesday
supp: 
code: 
youtubeId: 
---

# Tolerance-Guided Policy Learning for Adaptable and Transferrable Delicate Industrial Insertion

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1aObrQt-Y2elnex4L01v3rwPLH6_Tin7q/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Boshen Niu (Carnegie Mellon University); Chenxi Wang (Carnegie Mellon University); Changliu Liu (Carnegie Mellon University)***

#### Interactive Session
*2020-11-18, 11:50 - 12:20 PST*

#### Abstract
Policy learning for delicate industrial insertion tasks (e.g., PC board assembly) is challenging. This paper considers two major problems: how to learn a diversified policy (instead of just one average policy) that can efficiently handle different workpieces with minimum amount of training data, and how to handle defects of workpieces during insertion. To address the problems, we propose tolerance-guided policy learning. 
    To encourage transferability of the learned policy to different workpieces, we add a task embedding to the policy's input space using the insertion tolerance. Then we train the policy using generative adversarial imitation learning with reward shaping (RS-GAIL) on a variety of representative situations. 
    To encourage adaptability of the learned policy to handle defects, we build a probabilistic inference model that can output the best inserting pose based on failed insertions using the tolerance model. The best inserting pose is then used as a reference to the learned policy. 
    This proposed method is validated on a sequence of IC socket insertion tasks in simulation. The results show that 1) RS-GAIL can efficiently learn optimal policies under sparse rewards; 2) the tolerance embedding can enhance the transferability of the learned policy; 3) the probabilistic inference makes the policy robust to defects on the workpieces.

#### Video 

#### Reviews

#### Rebuttal

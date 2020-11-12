---
layout: page
title: "DeepMPCVS: Deep Model Predictive Control for Visual Servoing"
subtitle: 
description:
permalink: /paper_448/
grand_parent: All Papers
parent: Tuesday
supp: https://drive.google.com/file/d/1Q8iG4j1uvtLxGsOOdbll_DeVatowJNwF/view
code: 
youtubeId: 
---

# DeepMPCVS: Deep Model Predictive Control for Visual Servoing

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1OJh5Ngi5c_-CQzqDcz5SjGVuK1wzO1cc/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Pushkal Katara (Robotics Research Center, IIITH)*; Harish Y V S (IIIT HYDERABAD); Harit Pandya (University of Lincoln); Abhinav Gupta (International Institute of Information Technology (IIIT), Hyderabad); AadilMehdi Sanchawala (International Institute of Information Technology, Hyderabad); Gourav Kumar (TCS Innovation labs Kolkata); Brojeshwar Bhowmick (Tata Consultancy Services); Madhava Krishna (IIIT-Hyderabad)**

#### Abstract
The simplicity of the visual servoing approach makes it an attractive option for tasks dealing with vision-based control of robots in many real-world applications. However, attaining precise alignment for unseen environments pose a challenge to existing visual servoing approaches. While classical approaches assume a perfect world, the recent data-driven approaches face issues when generalizing to novel environments. In this paper, we aim to combine the best of both worlds. We present a deep model predictive visual servoing framework that can achieve precise alignment with optimal trajectories and can generalize to novel environments. Our framework consists of a deep network for optical flow predictions, which are used along with a predictive model to forecast future optical flow. For generating an optimal set of velocities we present a control network that can be trained on-the-fly without any supervision. Through extensive simulations on photo-realistic indoor settings of the popular Habitat framework, we show significant performance gain due to the proposed formulation vis-a-vis recent state of the art methods. Specifically, we show vastly improved performance in trajectory length and faster convergence over recent approaches.

#### Video 

#### Reviews

#### Rebuttal

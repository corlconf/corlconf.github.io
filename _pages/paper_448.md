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
youtube_id: 1cvBZ7Qz73g
pdf: https://drive.google.com/file/d/1OJh5Ngi5c_-CQzqDcz5SjGVuK1wzO1cc/view
---

# DeepMPCVS: Deep Model Predictive Control for Visual Servoing

<a href="https://drive.google.com/file/d/1OJh5Ngi5c_-CQzqDcz5SjGVuK1wzO1cc/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="https://drive.google.com/file/d/1Q8iG4j1uvtLxGsOOdbll_DeVatowJNwF/view" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Pushkal Katara (Robotics Research Center, IIITH)*; Harish Y V S (IIIT HYDERABAD); Harit Pandya (University of Lincoln); Abhinav Gupta (International Institute of Information Technology (IIIT), Hyderabad); AadilMehdi Sanchawala (International Institute of Information Technology, Hyderabad); Gourav Kumar (TCS Innovation labs Kolkata); Brojeshwar Bhowmick (Tata Consultancy Services); Madhava Krishna (IIIT-Hyderabad)**

#### Interactive Session
<a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SES7E8XY6NJDC2K5T" target="_blank" rel="noopener noreferrer"><em>2020-11-17, 11:10 - 11:40 PST </em></a>

#### Abstract
The simplicity of the visual servoing approach makes it an attractive option for tasks dealing with vision-based control of robots in many real-world applications. However, attaining precise alignment for unseen environments pose a challenge to existing visual servoing approaches. While classical approaches assume a perfect world, the recent data-driven approaches face issues when generalizing to novel environments. In this paper, we aim to combine the best of both worlds. We present a deep model predictive visual servoing framework that can achieve precise alignment with optimal trajectories and can generalize to novel environments. Our framework consists of a deep network for optical flow predictions, which are used along with a predictive model to forecast future optical flow. For generating an optimal set of velocities we present a control network that can be trained on-the-fly without any supervision. Through extensive simulations on photo-realistic indoor settings of the popular Habitat framework, we show significant performance gain due to the proposed formulation vis-a-vis recent state of the art methods. Specifically, we show vastly improved performance in trajectory length and faster convergence over recent approaches.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1yzf1m3EJTUfwXni6NhLU5tvEsoqEJ7XG/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


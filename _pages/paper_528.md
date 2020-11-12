---
layout: page
title: "Towards Autonomous Eye Surgery by Combining Deep Imitation Learning with Optimal Control"
subtitle: 
description:
permalink: /paper_528/
grand_parent: All Papers
parent: Wednesday
supp: 
code: 
youtubeId: 
---

# Towards Autonomous Eye Surgery by Combining Deep Imitation Learning with Optimal Control

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1UbaR_nH-sv5Dz-xtWaxAkWHDD1KNFAyn/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Ji Woong Kim (Johns Hopkins University)*; Peiyao Zhang (Johns Hopkins University); Peter Gehlbach (Johns Hopkins Hospital,); Iulian Iordachita (The Johns Hopkins University); Marin Kobilarov (Johns Hopkins University)**

#### Abstract
During retinal microsurgery, precise manipulation of the delicate retinal tissue is required for positive surgical outcome. However, accurate manipulation and navigation of surgical tools remain difficult due to a constrained workspace and the top-down view during the surgery, which limits the surgeon’s ability to estimate depth. To alleviate such difficulty, we propose to automate the tool-navigation task by learning to predict relative goal position on the retinal surface from the current tool-tip position. Given an estimated target on the retina, we generate an optimal trajectory leading to the predicted goal while imposing safety-related physical constraints aimed to minimize tissue damage. As an extended task, we generate goal predictions to various points across the retina to localize eye geometry and further generate safe trajectories within the estimated confines. Through experiments in both simulation and with several eye phantoms, we demonstrate that our framework can permit navigation to various points on the retina within 0.089mm and 0.118mm in xy error which is less than the human’s surgeon mean tremor at the tool-tip of 0.180mm. All safety constraints were fulfilled and the algorithm was robust to previously unseen eyes as well as unseen objects in the scene. Live video demonstration is available here: <a href="https://youtu.be/n5j5jCCelXk" target="_blank">https://youtu.be/n5j5jCCelXk</a>

#### Video 

#### Reviews

#### Rebuttal

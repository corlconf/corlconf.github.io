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
youtube_id: sgcMwDU645E
pdf: https://drive.google.com/file/d/1UbaR_nH-sv5Dz-xtWaxAkWHDD1KNFAyn/view
---

# Towards Autonomous Eye Surgery by Combining Deep Imitation Learning with Optimal Control

<a href="https://drive.google.com/file/d/1UbaR_nH-sv5Dz-xtWaxAkWHDD1KNFAyn/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Ji Woong Kim (Johns Hopkins University)*; Peiyao Zhang (Johns Hopkins University); Peter Gehlbach (Johns Hopkins Hospital,); Iulian Iordachita (The Johns Hopkins University); Marin Kobilarov (Johns Hopkins University)**

#### Interactive Session
<a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SESIAT91CYT9LD6TP" target="_blank" rel="noopener noreferrer"><em>2020-11-18, 11:10 - 11:40 PST </em></a>

#### Abstract
During retinal microsurgery, precise manipulation of the delicate retinal tissue is required for positive surgical outcome. However, accurate manipulation and navigation of surgical tools remain difficult due to a constrained workspace and the top-down view during the surgery, which limits the surgeon’s ability to estimate depth. To alleviate such difficulty, we propose to automate the tool-navigation task by learning to predict relative goal position on the retinal surface from the current tool-tip position. Given an estimated target on the retina, we generate an optimal trajectory leading to the predicted goal while imposing safety-related physical constraints aimed to minimize tissue damage. As an extended task, we generate goal predictions to various points across the retina to localize eye geometry and further generate safe trajectories within the estimated confines. Through experiments in both simulation and with several eye phantoms, we demonstrate that our framework can permit navigation to various points on the retina within 0.089mm and 0.118mm in xy error which is less than the human’s surgeon mean tremor at the tool-tip of 0.180mm. All safety constraints were fulfilled and the algorithm was robust to previously unseen eyes as well as unseen objects in the scene. Live video demonstration is available here: <a href="https://youtu.be/n5j5jCCelXk" target="_blank">https://youtu.be/n5j5jCCelXk</a>

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1PbpZbL7k6mB9TsLCM1YA7QKPx39Ru34W/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


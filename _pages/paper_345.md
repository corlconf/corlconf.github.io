---
layout: page
title: "Amodal 3D Reconstruction for Robotic Manipulation via Stability and Connectivity"
subtitle: 
description:
permalink: /paper_345/
grand_parent: All Papers
parent: Wednesday
supp: https://drive.google.com/file/d/1K05b6qZNjP0XNHaGZ5laF4lrPr7g4lij/view
code: https://github.com/wagnew3/ARM
youtube_id: 
pdf: https://drive.google.com/file/d/1AQMpFtZxKASH1WGs45NYfdMI621IXtAI/view
---

# Amodal 3D Reconstruction for Robotic Manipulation via Stability and Connectivity

<a href="https://drive.google.com/file/d/1AQMpFtZxKASH1WGs45NYfdMI621IXtAI/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="https://drive.google.com/file/d/1K05b6qZNjP0XNHaGZ5laF4lrPr7g4lij/view" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="https://github.com/wagnew3/ARM" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**William Agnew (University of Washington)*; Christopher Xie (University of Washington); Aaron Walsman (University of Washington); Octavian Murad (University of Washington); Yubo Wang (University of Washington); Pedro Domingos (University of Washington); Siddhartha Srinivasa (University of Washington)**

#### Interactive Session
<a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SESLA7NA9UCIK3CES" target="_blank" rel="noopener noreferrer"><em>2020-11-18, 11:50 - 12:20 PST </em></a>

#### Abstract
Learning-based 3D object reconstruction enables single- or few-shot estimation of 3D object models. For robotics,  this holds the potential to allow model-based methods to rapidly adapt to novel objects and scenes. Existing 3D reconstruction techniques optimize for visual reconstruction fidelity, typically measured by chamfer distance or voxel IOU. We find that when applied to realistic, cluttered robotics environments, these systems produce reconstructions with low physical realism, resulting in poor task performance when used for model-based control.  We propose ARM, an amodal 3D reconstruction system that introduces (1) a stability prior over object shapes, (2) a connectivity prior, and (3) a multi-channel input representation that allows for reasoning over relationships between groups of objects.  By using these priors over the physical properties of objects, our system improves reconstruction quality not just by standard visual metrics, but also performance of model-based control on a variety of robotics manipulation tasks in challenging, cluttered environments.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1w0PpaRKaoJZl3xXAVQZrVwj0JOiq1Vrt/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


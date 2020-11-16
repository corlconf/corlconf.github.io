---
layout: page
title: "Soft Multicopter Control Using Neural Dynamics Identification"
subtitle: 
description:
permalink: /paper_396/
grand_parent: All Papers
parent: Monday
supp: https://drive.google.com/file/d/1IdF0CHrFuBWYrTAg1snHQxSi9ek9bECd/view
code: 
youtube_id: o9KjUyFhmI8
pdf: https://drive.google.com/file/d/1VhGffWmJq_XX28imCZKOZTEOTVmFX8U1/view
---

# Soft Multicopter Control Using Neural Dynamics Identification

<a href="https://drive.google.com/file/d/1VhGffWmJq_XX28imCZKOZTEOTVmFX8U1/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="https://drive.google.com/file/d/1IdF0CHrFuBWYrTAg1snHQxSi9ek9bECd/view" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Yitong Deng (Dartmouth College)*; Yaorui Zhang (Dartmouth College); Xingzhe He (University of British Columbia); Shuqi Yang (Dartmouth College); Yunjin Tong (Dartmouth College); Michael Zhang (Dartmouth College); Daniel DiPietro (Dartmouth College); Bo Zhu (Dartmouth College)**

#### Interactive Session
<a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SESTK0H2Y23UC4SGH" target="_blank" rel="noopener noreferrer"><em>2020-11-16, 11:50 - 12:20 PST </em></a>

#### Abstract
We propose a data-driven method to automatically generate feedback controllers for soft multicopters featuring deformable materials, non-conventional geometries, and asymmetric rotor layouts, to deliver compliant deformation and agile locomotion. Our approach coordinates two sub-systems: a physics-inspired network ensemble that simulates the soft drone dynamics and a custom LQR control loop enhanced by a novel online-relinearization scheme to control the neural dynamics. Harnessing the insights from deformation mechanics, we design a decomposed state formulation whose modularity and compactness facilitate the dynamics learning while its measurability readies it for real-world adaptation. Our method is painless to implement, and requires only conventional, low-cost gadgets for fabrication. In a high-fidelity simulation environment, we demonstrate the efficacy of our approach by controlling a variety of customized soft multicopters to perform hovering, target reaching, velocity tracking, and active deformation.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/13KvkklAZAyqStybl1qV-0QHFA5ezqer_/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


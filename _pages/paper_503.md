---
layout: page
title: "Learning Predictive Models for Ergonomic Control of Prosthetic Devices"
subtitle: 
description:
permalink: /paper_503/
grand_parent: All Papers
parent: Monday
supp: https://drive.google.com/file/d/1tSIvNk-UG1MdH0pPQvsaR2mIqzzG0tAe/view
code: 
youtube_id: 5TwB3fmNXQE
pdf: https://drive.google.com/file/d/17i5wYOoZrgbpFGlHaQmHhElKp_UfolwQ/view
---

# Learning Predictive Models for Ergonomic Control of Prosthetic Devices

<a href="https://drive.google.com/file/d/17i5wYOoZrgbpFGlHaQmHhElKp_UfolwQ/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="https://drive.google.com/file/d/1tSIvNk-UG1MdH0pPQvsaR2mIqzzG0tAe/view" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**GEOFFEY CLARK (Arizona State University)*; Joseph Campbell (Arizona State University); Heni Ben Amor (Arizona State University)**

#### Interactive Session
<a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SES1AMRGLZ7ONQB1D" target="_blank" rel="noopener noreferrer"><em>2020-11-16, 12:30 - 13:00 PST </em></a>

#### Abstract
We present Model-Predictive Interaction Primitives - a robot learning framework for assistive motion in human-machine collaboration tasks which explicitly accounts for biomechanical impact on the human musculoskeletal system. First, we extend Interaction Primitives to enable predictive biomechanics: the prediction of future biomechanical states of a human partner conditioned on current observations and intended robot control signals. In turn, we leverage this capability within a model-predictive control strategy to identify the future ergonomic and biomechanical ramifications of potential robot actions. Optimal control trajectories are selected so as to minimize future physical impact on the human musculoskeletal system. We empirically demonstrate that our approach minimizes knee or muscle forces via generated control actions selected according to biomechanical cost functions. Experiments are performed in synthetic and real-world experiments involving powered prosthetic devices.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1bEGH2eiSL3wwfnOnjVOZdE4ANUI_1MRe/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


---
layout: page
title: "EXI-Net: EXplicitly/Implicitly Conditioned Network for Multiple Environment Sim-to-Real Transfer"
subtitle: 
description:
permalink: /paper_268/
grand_parent: All Papers
parent: Tuesday
supp: https://drive.google.com/file/d/1yxkCoXeE22yAIyNKqRPD7U_xqbmzf_2L/view
code: 
youtube_id: U5uQMDxkSz8
pdf: https://drive.google.com/file/d/1a1h5QgQwYQQud0oNSAJwT0G73zSuoF5w/view
---

# EXI-Net: EXplicitly/Implicitly Conditioned Network for Multiple Environment Sim-to-Real Transfer

<a href="https://drive.google.com/file/d/1a1h5QgQwYQQud0oNSAJwT0G73zSuoF5w/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="https://drive.google.com/file/d/1yxkCoXeE22yAIyNKqRPD7U_xqbmzf_2L/view" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Takayuki Murooka (The University of Tokyo)*; Masashi Hamaya (OMRON SINICX Corporation); Felix von Drigalski (OMRON SINIC X); Kazutoshi Tanaka (OMRON SINIC X Corporation); Yoshihisa Ijiri (OMRON Corporation)**

#### Interactive Session
<a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SES23YKPEJCPK6H0Z" target="_blank" rel="noopener noreferrer"><em>2020-11-17, 12:30 - 13:00 PST </em></a>

#### Abstract
Sim-to-real transfer is attractive for robot learning, as it avoids the high cost of collecting data with real robots, but transferring agents from simulation to the real world is challenging. Previous studies have presented promising methods to solve this problem, but they may fail when a wider range of dynamics has to be considered. In this study, we propose a network architecture with explicit and implicit dynamics parameters for sim-to-real transfer from multiple environments. Using this method, we can simultaneously estimate the dynamics of the real world and optimize the action in various kinds of environments. The core novelty lies in the simultaneous dynamics estimation and action optimization, as well as the use of explicit (physically quantifiable) and implicit (latent) dynamics parameters to condition the network input. We apply our method to the object pushing task and verify its effectiveness by comparing it with previous methods and real-world experiments.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1QccQFxahiElPRKXlz7ZOtLvGdfGqOBPX/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


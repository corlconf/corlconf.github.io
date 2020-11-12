---
layout: page
title: "Flightmare: A Flexible Quadrotor Simulator"
subtitle: 
description:
permalink: /paper_250/
grand_parent: All Papers
parent: Tuesday
supp: 
code: https://github.com/uzh-rpg/flightmare
youtubeId: 
---

# Flightmare: A Flexible Quadrotor Simulator

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1snUSNps-o0nHJwo3C_62XubQzKxIKztY/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Yunlong Song (ETH / University of Zurich)*; Selim  Naji  (ETH / Univ. of Zurich); Elia Kaufmann (ETH / University of Zurich); Antonio Loquercio (ETH / University of Zurich); Davide Scaramuzza (University of Zurich & ETH Zurich, Switzerland)**

#### Abstract
State-of-the-art quadrotor simulators have a rigid and highly-specialized structure: either are they really fast, physically accurate, or photo-realistic. In this work, we propose a paradigm shift in the development of simulators: moving the trade-off between accuracy and speed from the developers to the end-users. We use this idea to develop a flexible quadrotor simulator: Flightmare. In this work, we propose a novel quadrotor simulator: Flightmare.  Flightmare is composed of two main components: a configurable rendering engine built on Unity and a flexible physics engine for dynamics simulation. Those two components are totally decoupled and can run independently of each other. This makes our simulator extremely fast: rendering achieves speeds of up to 230 Hz, while physics simulation of up to 200,000 Hz on a laptop. In addition, Flightmare comes with several desirable features: (i) a large multi-modal sensor suite, including an interface to extract the 3D point-cloud of the scene; (ii) an API for reinforcement learning which can simulate hundreds of quadrotors in parallel; and (iii) integration with a virtual-reality headset for interaction with the simulated environment. We demonstrate the flexibility of Flightmare by using it for two different robotic tasks: quadrotor control using deep reinforcement learning and collision-free path planning in a complex 3D environment.

#### Video 

#### Reviews

#### Rebuttal

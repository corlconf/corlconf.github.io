---
layout: page
title: "Modeling Long-horizon Tasks as Sequential Interaction Landscapes"
subtitle: 
description:
permalink: /paper_101/
grand_parent: All Papers
parent: Monday
supp: 
code: 
youtubeId: 
---

# Modeling Long-horizon Tasks as Sequential Interaction Landscapes

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1Vo1zbHKHgHtEoNmmkyzBHXjab8fC6Tjl/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Soeren Pirk (Google)*; Karol Hausman (Google Brain); Alexander Toshev (Google); Mohi Khansari (X, The Moonshot Factory)**

#### Abstract
Task planning over long-time horizons is a challenging and open problem in robotics and its complexity grows exponentially with an increasing number of subtasks. In this paper we present a deep neural network that learns dependencies and transitions across subtasks solely from a set of demonstration videos. We represent each subtasks as action symbols (e.g. move cup), and show that these symbols can be learned and predicted directly from image observations. Learning symbol sequences provides the network with additional information about the most frequent transitions and relevant dependencies between subtasks and thereby structures tasks over long-time horizons. Learning from images, on the other hand, allows the network to continuously monitor the task progress and thus to interactively adapt to changes in the environment. We evaluate our framework on two long horizon tasks: (1) block stacking of puzzle pieces being executed by humans, and (2) a robot manipulation task involving pick and place of objects and sliding a cabinet door with  a 7-DoF robot arm. We show that complex plans can be carried out when executing the robotic task and the robot can interactively adapt to changes in the environment and recover from failure cases.

#### Video 

#### Reviews

#### Rebuttal

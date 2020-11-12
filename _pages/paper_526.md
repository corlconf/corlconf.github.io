---
layout: page
title: "Robust Policies via Mid-Level Visual Representations: An Experimental Study in Manipulation and Navigation"
subtitle: 
description:
permalink: /paper_526/
grand_parent: All Papers
parent: Monday
supp: https://drive.google.com/file/d/1sks2le3ziJRRpEL3-cWzP6vKTaaie-Jn/view
code: https://github.com/alexsax/robust-policies-via-midlevel-vision
youtubeId: 
---

# Robust Policies via Mid-Level Visual Representations: An Experimental Study in Manipulation and Navigation

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1C9q14pUZPMUxfntx9Kg1xoiL6nRr332b/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Bryan Chen (UC Berkeley)*; Alexander Sax (UC Berkeley); Francis Lewis (Stanford); Iro Armeni (Stanford University); Silvio Savarese (Stanford University); Amir Zamir (Swiss Federal Institute of Technology (EPFL)); Jitendra Malik (University of California at Berkeley); Lerrel Pinto (NYU/Berkeley)**

#### Interactive Session
*2020-11-16, 11:10 - 11:40 PST*

#### Abstract
Vision-based robotics often factors the control loop into separate components for perception and control. Conventional perception components usually extract hand-engineered features from the visual input that are then used by the control component in an explicit manner. In contrast, recent advances in deep RL make it possible to learn these features end-to-end during training, but the final result is often brittle, fails unexpectedly under minuscule visual shifts, and comes with a high sample complexity cost.

In this work, we study the effects of using mid-level visual representations asynchronously trained for traditional computer vision objectives as a generic and easy-to-decode perceptual state in an end-to-end RL framework. We show that the invariances provided by the mid-level representations aid generalization, improve sample complexity, and lead to a higher final performance. Compared to the alternative approaches for incorporating invariances, such as domain randomization, using asynchronously trained mid-level representations scale better to harder problems and larger domain shifts, and consequently, successfully trains policies for tasks where domain randomization or learning-from-scratch failed. Our experimental findings are reported on manipulation and navigation tasks using real robots as well as simulations. 

#### Video 

#### Reviews

#### Rebuttal

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
youtube_id: pJr-jb1vywE
pdf: https://drive.google.com/file/d/1C9q14pUZPMUxfntx9Kg1xoiL6nRr332b/view
---

# Robust Policies via Mid-Level Visual Representations: An Experimental Study in Manipulation and Navigation

<a href="https://drive.google.com/file/d/1C9q14pUZPMUxfntx9Kg1xoiL6nRr332b/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="https://drive.google.com/file/d/1sks2le3ziJRRpEL3-cWzP6vKTaaie-Jn/view" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="https://github.com/alexsax/robust-policies-via-midlevel-vision" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Bryan Chen (UC Berkeley)*; Alexander Sax (UC Berkeley); Francis Lewis (Stanford); Iro Armeni (Stanford University); Silvio Savarese (Stanford University); Amir Zamir (Swiss Federal Institute of Technology (EPFL)); Jitendra Malik (University of California at Berkeley); Lerrel Pinto (NYU/Berkeley)**

#### Interactive Session
*2020-11-16, 11:10 - 11:40 PST* 

#### Abstract
Vision-based robotics often factors the control loop into separate components for perception and control. Conventional perception components usually extract hand-engineered features from the visual input that are then used by the control component in an explicit manner. In contrast, recent advances in deep RL make it possible to learn these features end-to-end during training, but the final result is often brittle, fails unexpectedly under minuscule visual shifts, and comes with a high sample complexity cost.

In this work, we study the effects of using mid-level visual representations asynchronously trained for traditional computer vision objectives as a generic and easy-to-decode perceptual state in an end-to-end RL framework. We show that the invariances provided by the mid-level representations aid generalization, improve sample complexity, and lead to a higher final performance. Compared to the alternative approaches for incorporating invariances, such as domain randomization, using asynchronously trained mid-level representations scale better to harder problems and larger domain shifts, and consequently, successfully trains policies for tasks where domain randomization or learning-from-scratch failed. Our experimental findings are reported on manipulation and navigation tasks using real robots as well as simulations. 

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1OOWYoiY48y6LD4PDWHma1N7dyX8iOnaO/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


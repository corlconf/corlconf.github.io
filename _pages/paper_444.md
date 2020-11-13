---
layout: page
title: "Visual Imitation Made Easy"
subtitle: 
description:
permalink: /paper_444/
grand_parent: All Papers
parent: Wednesday
supp: https://drive.google.com/file/d/1O6i1MD4VuxKtAQswoTmMC3atxTM6PiiH/view
code: https://github.com/sarahisyoung/Visual-Imitation-Made-Easy/
youtubeId: 
pdf: https://drive.google.com/file/d/1n_KLFTDWJ5sKrZRm2viT2TpA4lIbmy3r/view
---

# Visual Imitation Made Easy

<a href="https://drive.google.com/file/d/1n_KLFTDWJ5sKrZRm2viT2TpA4lIbmy3r/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="https://drive.google.com/file/d/1O6i1MD4VuxKtAQswoTmMC3atxTM6PiiH/view" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="https://github.com/sarahisyoung/Visual-Imitation-Made-Easy/" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Sarah Young (UC Berkeley)*; Dhiraj Gandhi (Carnegie Mellon University);  Shubham Tulsiani (Facebook AI Research); Abhinav Gupta (CMU/FAIR); Pieter Abbeel (UC Berkeley); Lerrel Pinto (NYU/Berkeley)**

#### Interactive Session
*2020-11-18, 12:30 - 13:00 PST*

#### Abstract
Visual imitation learning provides a framework for learning complex manipulation behaviors by leveraging human demonstrations. However, current interfaces for imitation such as kinesthetic teaching or teleoperation prohibitively restrict our ability to efficiently collect large-scale data in the wild. Obtaining such diverse demonstration data is paramount for the generalization of learned skills to novel scenarios. In this work, we present an alternate interface for imitation that simplifies the data collection process while allowing for easy transfer to robots. We use commercially available reacher-grabber assistive tools both as a data collection device and as the robot's end-effector. To extract action information from these visual demonstrations, we use off-the-shelf Structure from Motion (SfM) techniques in addition to training a finger detection network. We experimentally evaluate on two challenging tasks: non-prehensile pushing and prehensile stacking, with 1000 diverse demonstrations for each task. For both tasks, we use standard behavior cloning to learn executable policies from the previously collected offline demonstrations. To improve learning performance, we employ a variety of data augmentations and provide an extensive analysis of its effects. Finally, we demonstrate the utility of our interface by evaluating on real robotic scenarios with previously unseen objects and achieve a 87% success rate on pushing and a 62% success rate on stacking. Robot videos are available at our  project website: <a href="https://sites.google.com/view/visual-imitation-made-easy" target="_blank">https://sites.google.com/view/visual-imitation-made-easy</a>.

#### Video 

#### Reviews

#### Rebuttal


---
layout: page
title: "CAMPs: Learning Context-Specific Abstractions for Efficient Planning in Factored MDPs"
subtitle: 
description:
permalink: /paper_23/
grand_parent: All Papers
parent: Tuesday
supp: 
code: https://git.io/JTnf6
youtubeId: 
pdf: https://drive.google.com/file/d/1kewz9U62Eh9IbZkFhSDuN99DzWLZT7NR/view
---

# CAMPs: Learning Context-Specific Abstractions for Efficient Planning in Factored MDPs

<a href="https://drive.google.com/file/d/1kewz9U62Eh9IbZkFhSDuN99DzWLZT7NR/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="https://git.io/JTnf6" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Rohan Chitnis (Massachusetts Institute of Technology)*; Tom Silver (MIT); Beomjoon Kim (MIT); Leslie Kaelbling (MIT); Tomas Lozano-Perez (MIT)**

#### Interactive Session
*2020-11-17, 12:30 - 13:00 PST*

#### Abstract
Meta-planning, or learning to guide planning from experience, is a promising approach to improving the computational cost of planning. A general meta-planning strategy is to learn to impose constraints on the states considered and actions taken by the agent. We observe that (1) imposing a constraint can induce context-specific independences that render some aspects of the domain irrelevant, and (2) an agent can take advantage of this fact by imposing constraints on its own behavior. These observations lead us to propose the context-specific abstract Markov decision process (CAMP), an abstraction of a factored MDP that affords efficient planning. We then describe how to learn constraints to impose so the CAMP optimizes a trade-off between rewards and computational cost. Our experiments consider five planners across four domains, including robotic navigation among movable obstacles (NAMO), robotic task and motion planning for sequential manipulation, and classical planning. We find planning with learned CAMPs to consistently outperform baselines, including Stilman's NAMO-specific algorithm. Video: <a href="https://youtu.be/wTXt6djcAd4" target="_blank">https://youtu.be/wTXt6djcAd4</a> Code: <a href="https://git.io/JTnf6" target="_blank">https://git.io/JTnf6</a>

#### Video 

#### Reviews

#### Rebuttal


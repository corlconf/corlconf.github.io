---
layout: page
title: "Hierarchical Robot Navigation in Novel Environments using Rough 2-D Maps"
subtitle: 
description:
permalink: /paper_442/
grand_parent: All Papers
parent: Wednesday
supp: 
code: https://github.com/cgxuvector/ml_nav
youtube_id: xA3CrOaHzxE
pdf: https://drive.google.com/file/d/11N5huogxSrWkL_dJm67KeldVEnaMHyG9/view
---

# Hierarchical Robot Navigation in Novel Environments using Rough 2-D Maps

<a href="https://drive.google.com/file/d/11N5huogxSrWkL_dJm67KeldVEnaMHyG9/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="https://github.com/cgxuvector/ml_nav" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Chengguang Xu (Northeastern University)*; Christopher Amato (Northeastern University); Lawson Wong (Northeastern University)**

#### Interactive Session
*2020-11-18, 11:10 - 11:40 PST* 

#### Abstract
In robot navigation, generalizing quickly to unseen environments is essential.  Hierarchical methods inspired by human navigation have been proposed, typically consisting of a high-level landmark proposer and a low-level controller. However, these methods either require precise high-level information to be given in advance, or need to construct such guidance from extensive interaction with the environment. In this work, we propose an approach that leverages a rough 2-D map of the environment to navigate in novel environments without requiring further learning. In particular, we introduce a dynamic topological map that can be initialized from the rough 2-D map along with a high-level planning approach for proposing reachable 2-D map patches of the intermediate landmarks between the start and goal locations. To use proposed 2-D patches, we train a deep generative model to generate intermediate landmarks in observation space which are used as subgoals by low-level goal-conditioned reinforcement learning. Importantly, because the low-level controller is only trained with local behaviors (e.g. go across the intersection, turn left at a corner) on existing environments, this framework allows us to generalize to novel environments given only a rough 2-D map, without requiring further learning. Experimental results demonstrate the effectiveness of the proposed framework in both seen and novel environments.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1uLPFmIKNADbI_qGg_O_oI6k8nDnSt0LD/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


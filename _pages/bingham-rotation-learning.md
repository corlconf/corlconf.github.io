---
layout: page
title: Bingham Rotation Learning (RSS 2020)
subtitle:  Representing Rotations in Deep Learning
description: RSS (2020) paper on learning rotation with uncertainty
permalink: /bingham-rotation-learning/
youtubeId: 8QMcNmCPYR0
---

# A Smooth Representation of <span>SO(3)</span> for Deep Rotation Learning with Uncertainty 

[<i class="fa fa-file-text-o" aria-hidden="true"></i> arXiv pre-print ](https://arxiv.org/abs/2006.01031){: .btn .btn-blue }
[<i class="fa fa-github" aria-hidden="true"></i> View it on Github](https://github.com/utiasSTARS/bingham-rotation-learning){: .btn .btn-green }
[<i class="fa fa-newspaper-o" aria-hidden="true"></i> RSS Paper](http://www.roboticsproceedings.org/rss16/p007.html){: .btn .btn-red }
<p class="label label-yellow"><i class="fa fa-trophy" aria-hidden="true"></i> Best Student Paper Award, RSS 2020 <i class="fa fa-trophy" aria-hidden="true"></i></p>

There are many ways to represent rotations: Euler angles, rotation matrices, axis-angle vectors, or unit quaternions, for example. In deep learning, it is common to use unit quaternions for their simple geometric and alebraic structure. However, unit quaternions lack an important <strong>smoothness property</strong> that makes learning 'large' rotations difficult, and other representations are not easily amenable to learning uncertainty. In this work, we address this gap and present a smooth representation that defines a <em>belief</em> (or distribution) over rotations.

{::nomarkdown} 
<div style='text-align:center'>
<img src='/assets/bingham-rotation-learning/so3_learning.png' width='75%'>
</div>
{:/}

### A Smooth Representation of <span>SO(3)</span> for Deep Rotation Learning with Uncertainty 
#### Valentin Peretroukhin, Matthew Giamou, David M. Rosen, W. Nicholas Greene, Nicholas Roy, and Jonathan Kelly 
##### Robotics: Science and Systems (RSS) 2020
 
## Code

{::nomarkdown} 
<a target="_blank" rel="external" href="https://github.com/utiasSTARS/bingham-rotation-learning"><i class="fa fa-github-square" aria-hidden="true"></i> Available on Github</a>
{:/}

## Video
{% include youtubePlayer.html id=page.youtubeId %}


### Abstract
Accurate rotation estimation is at the heart of robot perception tasks such as visual odometry and object pose estimation. Deep learning has recently provided a new way to perform these tasks, and the choice of rotation representation is an important part of network design. 

In this work, we present a novel symmetric matrix representation of rotations that is singularity-free and requires marginal computational overhead. We show that our representation has two important properties that make it particularly suitable for learned models: (1) it satisfies a smoothness property that improves convergence and generalization when regressing large rotation targets, and (2) it encodes a symmetric Bingham belief over the space of unit quaternions, permitting the training of uncertainty-aware models. 

We empirically validate the benefits of our formulation by training deep neural rotation regressors  on two data modalities. First, we use synthetic point-cloud data to show that our representation leads to superior predictive accuracy over existing representations for arbitrary rotation targets. Second, we use vision data collected onboard ground and aerial vehicles to demonstrate that our representation is amenable to an effective out-of-distribution (OOD) rejection technique that significantly improves the robustness of rotation estimates to unseen environmental effects and corrupted input images, without requiring the use of an explicit likelihood loss, stochastic sampling, or an auxiliary classifier. This capability is key for safety-critical applications where detecting novel inputs can prevent catastrophic failure of learned models.





## Citation
<pre wrap='true'>
@inproceedings{peretroukhin_so3_2020, 
    AUTHOR    = {Valentin Peretroukhin AND Matthew Giamou AND W. Nicholas Greene AND David Rosen AND Jonathan Kelly AND Nicholas Roy}, 
    TITLE     = { {A Smooth Representation of Belief over SO(3) for Deep Rotation Learning with Uncertainty} }, 
    BOOKTITLE = {Proceedings of Robotics: Science and Systems}, 
    YEAR      = {2020}, 
    ADDRESS   = {Corvalis, Oregon, USA}, 
    MONTH     = {July}, 
    DOI       = {10.15607/RSS.2020.XVI.007} 
}
</pre>



---
layout: page
title: "Diverse Plausible Shape Completions from Ambiguous Depth Images"
subtitle: 
description:
permalink: /paper_415/
grand_parent: All Papers
parent: Monday
supp: 
code: https://github.com/UM-ARM-Lab/probabilistic_shape_completion

youtube_id: f3nLH875nik
pdf: https://drive.google.com/file/d/1vATHT3GuhjV_mRiA-M_w0E__gBwmPdjF/view
---

# Diverse Plausible Shape Completions from Ambiguous Depth Images

<a href="https://drive.google.com/file/d/1vATHT3GuhjV_mRiA-M_w0E__gBwmPdjF/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="https://github.com/UM-ARM-Lab/probabilistic_shape_completion
" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Bradley Saund (University of Michigan)*; Dmitry Berenson (University of Michigan)**

#### Interactive Session
*2020-11-16, 11:50 - 12:20 PST* 

#### Abstract
We propose PSSNet, a network architecture for generating diverse plausible 3D reconstructions from a single 2.5D depth image. Existing methods tend to produce only small variations on a single shape, even when multiple shapes are consistent with an observation. To obtain diversity we alter a Variational Auto Encoder by providing a learned shape bounding box feature as side information during training. Since these features are known during training, we are able to add a supervised loss to the encoder and noiseless values to the decoder. To evaluate, we sample a set of completions from a network, construct a set of plausible shape matches for each test observation, and compare using our plausible diversity metric defined over sets of shapes. We perform experiments using Shapenet mugs and partially-occluded YCB objects and find that our method performs comparably in datasets with little ambiguity, and outperforms existing methods when many shapes plausibly fit an observed depth image. We demonstrate one use for PSSNet on a physical robot when grasping objects in occlusion and clutter.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1-J5vfVSsx4mVNn6WD040gjsGdabdba_h/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


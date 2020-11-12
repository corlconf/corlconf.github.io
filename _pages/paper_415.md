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

youtubeId: 
---

# Diverse Plausible Shape Completions from Ambiguous Depth Images

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1vATHT3GuhjV_mRiA-M_w0E__gBwmPdjF/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Bradley Saund (University of Michigan)*; Dmitry Berenson (University of Michigan)**

#### Interactive Session
*2020-11-16, 11:50 - 12:20 PST*

#### Abstract
We propose PSSNet, a network architecture for generating diverse plausible 3D reconstructions from a single 2.5D depth image. Existing methods tend to produce only small variations on a single shape, even when multiple shapes are consistent with an observation. To obtain diversity we alter a Variational Auto Encoder by providing a learned shape bounding box feature as side information during training. Since these features are known during training, we are able to add a supervised loss to the encoder and noiseless values to the decoder. To evaluate, we sample a set of completions from a network, construct a set of plausible shape matches for each test observation, and compare using our plausible diversity metric defined over sets of shapes. We perform experiments using Shapenet mugs and partially-occluded YCB objects and find that our method performs comparably in datasets with little ambiguity, and outperforms existing methods when many shapes plausibly fit an observed depth image. We demonstrate one use for PSSNet on a physical robot when grasping objects in occlusion and clutter.

#### Video 

#### Reviews

#### Rebuttal

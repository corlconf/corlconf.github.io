---
layout: page
title: "Unsupervised Metric Relocalization Using Transform Consistency Loss"
subtitle: 
description:
permalink: /paper_389/
grand_parent: All Papers
parent: Wednesday
supp: 
code: 
youtubeId: 
---

# Unsupervised Metric Relocalization Using Transform Consistency Loss

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/14IYZ1oKJT3Uw1K9U8GB_AMcAMX-NqQJr/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Mike Kasper (University of Colorado)*; Fernando Nobre (Amazon); Christoffer Heckman (University of Colorado); Nima Keivan (Amazon)**

#### Abstract
Training networks to perform metric relocalization traditionally requires accurate image correspondences. In practice, these are obtained by restricting domain coverage, employing additional sensors, or capturing large multi-view datasets. We instead propose a self-supervised solution, which exploits a key insight: localizing a query image within a map should yield the same absolute pose, regardless of the reference image used for registration. Guided by this intuition, we derive a novel transform consistency loss. Using this loss function, we train a deep neural network to infer dense feature and saliency maps to perform robust metric relocalization in dynamic environments.  We evaluate our framework on synthetic and real-world data, showing our approach outperforms other supervised methods when a limited amount of ground-truth information is available.

#### Video 

#### Reviews

#### Rebuttal

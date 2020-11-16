---
layout: page
title: "MultiPoint: Cross-spectral registration of thermal and optical aerial imagery"
subtitle: 
description:
permalink: /paper_392/
grand_parent: All Papers
parent: Tuesday
supp: 
code: https://github.com/ethz-asl/multipoint
youtube_id: dq0O7rnn70U
pdf: https://drive.google.com/file/d/1ZLUrgdCfsXLhyW2RPgDb4ijzE8AwAfMk/view
---

# MultiPoint: Cross-spectral registration of thermal and optical aerial imagery

<a href="https://drive.google.com/file/d/1ZLUrgdCfsXLhyW2RPgDb4ijzE8AwAfMk/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="https://github.com/ethz-asl/multipoint" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Florian Achermann (ETH Zurich)*; Andrey Kolobov (Microsoft); Debadeepta Dey (Microsoft); Timo Hinzmann (ETH Zürich); Jen Jen Chung (ETH Zurich); Roland Siegwart (ETH Zürich, Autonomous Systems Lab); Nicholas Lawrance (ETH Zürich)**

#### Interactive Session
<a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SESE2BTX3IC8XZD4L" target="_blank" rel="noopener noreferrer"><em>2020-11-17, 11:10 - 11:40 PST </em></a>

#### Abstract
While optical cameras are ubiquitous in robotics, some robots can sense the world in several sections of the electromagnetic spectrum simultaneously, which can extend their capabilities in fundamental ways. For instance, many fixed-wing UAVs carry both optical and thermal imaging cameras, potentially allowing them to detect temperature difference-induced atmospheric updrafts, map their locations, and adjust their flight path accordingly to increase their time aloft. A key step for unlocking the potential offered by multi-spectral data is generating consistent, multi-spectral maps of the environment. In this work, we introduce MultiPoint, a novel data-driven method for generating interest points and associated descriptors for registering optical and thermal image pairs without knowledge of the relative camera viewpoints. Existing pixel-based alignment methods are accurate but too slow to work in near-real time, while feature-based methods such as SuperPoint are fast but produce poor-quality cross-spectral matches due to interest point instability in thermal images. MultiPoint capitalizes on the strengths of both approaches.
An offline mutual information-based procedure is used to align cross-spectral image pairs from a training set, which are then processed by our generalized multi-spectral homographic adaptation stage to generate highly repeatable interest points that are invariant across viewpoint changes in both spectra. These are used to train a MultiPoint deep neural network by exposing  this model to both same-spectrum and cross-spectral image pairs. This model is then deployed for fast and accurate online interest point detection. 
We show that MultiPoint outperforms existing techniques for feature-based image alignment using a dataset of real-world thermal-optical imagery captured by a UAV during flights in different conditions and release this dataset, the first of its kind.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1ATl6DXi0x9g_U9noxDhDJ4udx1d1BLT-/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


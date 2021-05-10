---
layout: page
title: "StrObe: Streaming Object Detection from LiDAR Packets"
subtitle: 
description:
permalink: /paper_263/
grand_parent: All Papers
parent: Wednesday
supp: https://drive.google.com/file/d/1YT34qKEg3eIrM0ZuoQ8Di_3cCyG1gO7h/view
code: 
youtube_id: Gy97AnWdGn8
pdf: https://drive.google.com/file/d/1BLmWnwNG9gzyWz9NecloLwD6vJkh1t_Y/view
---

# StrObe: Streaming Object Detection from LiDAR Packets

<a href="https://drive.google.com/file/d/1BLmWnwNG9gzyWz9NecloLwD6vJkh1t_Y/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="https://drive.google.com/file/d/1YT34qKEg3eIrM0ZuoQ8Di_3cCyG1gO7h/view" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Davi Frossard (Uber Advanced Technologies Group / University of Toronto)*; Shun Da Suo (Uber ATG, University of Toronto); Sergio Casas (University of Toronto); James Tu (Uber ATG); Raquel Urtasun (Uber ATG)**

#### Interactive Session
<em>2020-11-18, 11:50 - 12:20 PST </em> | <a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SES27I1KMZDXRT9VU" target="_blank" rel="noopener noreferrer"> PheedLoop Session <i class="fa fa-external-link" aria-hidden="true"></i> </a> 

#### Abstract
Many modern robotics systems employ LiDAR as their main sensing modality due to its geometrical richness. Rolling shutter LIDARs are particularly common, in which a sweep is built through the accumulation of points over an entire revolution of the sensor, thus producing a 360 point cloud of the scene. Modern perception algorithms wait for the full sweep to be built before processing the data, which introduces an additional latency of up to 100ms. As a consequence, by the time an output is produced, it no longer accurately reflects the state of the world. This poses a big challenge, as robotics applications require minimal reaction times, such that maneuvers can be quickly planned in the event of a safety-critical situation. In this paper we propose StrObe, a novel approach that minimizes latency by ingesting packets of LiDAR and emitting a stream of detections without waiting for the full sweep to be built. StrObe reuses computations from previous points and iteratively updates the spatial memory of the scene as new evidence comes in, resulting in latency reduced accurate perception. We demonstrate the effectiveness of our approach on a large scale dataset, showing that our approach far outperforms the state-of-the-art when latency is taken into account while still matching the performance in the traditional setting.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/12WqMV488Q53zvmHfqqnVy2XkrnGrxr0p/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


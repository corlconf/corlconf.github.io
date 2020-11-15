---
layout: page
title: "SAM: Squeeze-and-Mimic Networks for Conditional Visual Driving Policy Learning"
subtitle: 
description:
permalink: /paper_40/
grand_parent: All Papers
parent: Tuesday
supp: 
code: https://github.com/twsq/sam-driving
youtube_id: ipKAMzmJpMs
pdf: https://drive.google.com/file/d/1VVWsMR2MJ1q3Jknxe1QDHmnN37TpQzy8/view
---

# SAM: Squeeze-and-Mimic Networks for Conditional Visual Driving Policy Learning

<a href="https://drive.google.com/file/d/1VVWsMR2MJ1q3Jknxe1QDHmnN37TpQzy8/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="https://github.com/twsq/sam-driving" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Albert Zhao (UCLA)*; Tong He (UCLA); Yitao Liang (UCLA); Haibin Huang (Kuaishou Technology); Guy Van den Broeck (UCLA); Stefano Soatto (UCLA)**

#### Interactive Session
*2020-11-17, 11:50 - 12:20 PST* 

#### Abstract
We describe a policy learning approach to map visual inputs to driving controls conditioned on turning command that leverages side tasks on semantics and object affordances via a learned representation trained for driving. To learn this representation, we train a squeeze network to drive using annotations for the side task as input. This representation encodes the driving-relevant information associated with the side task while ideally throwing out side task-relevant but driving-irrelevant nuisances. We then train a mimic network to drive using only images as input and use the squeeze network's latent representation to supervise the mimic network via a mimicking loss. Notably, we do not aim to achieve the side task nor to learn features for it; instead, we aim to learn, via the mimicking loss, a representation of the side task annotations directly useful for driving. We test our approach using the CARLA simulator. In addition, we introduce a more challenging but realistic evaluation protocol that considers a run that reaches the destination successful only if it does not violate common traffic rules.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1lrStoIW3_cJ8vaKRfB0T14f_kb_y695d/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


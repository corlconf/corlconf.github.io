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
youtubeId: 
---

# SAM: Squeeze-and-Mimic Networks for Conditional Visual Driving Policy Learning

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1VVWsMR2MJ1q3Jknxe1QDHmnN37TpQzy8/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Albert Zhao (UCLA)*; Tong He (UCLA); Yitao Liang (UCLA); Haibin Huang (Kuaishou Technology); Guy Van den Broeck (UCLA); Stefano Soatto (UCLA)**

#### Abstract
We describe a policy learning approach to map visual inputs to driving controls conditioned on turning command that leverages side tasks on semantics and object affordances via a learned representation trained for driving. To learn this representation, we train a squeeze network to drive using annotations for the side task as input. This representation encodes the driving-relevant information associated with the side task while ideally throwing out side task-relevant but driving-irrelevant nuisances. We then train a mimic network to drive using only images as input and use the squeeze network's latent representation to supervise the mimic network via a mimicking loss. Notably, we do not aim to achieve the side task nor to learn features for it; instead, we aim to learn, via the mimicking loss, a representation of the side task annotations directly useful for driving. We test our approach using the CARLA simulator. In addition, we introduce a more challenging but realistic evaluation protocol that considers a run that reaches the destination successful only if it does not violate common traffic rules.

#### Video 

#### Reviews

#### Rebuttal

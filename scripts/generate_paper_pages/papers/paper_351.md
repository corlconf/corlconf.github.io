---
layout: page
title: "Learning Hierarchical Task Networks with Preferences from Unannotated Demonstrations"
subtitle: 
description:
permalink: /paper_351/
grand_parent: All Papers
parent: Tuesday
supp: https://drive.google.com/file/d/1i2NWHoTT6Ws7YT6Hsb1u3Gii_oKzSyzZ/view
code: https://github.com/GT-RAIL/circuit_htn
youtube_id: bLQ0ZZqtT0s
pdf: https://drive.google.com/file/d/18MBP2D4BgOAsKjEW9DEqRb8v2ugx1nwQ/view
---

# Learning Hierarchical Task Networks with Preferences from Unannotated Demonstrations

<a href="https://drive.google.com/file/d/18MBP2D4BgOAsKjEW9DEqRb8v2ugx1nwQ/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="https://drive.google.com/file/d/1i2NWHoTT6Ws7YT6Hsb1u3Gii_oKzSyzZ/view" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="https://github.com/GT-RAIL/circuit_htn" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Kevin  Chen (Georgia Institute of Technology); Nithin Shrivatsav Srikanth (Georgia Institute of Technology); David Kent (Georgia Institute of Technology)*; Harish Ravichandar (Georgia Institute of Technology); Sonia Chernova (Georgia Institute of Technology	)**

#### Interactive Session
<em>2020-11-17, 12:30 - 13:00 PST </em> | <a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SES8P6MJ8SWM7LBC0" target="_blank" rel="noopener noreferrer"> PheedLoop Session <i class="fa fa-external-link" aria-hidden="true"></i> </a> 

#### Abstract
We address the problem of learning Hierarchical Task Networks (HTNs) from unannotated task demonstrations, while retaining action execution preferences present in the demonstration data.  We show that the problem of learning a complex HTN structure can be made analogous to the problem of series/parallel reduction of resistor networks, a foundational concept in Electrical Engineering.  Based on this finding, we present the CircuitHTN algorithm, which constructs an action graph representing the demonstrations, and then reduces the graph following rules for reducing combination electrical circuits. Evaluation on real-world household kitchen tasks shows that CircuitHTN outperforms prior work in task structure and preference learning, successfully handling large data sets and exhibiting similar action selection preferences as the demonstrations.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1aGTQNixMWXQOje-dgVWZ2Kn0ZfZFkYaE/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


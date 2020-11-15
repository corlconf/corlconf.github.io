---
layout: page
title: "Few-shot Object Grounding and Mapping for Natural Language Robot Instruction Following"
subtitle: 
description:
permalink: /paper_417/
grand_parent: All Papers
parent: Monday
supp: 
code: https://github.com/lil-lab/drif/tree/fewshot2020
youtube_id: iIyO2a8MCyE
pdf: https://drive.google.com/file/d/14IuMBuWKW0ZPhVMc17slpg5OJNdoQRk6/view
---

# Few-shot Object Grounding and Mapping for Natural Language Robot Instruction Following

<a href="https://drive.google.com/file/d/14IuMBuWKW0ZPhVMc17slpg5OJNdoQRk6/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="https://github.com/lil-lab/drif/tree/fewshot2020" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Valts Blukis (Cornell University)*; Ross Knepper (Cornell University); Yoav Artzi (Cornell University)**

#### Interactive Session
*2020-11-16, 12:30 - 13:00 PST* 

#### Abstract
We study the problem of learning a robot policy to follow natural language instructions that can be easily extended to reason about new objects. We introduce a few-shot language-conditioned object grounding method trained from augmented reality data that uses exemplars to identify objects and align them to their mentions in instructions. We present a learned map representation that encodes object locations and their instructed use, and construct it from our few-shot grounding output. We integrate this mapping approach into an instruction-following policy, thereby allowing it to  reason about previously unseen objects at test-time by simply adding exemplars. We evaluate on the task of learning to map raw observations and instructions to continuous control of a physical quadcopter. Our approach significantly outperforms the prior state of the art in the presence of new objects, even when the prior approach observes all objects during training.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1jG4jH1w2sAPF7T14tTZXN3RHUSRxzoiJ/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


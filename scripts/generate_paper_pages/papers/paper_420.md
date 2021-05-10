---
layout: page
title: "Deep Latent Competition: Learning to Race Using Visual Control Policies in Latent Space"
subtitle: 
description:
permalink: /paper_420/
grand_parent: All Papers
parent: Monday
supp: 
code: https://sites.google.com/view/deep-latent-competition
youtube_id: wYjv0vmq3o0
pdf: https://drive.google.com/file/d/1WLenYQ2yaMYKxI0sH9XEvOxGWnt74RIx/view
---

# Deep Latent Competition: Learning to Race Using Visual Control Policies in Latent Space

<a href="https://drive.google.com/file/d/1WLenYQ2yaMYKxI0sH9XEvOxGWnt74RIx/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="https://sites.google.com/view/deep-latent-competition" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Wilko Schwarting (Massachusetts Institute of Technology)*; Tim Seyde (MIT); Igor Gilitschenski (Massachusetts Institute of Technology); Lucas Liebenwein (Massachusetts Institute of Technology); Ryan Sander (Massachusetts Institute of Technology); Sertac Karaman (Massachusetts Institute of Technology); Daniela Rus (Massachusetts Institute of Technology)**

#### Interactive Session
<em>2020-11-16, 12:30 - 13:00 PST </em> | <a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SESXIWWPF709DJ5DR" target="_blank" rel="noopener noreferrer"> PheedLoop Session <i class="fa fa-external-link" aria-hidden="true"></i> </a> 

#### Abstract
Learning competitive behaviors in multi-agent settings such as racing requires long-term reasoning about potential adversarial interactions. This paper presents Deep Latent Competition (DLC), a novel reinforcement learning algorithm that learns competitive visual control policies through self-play in imagination. The DLC agent imagines multi-agent interaction sequences in the compact latent space of a learned world model that combines a joint transition function with opponent viewpoint prediction. Imagined self-play reduces costly sample generation in the real world, while the latent representation enables planning to scale gracefully with observation dimensionality.  We demonstrate the effectiveness of our algorithm in learning competitive behaviors on a novel multi-agent racing benchmark that requires planning from image observations. Code and videos available at <a href="https://sites.google.com/view/deep-latent-competition" target="_blank">https://sites.google.com/view/deep-latent-competition</a>.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1UY8CmXuERj8wZgcK22GBSJxheVRhuBSF/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


---
layout: page
title: "Multi-Modal Anomaly Detection for Unstructured and Uncertain Environments"
subtitle: 
description:
permalink: /paper_324/
grand_parent: All Papers
parent: Wednesday
supp: 
code: https://github.com/tianchenji/Multimodal-SVAE
youtube_id: 
pdf: https://drive.google.com/file/d/1PIdenJv-TtQGpby5kJb8VgXRBX8QxGeF/view
---

# Multi-Modal Anomaly Detection for Unstructured and Uncertain Environments

<a href="https://drive.google.com/file/d/1PIdenJv-TtQGpby5kJb8VgXRBX8QxGeF/view" target="_blank" rel="noopener noreferrer" class="btn btn-blue"><i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF </a> {% if page.supp %}<a href="" target="_blank" rel="noopener noreferrer" class="btn btn-green"><i class="fa fa-file-text-o" aria-hidden="true"></i> Supplemental </a>{% endif %} {% if page.code %}<a href="https://github.com/tianchenji/Multimodal-SVAE" target="_blank" rel="noopener noreferrer" class="btn"><i class="fa fa-github" aria-hidden="true"></i> Code </a>{% endif %} 

#### Authors
**Tianchen Ji (University of Illinois at Urbana-Champaign)*; Sri Theja Vuppala (University of Illinois at Urbana-Champaign); Girish Chowdhary (University of Illinois at Urbana Champaign); Katherine Driggs-Campbell (University of Illinois at Urbana-Champaign)**

#### Interactive Session
<em>2020-11-18, 11:10 - 11:40 PST </em> | <a href="https://pheedloop.com/corl2020/virtual/?page=sessions&section=SESR19FI8URTPNA8K" target="_blank" rel="noopener noreferrer"> PheedLoop Session <i class="fa fa-external-link" aria-hidden="true"></i> </a> 

#### Abstract
To achieve high-levels of autonomy, modern robots require the ability to detect and recover from anomalies and failures with minimal human supervision. Multi-modal sensor signals could provide more information for such anomaly detection tasks; however, the fusion of high-dimensional and heterogeneous sensor modalities remains a challenging problem. We propose a deep learning neural network: supervised variational autoencoder (SVAE), for failure identification in unstructured and uncertain environments. Our model leverages the representational power of VAE to extract robust features from high-dimensional inputs for supervised learning tasks. The training objective unifies the generative model and the discriminative model, thus making the learning a one-stage procedure. Our experiments on real field robot data demonstrate superior failure identification performance than baseline methods, and that our model learns interpretable representations.

#### Video
{% if page.youtube_id %}
{% include youtubePlayer.html id=page.youtube_id %}
{% endif %}

#### Reviews and Rebuttal
<a href="https://drive.google.com/file/d/1-w7jWdXwuPTtsZ5Reg8MUXuW-QR3rdff/view" target="_blank" rel="noopener noreferrer" class="btn btn-purple"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Reviews & Rebuttal </a>


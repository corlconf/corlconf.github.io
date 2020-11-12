---
layout: page
title: "Generalization Guarantees for Imitation Learning"
subtitle: 
description:
permalink: /paper_322/
grand_parent: All Papers
parent: Wednesday
supp: 
code: https://github.com/irom-lab/PAC-Imitation
youtubeId: 
---

# Generalization Guarantees for Imitation Learning

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1SfN2vBg_pQm1UYjm8YgJnrO34mUAxPLr/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Allen Ren (Princeton University)*; Sushant Veer (Princeton University); Anirudha Majumdar (Princeton University)**

#### Interactive Session
*2020-11-18, 12:30 - 13:00 PST*

#### Abstract
Control policies from imitation learning can often fail to generalize to novel environments due to imperfect demonstrations or the inability of imitation learning algorithms to accurately infer the expert’s policies. In this paper, we present rigorous generalization guarantees for imitation learning by leveraging the Probably Approximately Correct (PAC)-Bayes framework to provide upper bounds on the expected cost of policies in novel environments. We propose a two-stage training method where a latent policy distribution is ﬁrst embedded with multi-modal expert behavior using a conditional variational autoencoder, and then “ﬁne-tuned” in new training environments to explicitly optimize the generalization bound. We demonstrate strong generalization bounds and their tightness relative to empirical performance in simulation for (i) grasping diverse mugs, (ii) planar pushing with visual feedback, and (iii) vision-based indoor navigation, as well as through hardware experiments for the two manipulation tasks.

#### Video 

#### Reviews

#### Rebuttal

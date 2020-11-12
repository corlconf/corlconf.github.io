---
layout: page
title: "The RobotSlang Benchmark: Dialog-guided Robot Localization and Navigation"
subtitle: 
description:
permalink: /paper_297/
grand_parent: All Papers
parent: Monday
supp: 
code: https://github.com/MichiganCOG/RobotSlangBenchmark
youtubeId: 
---

# The RobotSlang Benchmark: Dialog-guided Robot Localization and Navigation

[<i class="fa fa-file-text-o" aria-hidden="true"></i> Paper PDF ](https://drive.google.com/file/d/1VbIQOSifKFhyWwISUpunnTOAeL_WNrRX/view){: .btn .btn-blue } {% if page.supp %} [<i class="fa fa-file-text-o" aria-hidden="true"></i> Supplementary ]({{ page.supp }}){: .btn .btn-green } {% endif %} {% if page.code %} [<i class="fa fa-github" aria-hidden="true"></i> Code]({{ page.code }}){: .btn .btn-red }
{% endif %}

#### Authors
**Shurjo Banerjee (University of Michigan)*; Jesse Thomason (University of Washington); Jason Corso (University of Michigan)**

#### Abstract
Autonomous robot systems for applications from search and rescue to assistive guidance should be able to engage in natural language dialog with people. To study such cooperative communication, we introduce Robot Simultaneous Localization and Mapping with Natural Language (RobotSlang), a benchmark of 169 natural language dialogs between a human Driver controlling a robot and a human Commander providing guidance towards navigation goals. In each trial, the pair first cooperates to localize the robot on a global map visible to the Commander, then the Driver follows Commander instructions to move the robot to a sequence of target objects. We introduce a Localization from Dialog History (LDH) and a Navigation from Dialog History (NDH) task where a learned agent is given dialog and visual observations from the robot platform as input and must localize in the global map or navigate towards the next target object, respectively. RobotSlang is comprised of nearly 5k utterances and over 1k minutes of robot camera and control streams. We present an initial model for the NDH task, and show that an agent trained in simulation can follow the RobotSlang dialog-based navigation instructions for controlling a physical robot platform. Code and data are available at <a href="https://umrobotslang.github.io/" target="_blank">https://umrobotslang.github.io/</a>.

#### Video 

#### Reviews

#### Rebuttal

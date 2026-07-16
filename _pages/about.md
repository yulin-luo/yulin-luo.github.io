---
permalink: /
title: "Yulin Luo - Homepage"
excerpt: "PhD student at Peking University. Research on open-world generalization for embodied intelligence."
author_profile: true
redirect_from:
  - /about/
  - /about.html
header:
  og_image: images/lyl_photo.png     # 站外分享（Google/微信）用图
  teaser: images/lyl_photo.png        # 站内缩略图
---

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">

<span class='anchor' id='about-me'></span>
My name is <span class="author-highlight">Yulin Luo</span> (罗峪霖). I'm a PhD student (since 2023) at the <a href="https://cs.pku.edu.cn/" class="link-accent">School of Computer Science</a>, **Peking University**, advised by Assistant Professor <a href="https://scholar.google.cz/citations?user=voqw10cAAAAJ&hl=zh-CN" class="link-accent">Shanghang Zhang</a>. I received my Bachelor's degree in Automation from **Shanghai Jiao Tong University** in 2023. My current vision is <span class="accent-text">open-world generalization for embodied intelligence</span>. More details are available in my <a href="/files/Yulin_Luo_CV.pdf" class="link-accent"><i class="fas fa-file-pdf"></i> curriculum vitae</a>.

<details class="quick-jump-nav">
  <summary aria-label="Open section navigation">
    <i class="fas fa-compass"></i>
    <span>Jump</span>
  </summary>
  <nav aria-label="Quick section navigation">
    <a href="#about-me"><i class="fas fa-arrow-up"></i><span>Top</span></a>
    <a href="#news"><i class="fas fa-fire"></i><span>News</span></a>
    <a href="#education"><i class="fas fa-graduation-cap"></i><span>Education</span></a>
    <a href="#experience"><i class="fas fa-briefcase"></i><span>Experience</span></a>
    <a href="#publications"><i class="fas fa-file-lines"></i><span>Publications</span></a>
    <a href="#awards"><i class="fas fa-trophy"></i><span>Awards</span></a>
    <a href="#services"><i class="fas fa-glasses"></i><span>Services</span></a>
  </nav>
</details>


<div class="profile-summary-stack">
  <div class="highlight-block floating-card research-profile-card">
    <h3><i class="fas fa-robot"></i> Embodied Researcher</h3>
    <ul>
      <li><span class="primary-gradient-text">Generalizable models</span>:
        designing architectures and learning algorithms for embodied foundation models that generalize across objects, skills, embodiments, scenes, and tasks.
        <div class="profile-evidence-links">
          <a href="#pub-deepvision-vla">DeepVision-VLA <span>ACM MM'26</span></a>
          <a href="#pub-moase">MoASE <span>AAAI'26 Oral</span></a>
        </div>
      </li>
      <li><span class="primary-gradient-text">Goal-aligned benchmarks</span>:
        evaluating model capabilities under realistic conditions and against the long-term goal of open-world robot intelligence.
        <div class="profile-evidence-links">
          <a href="#pub-robobench">RoboBench <span>ECCV'26</span></a>
        </div>
      </li>
      <li><span class="primary-gradient-text">Evaluation-driven co-evolution</span>:
        turning diagnosed gaps into model and data redesign, then using improved models and data to define the next evaluation cycle.
        <div class="profile-evidence-links">
          <a href="#pub-ssd-llm">SSD-LLM <span>ECCV'24</span></a>
        </div>
      </li>
    </ul>
    <figure class="generalization-figure">
      <img src="images/open_world_generalization_teaser_en.webp" alt="Open-world generalization hierarchy for embodied intelligence" width="1648" height="893" decoding="async" fetchpriority="high">
    </figure>
  </div>
</div>

<span class='anchor' id='news'></span>
# 🔥 News
<div class="news-panel" markdown="1">

- *2026.07*: &nbsp;🎉 <b><a class="news-paper-link" href="#pub-deepvision-vla">DeepVision-VLA</a></b>, a vision-representation enhancement method for VLA models, is accepted to <span class="accent-text">ACM MM 2026</span>. (first author)
- *2026.07*: &nbsp;🎉 <b><a class="news-paper-link" href="#pub-robobench">RoboBench</a></b> is included in the official evaluation suite of <a class="news-paper-link" href="https://github.com/Tencent-Hunyuan/HY-Embodied" target="_blank" rel="noopener">HY-Embodied</a>, with <span class="accent-text">RoboBench-MCQ</span> and <span class="accent-text">RoboBench-Planning</span> reported for HY-Embodied-0.5 and Hy-Embodied-VLM-1.0.
- *2026.07*: &nbsp;🎉 <b><a class="news-paper-link" href="#pub-robobench">RoboBench</a></b>, a robot-scenario benchmark for evaluating MLLMs as embodied brains, is accepted to <span class="accent-text">ECCV 2026</span>. (first author)
- *2025.11*: &nbsp;🎉 <b><a class="news-paper-link" href="#pub-moase">MoASE</a></b>, a sparse MoE adaptation method for robust continual test-time vision models, is accepted as <span class="news-highlight-oral">Oral</span> at <span class="accent-text">AAAI 2026</span>. (co-first author)
- *2025.09*: &nbsp;🎉 <a class="news-paper-link" href="#pub-seear1">SEEA-R1</a>, a tree-structured RL fine-tuning method for self-evolving embodied agents, is accepted to <span class="accent-text">NeurIPS 2025</span>.
- *2025.04*: &nbsp;🎉 <a class="news-paper-link" href="#pub-robomind">RoboMIND</a>, a multi-embodiment robot manipulation benchmark with normative data, is accepted to <span class="accent-text">RSS 2025</span>.
- *2025.01*: &nbsp;🎉 <a class="news-paper-link" href="#pub-draw-and-understand">Draw-and-Understand</a>, a visual-prompt method that helps MLLMs understand user intent, is accepted to <span class="accent-text">ICLR 2025</span>.
- *2024.07*: &nbsp;🎉 <b><a class="news-paper-link" href="#pub-ssd-llm">SSD-LLM</a></b>, an LLM-based dataset analyst for discovering subpopulation structure, is accepted to <span class="accent-text">ECCV 2024</span>. (first author)
- *2023.12*: &nbsp;🎉 <b><a class="news-paper-link" href="#pub-mofme">MoFME</a></b>, an uncertainty-aware mixture-of-experts method for efficient image deweathering, is accepted to <span class="accent-text">AAAI 2024</span>.
- *2023.09*: &nbsp;🎓 Started PhD at Peking University, advised by Prof. Shanghang Zhang.
- *2023.06*: &nbsp;🎓 Graduated with B.Eng. in Automation from Shanghai Jiao Tong University.
- *2022.06*: &nbsp;🎉 <b><a class="news-paper-link" href="#pub-randstainna">RandStainNA</a></b>, a stain augmentation and normalization method for robust histology slide features, is accepted to <span class="accent-text">MICCAI 2022</span>. (co-first author)

</div>

<span class='anchor' id='education'></span>
# 🏫 Education
<div class="credential-list">
  <div class="credential-card floating-card">
    <div class="credential-period"><i class="fas fa-calendar-days"></i> 2023.09 - Present</div>
    <img class="credential-logo" src="images/pku-logo-official.png" alt="Peking University logo" width="360" height="360" decoding="async" loading="lazy">
    <div class="credential-content">
      <h3>Peking University</h3>
      <div class="credential-line"><i class="fas fa-graduation-cap"></i><span>Ph.D. Candidate</span></div>
      <div class="credential-line"><i class="fas fa-building-columns"></i><span>School of Computer Science</span></div>
      <div class="credential-line"><i class="fas fa-user-tie"></i><span>Advisor: Assistant Professor <a href="https://scholar.google.cz/citations?user=voqw10cAAAAJ&hl=zh-CN" class="link-accent">Shanghang Zhang</a></span></div>
    </div>
  </div>
  <div class="credential-card floating-card">
    <div class="credential-period"><i class="fas fa-calendar-days"></i> 2019.09 - 2023.06</div>
    <img class="credential-logo" src="images/sjtu-logo-official.svg" alt="Shanghai Jiao Tong University logo" width="75" height="75" decoding="async" loading="lazy">
    <div class="credential-content">
      <h3>Shanghai Jiao Tong University</h3>
      <div class="credential-line"><i class="fas fa-graduation-cap"></i><span>B.Eng. in Automation</span></div>
      <div class="credential-line"><i class="fas fa-chart-line"></i><span>GPA: 3.87/4.30; Major rank: 2/89.</span></div>
    </div>
  </div>
</div>

<span class='anchor' id='experience'></span>
# 💼 Research Experience
<div class="experience-list">
  <div class="experience-card floating-card">
    <div class="experience-period"><i class="fas fa-calendar-days"></i> 2025.12 - Present</div>
    <img class="experience-logo" src="images/simplexity-logo.svg" alt="Simplexity Robotics logo" width="80" height="21" decoding="async" loading="lazy">
    <div class="experience-content">
      <h3><a href="https://www.simplexityrobotics.com/" class="link-accent">Simplexity Robotics</a> <span class="cn-name">(至简动力)</span></h3>
      <div class="credential-line"><i class="fas fa-briefcase"></i><span>Research Intern</span></div>
      <div class="credential-line"><i class="fas fa-robot"></i><span>Embodied intelligence and generalizable robot foundation models.</span></div>
    </div>
  </div>
  <div class="experience-card floating-card">
    <div class="experience-period"><i class="fas fa-calendar-days"></i> 2024.08 - 2025.10</div>
    <img class="experience-logo" src="images/baai-logo.png" alt="BAAI logo" width="80" height="80" decoding="async" loading="lazy">
    <div class="experience-content">
      <h3><a href="https://www.baai.ac.cn/zh-cn/research" class="link-accent">Beijing Academy of Artificial Intelligence (BAAI)</a></h3>
      <div class="credential-line"><i class="fas fa-briefcase"></i><span>Research Intern</span></div>
      <div class="credential-line"><i class="fas fa-brain"></i><span>Embodied-brain benchmarks for multimodal large language models and robot intelligence.</span></div>
    </div>
  </div>
  <div class="experience-card floating-card">
    <div class="experience-period"><i class="fas fa-calendar-days"></i> 2024.03 - 2024.08</div>
    <img class="experience-logo" src="images/bytedance-logo.ico" alt="ByteDance logo" width="300" height="300" decoding="async" loading="lazy">
    <div class="experience-content">
      <h3><a href="https://www.bytedance.com/zh/" class="link-accent">ByteDance</a></h3>
      <div class="credential-line"><i class="fas fa-briefcase"></i><span>Research Intern</span></div>
      <div class="credential-line"><i class="fas fa-shield-halved"></i><span>Trust & Safety Applied Algorithm Team for Ads and E-commerce.</span></div>
    </div>
  </div>
</div>

<span class='anchor' id='publications'></span>
# 📃 Publications

<section class="research-trajectory floating-card" aria-labelledby="research-trajectory-title">
  <div class="trajectory-heading">
    <div>
      <h2 id="research-trajectory-title">Research Trajectory</h2>
      <p>Selected first / co-first works since 2024. Hollow dots mark arXiv v1 release; solid dots mark acceptance.</p>
    </div>
    <div class="trajectory-legend" aria-label="Timeline legend">
      <span><i class="dot dot-arxiv"></i> arXiv v1</span>
      <span><i class="dot dot-accepted"></i> Accepted</span>
      <span><i class="dot dot-highlight"></i> Oral / highlight</span>
    </div>
  </div>
  <div class="trajectory-axis" aria-hidden="true">
    <span class="axis-year axis-start" style="left: 0%">2024</span>
    <span class="axis-month" style="left: 5.6%">03</span>
    <span class="axis-month" style="left: 13.9%">06</span>
    <span class="axis-month" style="left: 22.2%">09</span>
    <span class="axis-month" style="left: 30.6%">12</span>
    <span class="axis-year" style="left: 33.3%">2025</span>
    <span class="axis-month" style="left: 38.9%">03</span>
    <span class="axis-month" style="left: 47.2%">06</span>
    <span class="axis-month" style="left: 55.6%">09</span>
    <span class="axis-month" style="left: 63.9%">12</span>
    <span class="axis-year" style="left: 66.7%">2026</span>
    <span class="axis-month" style="left: 72.2%">03</span>
    <span class="axis-month" style="left: 80.6%">06</span>
    <span class="axis-month" style="left: 88.9%">09</span>
    <span class="axis-month" style="left: 97.2%">12</span>
  </div>
  <div class="trajectory-lanes">
    <div class="trajectory-lane">
      <div class="lane-label"><i class="fas fa-microchip"></i><span>Model</span></div>
      <div class="lane-track">
        <a class="trajectory-link trajectory-span" href="#pub-moase" style="--start:11.1%; --end:61.1%; --mid:36.1%; --y:34%;" title="MoASE: arXiv v1 2024.05 → AAAI Oral acceptance 2025.11">
          <span class="timeline-label label-above" style="left: var(--mid);">MoASE <span class="timeline-venue">(AAAI'26 Oral)</span></span>
          <span class="span-line"></span>
          <span class="timeline-dot arxiv-dot" style="left: var(--start);"></span>
          <span class="timeline-dot accepted-dot highlight-dot" style="left: var(--end);"></span>
        </a>
        <a class="trajectory-link trajectory-span" href="#pub-deepvision-vla" style="--start:72.2%; --end:83.3%; --mid:77.8%; --y:72%;" title="DeepVision-VLA: arXiv v1 2026.03 → ACM MM 2026 acceptance 2026.07">
          <span class="timeline-label label-below" style="left: var(--mid);">DeepVision-VLA <span class="timeline-venue">(ACM MM'26)</span></span>
          <span class="span-line"></span>
          <span class="timeline-dot arxiv-dot" style="left: var(--start);"></span>
          <span class="timeline-dot accepted-dot" style="left: var(--end);"></span>
        </a>
      </div>
    </div>
    <div class="trajectory-lane">
      <div class="lane-label"><i class="fas fa-clipboard-check"></i><span>Evaluation</span></div>
      <div class="lane-track">
        <a class="trajectory-link trajectory-span" href="#pub-robomind" style="--start:30.6%; --end:41.7%; --mid:36.1%; --y:34%;" title="RoboMIND: arXiv v1 2024.12 → RSS 2025 acceptance 2025.04">
          <span class="timeline-label label-above" style="left: var(--mid);">RoboMIND <span class="timeline-venue">(RSS'25)</span></span>
          <span class="span-line"></span>
          <span class="timeline-dot arxiv-dot" style="left: var(--start);"></span>
          <span class="timeline-dot accepted-dot" style="left: var(--end);"></span>
        </a>
        <a class="trajectory-link trajectory-span" href="#pub-robobench" style="--start:58.3%; --end:83.3%; --mid:70.8%; --y:72%;" title="RoboBench: arXiv v1 2025.10 → ECCV 2026.07">
          <span class="timeline-label label-below" style="left: var(--mid);">RoboBench <span class="timeline-venue">(ECCV'26)</span></span>
          <span class="span-line"></span>
          <span class="timeline-dot arxiv-dot" style="left: var(--start);"></span>
          <span class="timeline-dot accepted-dot" style="left: var(--end);"></span>
        </a>
      </div>
    </div>
    <div class="trajectory-lane trajectory-lane-compact">
      <div class="lane-label"><i class="fas fa-arrows-rotate"></i><span>Model-Data Co-evolution</span></div>
      <div class="lane-track">
        <a class="trajectory-link trajectory-span" href="#pub-ssd-llm" style="--start:11.1%; --end:16.7%; --mid:13.9%; --y:50%;" title="SSD-LLM: arXiv v1 2024.05 → ECCV 2024 acceptance 2024.07">
          <span class="timeline-label label-above" style="left: var(--mid);">SSD-LLM <span class="timeline-venue">(ECCV'24)</span></span>
          <span class="span-line"></span>
          <span class="timeline-dot arxiv-dot" style="left: var(--start);"></span>
          <span class="timeline-dot accepted-dot" style="left: var(--end);"></span>
        </a>
      </div>
    </div>
  </div>
</section>

<!-- ⭐️ = (共同)第一作者；📧 = 通讯作者。teaser 图默认用占位图 images/500x300.png，
     你把每篇的图放到 images/ 后替换 src 即可。缺 arXiv 链接的用 "#" 占位，后续补。 -->
<div id="publications-wrapper">
  <div id="filter-container" class="filter-bar">
    <div class="filter-group">
      <label for="filter-author">Author Role</label>
      <select id="filter-author" data-dim="author">
        <option value="">All</option>
        <option value="First Author">First author</option>
        <option value="Co-First Author">Co-first author</option>
        <option value="Other">Other</option>
      </select>
    </div>
    <div class="filter-group">
      <label for="filter-venue">Venue Tier</label>
      <select id="filter-venue" data-dim="venue">
        <option value="">All</option>
        <option value="CCF-A">CCF-A</option>
        <option value="CCF-B">CCF-B</option>
      </select>
    </div>
    <div class="filter-group">
      <label for="filter-type">Publication Type</label>
      <select id="filter-type" data-dim="type">
        <option value="">All</option>
        <option value="Conference">Conference</option>
        <option value="Preprint">Preprint</option>
      </select>
    </div>
    <div class="filter-group">
      <label for="filter-highlight">Highlight</label>
      <select id="filter-highlight" data-dim="highlight">
        <option value="">All</option>
        <option value="Oral">Oral Presentation</option>
      </select>
    </div>
    <div class="filter-group">
      <label for="filter-domain">Domain</label>
      <select id="filter-domain" data-dim="domain">
        <option value="">All</option>
        <option value="Embodied AI">Embodied AI</option>
        <option value="Computer Vision">Computer Vision</option>
        <option value="Medical Imaging">Medical Imaging</option>
        <option value="Data-centric AI">Data-centric AI</option>
      </select>
    </div>
    <div class="filter-group">
      <label for="filter-focus">Focus</label>
      <select id="filter-focus" data-dim="focus">
        <option value="">All</option>
        <option value="VLA">VLA</option>
        <option value="Benchmark">Benchmark</option>
        <option value="Agentic">Agentic</option>
        <option value="World Model">World Model</option>
        <option value="MoE">MoE</option>
        <option value="Data Augmentation">Data Augmentation</option>
        <option value="MLLM">MLLM</option>
      </select>
    </div>
    <button id="filter-reset" class="filter-reset-btn">Reset</button>
  </div>

  <div id="pub-robobench" class='paper-box floating-card' data-order="20251017801" data-tags="First Author, Conference, CCF-B, Embodied AI, Benchmark">
    <div class='paper-box-image paper-box-image-duo'>
      <div class="badge pulse-accent">ECCV 2026</div>
      <a class="paper-image-link" href="images/robobench.png" aria-label="Open full-size RoboBench teaser">
        <img src='images/robobench.webp' alt="RoboBench teaser" width="1800" height="1128" decoding="async" loading="lazy">
      </a>
      <div class="paper-image-caption"><span>Teaser</span>Benchmark overview across embodied abilities</div>
      <a class="paper-image-link" href="images/robobench-method.png" aria-label="Open full-size RoboBench construction pipeline">
        <img src='images/robobench-method.webp' alt="RoboBench construction pipeline" width="1800" height="803" decoding="async" loading="lazy">
      </a>
      <div class="paper-image-caption"><span>Method</span>Data construction pipeline for robot scenarios</div>
    </div>
    <div class='paper-box-text'>
      <h3>RoboBench: A Comprehensive Evaluation Benchmark for Multimodal Large Language Models as Embodied Brain</h3>
      <div class="authors"><span class="author-highlight">Yulin Luo</span>⭐️, Chun-Kai Fan⭐️, Menghang Dong⭐️, Jiayu Shi⭐️, Xiangju Mi⭐️, Mengdi Zhao⭐️†, Bo-Wen Zhang⭐️, Cheng Chi⭐️†, et al., Shanghang Zhang📧</div>
      <div class="venue">European Conference on Computer Vision (ECCV), 2026</div>
      <div class="paper-timeline"><i class="fas fa-clock"></i><span>arXiv v1: 2025.10 · Accepted: 2026.07</span></div>
      <div class="paper-tldr"><span>In Short:</span> Builds a 6K-QA benchmark to diagnose embodied-brain abilities in MLLMs, and links cognitive scores to downstream VLA performance.</div>
      <div class="links">
        <a href="https://arxiv.org/abs/2510.17801" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
        <a href="https://robo-bench.github.io/" class="btn-accent"><i class="fas fa-globe"></i> Project</a>
        <a href="https://github.com/yulin-luo/RoboBench" class="btn-accent"><i class="fab fa-github"></i> Code</a>
        <a href="https://huggingface.co/datasets/LeoFan01/RoboBench" class="btn-accent"><i class="fas fa-database"></i> Dataset</a>
        <a href="https://mp.weixin.qq.com/s/SdGEqu_1mz14DhUumTZ3FQ" class="btn-accent media-link" target="_blank" rel="noopener"><i class="fas fa-newspaper"></i> 具身智能之心</a>
      </div>
    </div>
  </div>

  <div id="pub-ssd-llm" class='paper-box floating-card' data-order="20240502363" data-tags="First Author, Conference, CCF-B, Data-centric AI, Data Augmentation">
    <div class='paper-box-image paper-box-image-duo'>
      <div class="badge pulse-accent">ECCV 2024</div>
      <a class="paper-image-link" href="images/ssdllm.png" aria-label="Open full-size SSD-LLM teaser">
        <img src='images/ssdllm.webp' alt="SSD-LLM teaser" width="1800" height="1039" decoding="async" loading="lazy">
      </a>
      <div class="paper-image-caption"><span>Teaser</span>Workflow for discovering subpopulation structure</div>
      <a class="paper-image-link" href="images/ssdllm-method.png" aria-label="Open full-size SSD-LLM method diagram">
        <img src='images/ssdllm-method.webp' alt="SSD-LLM method diagram" width="1800" height="688" decoding="async" loading="lazy">
      </a>
      <div class="paper-image-caption"><span>Method</span>Caption, criteria generation, refinement, and assignment</div>
    </div>
    <div class='paper-box-text'>
      <h3>LLM as Dataset Analyst: Subpopulation Structure Discovery with Large Language Model</h3>
      <div class="paper-short-name">Short name: SSD-LLM</div>
      <div class="authors"><span class="author-highlight">Yulin Luo</span>⭐️, Ruichuan An⭐️, Bocheng Zou, Yiming Tang, Jiaming Liu, Shanghang Zhang📧</div>
      <div class="venue">European Conference on Computer Vision (ECCV), 2024</div>
      <div class="paper-timeline"><i class="fas fa-clock"></i><span>arXiv v1: 2024.05 · Accepted: 2024.07</span></div>
      <div class="paper-tldr"><span>In Short:</span> Turns LLMs into dataset analysts that discover hidden subpopulations, exposing dataset bias and guiding targeted data improvement.</div>
      <div class="links">
        <a href="https://arxiv.org/abs/2405.02363" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
        <a href="https://doi.org/10.1007/978-3-031-73414-4_14" class="btn-accent"><i class="fas fa-award"></i> ECCV</a>
        <a href="https://llm-as-dataset-analyst.github.io/" class="btn-accent"><i class="fas fa-globe"></i> Project</a>
        <a href="https://github.com/yulin-luo/SSDLLM" class="btn-accent"><i class="fab fa-github"></i> Code</a>
      </div>
    </div>
  </div>

  <div id="pub-moase" class='paper-box floating-card' data-order="20240516486" data-tags="Co-First Author, Conference, CCF-A, Oral, Computer Vision, MoE">
    <div class='paper-box-image paper-box-image-duo'>
      <div class="badge pulse-accent">AAAI 2026 · Oral</div>
      <a class="paper-image-link" href="images/moase-teaser.png" aria-label="Open full-size MoASE teaser">
        <img src='images/moase-teaser.webp' alt="MoASE teaser" width="1800" height="540" decoding="async" loading="lazy">
      </a>
      <div class="paper-image-caption"><span>Teaser</span>Sparse activations motivate expert decomposition</div>
      <a class="paper-image-link" href="images/moase-method.png" aria-label="Open full-size MoASE method diagram">
        <img src='images/moase-method.webp' alt="MoASE method diagram" width="1322" height="440" decoding="async" loading="lazy">
      </a>
      <div class="paper-image-caption"><span>Method</span>MoASE routes activation patterns into experts</div>
    </div>
    <div class='paper-box-text'>
      <h3>Decomposing the Neurons: Activation Sparsity via Mixture of Experts for Continual Test-Time Adaptation</h3>
      <div class="paper-short-name">Short name: MoASE</div>
      <div class="authors">Rongyu Zhang⭐️, Aosong Cheng⭐️, <span class="author-highlight">Yulin Luo</span>⭐️, Gaole Dai, Huanrui Yang, et al., Shanghang Zhang📧</div>
      <div class="venue">AAAI Conference on Artificial Intelligence (AAAI), 2026 &nbsp;(<b>Oral</b>)</div>
      <div class="paper-timeline"><i class="fas fa-clock"></i><span>arXiv v1: 2024.05 · Accepted: 2025.11</span></div>
      <div class="paper-tldr"><span>In Short:</span> Interprets continual test-time adaptation through sparse neuron activations, routing activation patterns into experts for stable adaptation.</div>
      <div class="links">
        <a href="https://arxiv.org/abs/2405.16486" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
        <a href="https://doi.org/10.1609/aaai.v40i42.40922" class="btn-accent"><i class="fas fa-award"></i> AAAI</a>
        <a href="https://github.com/RoyZry98/MoASE-Pytorch" class="btn-accent"><i class="fab fa-github"></i> Code</a>
      </div>
    </div>
  </div>

  <div id="pub-deepvision-vla" class='paper-box floating-card' data-order="20260315618" data-tags="First Author, Conference, CCF-A, Embodied AI, VLA">
    <div class='paper-box-image paper-box-image-duo'>
      <div class="badge pulse-accent">ACM MM 2026</div>
      <a class="paper-image-link" href="images/deepvision-vla-teaser.png" aria-label="Open full-size DeepVision-VLA teaser">
        <img src='images/deepvision-vla-teaser.webp' alt="DeepVision-VLA teaser" width="1281" height="521" decoding="async" loading="lazy">
      </a>
      <div class="paper-image-caption"><span>Teaser</span>Vision foundation representations before robot action</div>
      <a class="paper-image-link" href="images/deepvision-vla-method.png" aria-label="Open full-size DeepVision-VLA method diagram">
        <img src='images/deepvision-vla-method.webp' alt="DeepVision-VLA method diagram" width="1800" height="926" decoding="async" loading="lazy">
      </a>
      <div class="paper-image-caption"><span>Method</span>Representation enhancement pipeline for VLA policies</div>
    </div>
    <div class='paper-box-text'>
      <h3>Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models</h3>
      <div class="authors"><span class="author-highlight">Yulin Luo</span>⭐️, Hao Chen⭐️†, Zhuangzhe Wu⭐️, Bowen Sui⭐️, Jiaming Liu⭐️†, et al., Shanghang Zhang📧</div>
      <div class="venue">ACM International Conference on Multimedia (ACM MM), 2026</div>
      <div class="paper-timeline"><i class="fas fa-clock"></i><span>arXiv v1: 2026.03 · Accepted: 2026.07</span></div>
      <div class="paper-tldr"><span>In Short:</span> Enhances vision foundation representations before action decoding, improving VLA policies for precise robot control.</div>
      <div class="links">
        <a href="https://arxiv.org/abs/2603.15618" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
        <a href="https://2026.acmmm.org/" class="btn-accent"><i class="fas fa-award"></i> ACM MM</a>
        <a href="https://deepvision-vla.github.io/" class="btn-accent"><i class="fas fa-globe"></i> Project</a>
        <a href="https://mp.weixin.qq.com/s/q9brBo3pf750Lq6UXchK3g" class="btn-accent media-link" target="_blank" rel="noopener"><i class="fas fa-newspaper"></i> 量子位</a>
      </div>
    </div>
  </div>

  <div id="pub-randstainna" class='paper-box floating-card' data-order="20220612694" data-tags="Co-First Author, Conference, CCF-B, Medical Imaging, Data Augmentation">
    <div class='paper-box-image paper-box-image-duo'>
      <div class="badge pulse-accent">MICCAI 2022</div>
      <a class="paper-image-link" href="images/randstainna.png" aria-label="Open full-size RandStainNA teaser">
        <img src='images/randstainna.webp' alt="RandStainNA teaser" width="1800" height="1147" decoding="async" loading="lazy">
      </a>
      <div class="paper-image-caption"><span>Teaser</span>Stain augmentation and normalization are bridged</div>
      <a class="paper-image-link" href="images/randstainna-method.png" aria-label="Open full-size RandStainNA method diagram">
        <img src='images/randstainna-method.webp' alt="RandStainNA method diagram" width="1800" height="1066" decoding="async" loading="lazy">
      </a>
      <div class="paper-image-caption"><span>Method</span>Random virtual templates for stain-agnostic training</div>
    </div>
    <div class='paper-box-text'>
      <h3>RandStainNA: Learning Stain-Agnostic Features from Histology Slides by Bridging Stain Augmentation and Normalization</h3>
      <div class="authors">Yiqing Shen⭐️, <span class="author-highlight">Yulin Luo</span>⭐️, Dinggang Shen, Jing Ke📧</div>
      <div class="venue">Medical Image Computing and Computer Assisted Intervention (MICCAI), 2022</div>
      <div class="paper-timeline"><i class="fas fa-clock"></i><span>arXiv v1: 2022.06 · Accepted: 2022.06</span></div>
      <div class="paper-tldr"><span>In Short:</span> Unifies stain normalization and augmentation with random color-space sampling, improving robustness for histology classification and segmentation.</div>
      <div class="links">
        <a href="https://arxiv.org/abs/2206.12694" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
        <a href="https://doi.org/10.1007/978-3-031-16434-7_21" class="btn-accent"><i class="fas fa-award"></i> MICCAI</a>
        <a href="https://github.com/yiqings/RandStainNA" class="btn-accent"><i class="fab fa-github"></i> Code</a>
      </div>
    </div>
  </div>

  <div id="pub-robomind" class='paper-box floating-card' data-order="20241213877" data-tags="Other, Conference, CCF-B, Embodied AI, Benchmark">
    <div class='paper-box-image paper-box-image-duo'>
      <div class="badge pulse-accent">RSS 2025</div>
      <a class="paper-image-link" href="images/robomind.png" aria-label="Open full-size RoboMIND teaser">
        <img src='images/robomind.webp' alt="RoboMIND teaser" width="500" height="366" decoding="async" loading="lazy">
      </a>
      <div class="paper-image-caption"><span>Teaser</span>Multi-embodiment robot manipulation benchmark</div>
      <a class="paper-image-link" href="images/robomind-method.png" aria-label="Open full-size RoboMIND annotation process">
        <img src='images/robomind-method.webp' alt="RoboMIND annotation process" width="1533" height="385" decoding="async" loading="lazy">
      </a>
      <div class="paper-image-caption"><span>Method</span>Language-guided task process and annotation examples</div>
    </div>
    <div class='paper-box-text'>
      <h3>RoboMIND: Benchmark on Multi-Embodiment Intelligence Normative Data for Robot Manipulation</h3>
      <div class="authors">Kun Wu⭐️, Chengkai Hou⭐️, Jiaming Liu⭐️, Zhengping Che⭐️†, Xiaozhu Ju⭐️†, ..., <span class="author-highlight">Yulin Luo</span>, ..., Shanghang Zhang📧, Jian Tang📧</div>
      <div class="venue">Robotics: Science and Systems (RSS), 2025</div>
      <div class="paper-timeline"><i class="fas fa-clock"></i><span>arXiv v1: 2024.12 · Accepted: 2025.04</span></div>
      <div class="paper-tldr"><span>In Short:</span> Collects multi-embodiment manipulation data and benchmark protocols to study general robot skills across platforms and tasks.</div>
      <div class="links">
        <a href="https://arxiv.org/abs/2412.13877" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
        <a href="https://roboticsconference.org/program/papers/152/" class="btn-accent"><i class="fas fa-award"></i> RSS</a>
        <a href="https://x-humanoid-robomind.github.io/" class="btn-accent"><i class="fas fa-globe"></i> Project</a>
        <a href="https://github.com/x-humanoid-robomind" class="btn-accent"><i class="fab fa-github"></i> Code</a>
        <a href="https://huggingface.co/datasets/x-humanoid-robomind/RoboMIND" class="btn-accent"><i class="fas fa-database"></i> Dataset</a>
      </div>
    </div>
  </div>

  <div id="pub-draw-and-understand" class='paper-box floating-card' data-order="20240320271" data-tags="Other, Conference, CCF-A, Computer Vision, MLLM">
    <div class='paper-box-image paper-box-image-duo'>
      <div class="badge pulse-accent">ICLR 2025</div>
      <a class="paper-image-link" href="images/drawandunderstand-teaser.jpg" aria-label="Open full-size Draw-and-Understand teaser">
        <img src='images/drawandunderstand-teaser.webp' alt="Draw-and-Understand teaser" width="1800" height="560" decoding="async" loading="lazy">
      </a>
      <div class="paper-image-caption"><span>Teaser</span>Visual prompting for fine-grained user intent</div>
      <a class="paper-image-link" href="images/drawandunderstand-method.png" aria-label="Open full-size Draw-and-Understand method diagram">
        <img src='images/drawandunderstand-method.webp' alt="Draw-and-Understand training strategy and model architecture" width="1800" height="959" decoding="async" loading="lazy">
      </a>
      <div class="paper-image-caption"><span>Method</span>Two-stage training and the SPHINX-V architecture</div>
    </div>
    <div class='paper-box-text'>
      <h3>Draw-and-Understand: Leveraging Visual Prompts to Enable MLLMs to Comprehend What You Want</h3>
      <div class="authors">Weifeng Lin⭐️, Xinyu Wei⭐️, Ruichuan An, Peng Gao, Bocheng Zou, <span class="author-highlight">Yulin Luo</span>, Siyuan Huang, Shanghang Zhang, Hongsheng Li📧</div>
      <div class="venue">International Conference on Learning Representations (ICLR), 2025</div>
      <div class="paper-timeline"><i class="fas fa-clock"></i><span>arXiv v1: 2024.03 · Accepted: 2025.01</span></div>
      <div class="paper-tldr"><span>In Short:</span> Introduces visual prompting data and benchmarks so MLLMs can follow user-drawn marks, regions, and fine-grained visual intent.</div>
      <div class="links">
        <a href="https://arxiv.org/abs/2403.20271" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
        <a href="https://iclr.cc/virtual/2025/poster/29098" class="btn-accent"><i class="fas fa-award"></i> ICLR</a>
        <a href="https://github.com/AFeng-x/Draw-and-Understand" class="btn-accent"><i class="fab fa-github"></i> Code</a>
        <a href="https://huggingface.co/datasets/Afeng-x/Draw-and-Understand/tree/main/stage_2_fine-tuning/MDVP-Data" class="btn-accent"><i class="fas fa-database"></i> Data</a>
        <a href="https://huggingface.co/datasets/Afeng-x/Draw-and-Understand/tree/main/MDVP-bench" class="btn-accent"><i class="fas fa-database"></i> Bench</a>
        <a href="https://huggingface.co/Afeng-x/SPHINX-V-Model" class="btn-accent"><i class="fas fa-cube"></i> CKPT</a>
      </div>
    </div>
  </div>

  <div id="pub-seear1" class='paper-box floating-card' data-order="20250621669" data-tags="Other, Conference, CCF-A, Embodied AI, Agentic, World Model">
    <div class='paper-box-image paper-box-image-duo'>
      <div class="badge pulse-accent">NeurIPS 2025</div>
      <a class="paper-image-link" href="images/seear1-teaser.png" aria-label="Open full-size SEEA-R1 teaser">
        <img src='images/seear1-teaser.webp' alt="SEEA-R1 teaser" width="789" height="390" decoding="async" loading="lazy">
      </a>
      <div class="paper-image-caption"><span>Teaser</span>Self-evolving embodied agents through tree search</div>
      <a class="paper-image-link" href="images/seear1-method.png" aria-label="Open full-size SEEA-R1 method diagram">
        <img src='images/seear1-method.webp' alt="SEEA-R1 data and model evolution framework" width="1800" height="1010" decoding="async" loading="lazy">
      </a>
      <div class="paper-image-caption"><span>Method</span>Coupled data and model evolution with relative advantages</div>
    </div>
    <div class='paper-box-text'>
      <h3>SEEA-R1: Tree-Structured Reinforcement Fine-Tuning for Self-Evolving Embodied Agents</h3>
      <div class="authors">Wanxin Tian⭐️, Shijie Zhang⭐️, Kevin Zhang⭐️, Xiaowei Chi, Chun-Kai Fan, Junyu Lu, <span class="author-highlight">Yulin Luo</span>, et al., Shanghang Zhang📧, Jian Tang📧</div>
      <div class="venue">Advances in Neural Information Processing Systems (NeurIPS), 2025</div>
      <div class="paper-timeline"><i class="fas fa-clock"></i><span>arXiv v1: 2025.06 · Accepted: 2025.09</span></div>
      <div class="paper-tldr"><span>In Short:</span> Uses tree-structured reinforcement fine-tuning to improve embodied-agent reasoning through self-evolving exploration and feedback.</div>
      <div class="links">
        <a href="https://arxiv.org/abs/2506.21669" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
        <a href="https://proceedings.neurips.cc/paper_files/paper/2025/hash/7103cd82de95a7b30983fcf74ba499ac-Abstract-Conference.html" class="btn-accent"><i class="fas fa-award"></i> NeurIPS</a>
        <a href="https://seea-r1.github.io/" class="btn-accent"><i class="fas fa-globe"></i> Project</a>
        <a href="https://github.com/AurumTian/seea-r1" class="btn-accent"><i class="fab fa-github"></i> Code</a>
      </div>
    </div>
  </div>

  <div id="pub-mofme" class='paper-box floating-card' data-order="20231216610" data-tags="Other, Conference, CCF-A, Computer Vision, MoE">
    <div class='paper-box-image paper-box-image-duo'>
      <div class="badge pulse-accent">AAAI 2024</div>
      <a class="paper-image-link" href="images/mofme.png" aria-label="Open full-size MoFME teaser">
        <img src='images/mofme.webp' alt="MoFME teaser" width="1800" height="562" decoding="async" loading="lazy">
      </a>
      <div class="paper-image-caption"><span>Teaser</span>Deweathering pipeline for downstream perception</div>
      <a class="paper-image-link" href="images/mofme-method.png" aria-label="Open full-size MoFME method diagram">
        <img src='images/mofme-method.webp' alt="MoFME method diagram" width="1800" height="740" decoding="async" loading="lazy">
      </a>
      <div class="paper-image-caption"><span>Method</span>Feature modulation experts with uncertainty-aware routing</div>
    </div>
    <div class='paper-box-text'>
      <h3>Efficient Deweather Mixture-of-Experts with Uncertainty-Aware Feature-Wise Linear Modulation</h3>
      <div class="paper-short-name">Short name: MoFME</div>
      <div class="authors">Rongyu Zhang, <span class="author-highlight">Yulin Luo</span>, Jiaming Liu, Huanrui Yang, Zhen Dong, et al., Yuan Du📧, Shanghang Zhang📧</div>
      <div class="venue">AAAI Conference on Artificial Intelligence (AAAI), 2024</div>
      <div class="paper-timeline"><i class="fas fa-clock"></i><span>arXiv v1: 2023.12 · Accepted: 2023.12</span></div>
      <div class="paper-tldr"><span>In Short:</span> Modulates deweathering experts with uncertainty-aware feature-wise signals for efficient restoration under adverse weather.</div>
      <div class="links">
        <a href="https://arxiv.org/abs/2312.16610" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
        <a href="https://doi.org/10.1609/aaai.v38i15.29622" class="btn-accent"><i class="fas fa-award"></i> AAAI</a>
        <a href="https://github.com/RoyZry98/MoFME-Pytorch" class="btn-accent"><i class="fab fa-github"></i> Code</a>
      </div>
    </div>
  </div>

</div>

<span class='anchor' id='awards'></span>
# 🏆 Awards
- Shanghai Jiao Tong University <span class="primary-gradient-text">Outstanding Graduate</span> &nbsp;*2023.06*.
- Weichai Power <span class="primary-gradient-text">Scholarship</span> &nbsp;*2022.10*.
- Huawei <span class="primary-gradient-text">Scholarship</span> &nbsp;*2021.12*.
- Shanghai Jiao Tong University <span class="primary-gradient-text">B-Class Merit Scholarship</span> &nbsp;*2020.12, 2021.12, 2022.12*.

<span class='anchor' id='services'></span>
# 👓 Services
- *Conferences*: &nbsp;Reviewer of AAAI 2026, ICLR 2026, CVPR 2026, ECCV 2026, and NeurIPS 2026 Datasets & Benchmarks.
<!-- TODO(可选): 期刊审稿 -->

<span class='anchor' id='interests'></span>
# 😊 Interests
<!-- TODO(可选): 兴趣爱好卡片，参考模板 blog-card 风格。不需要可整节删掉。 -->

<script>
document.addEventListener('DOMContentLoaded', function() {
  const wrapper = document.getElementById('publications-wrapper');
  if (!wrapper) return;

  const paperBoxes = Array.from(wrapper.querySelectorAll('.paper-box'));

  // Default order is reverse chronological by arXiv id when available.
  paperBoxes.sort((a, b) => {
    return Number(b.dataset.order || 0) - Number(a.dataset.order || 0);
  });
  paperBoxes.forEach(box => wrapper.appendChild(box));

  const filterContainer = document.getElementById('filter-container');
  const selects = filterContainer ? filterContainer.querySelectorAll('select[data-dim]') : [];
  const resetBtn = document.getElementById('filter-reset');

  const dimensionMap = {
    author: ['First Author', 'Co-First Author', 'Other'],
    venue: ['CCF-A', 'CCF-B'],
    type: ['Conference', 'Preprint'],
    highlight: ['Oral'],
    domain: ['Embodied AI', 'Computer Vision', 'Medical Imaging', 'Data-centric AI'],
    focus: ['VLA', 'Benchmark', 'Agentic', 'World Model', 'MoE', 'Data Augmentation', 'MLLM']
  };

  const visibleTagLabels = {
    'First Author': 'First author',
    'Co-First Author': 'Co-first author',
    'Oral': 'Oral',
    'CCF-A': 'CCF-A',
    'CCF-B': 'CCF-B'
  };
  const hiddenVisibleTags = new Set(['Other', 'Conference', 'Preprint']);

  function arrangePaperFigures() {
    paperBoxes.forEach(box => {
      box.querySelectorAll('.paper-image-caption').forEach(caption => {
        const kind = caption.querySelector('span');
        const imageLink = caption.previousElementSibling;
        if (!kind || !imageLink || !imageLink.classList.contains('paper-image-link')) return;
        kind.classList.add('paper-image-kind');
        imageLink.insertAdjacentElement('beforebegin', kind);
      });
    });
  }

  function renderPaperTags() {
    paperBoxes.forEach(box => {
      if (box.querySelector('.paper-tags')) return;
      const venue = box.querySelector('.venue');
      if (!venue) return;

      const tags = (box.getAttribute('data-tags') || '')
        .split(',')
        .map(t => t.trim())
        .filter(t => t && !hiddenVisibleTags.has(t));
      if (!tags.length) return;

      const tagList = document.createElement('div');
      tagList.className = 'paper-tags';
      tagList.setAttribute('aria-label', 'Publication tags');
      tags.forEach(tag => {
        const tagItem = document.createElement('span');
        tagItem.className = 'paper-tag';
        tagItem.dataset.tag = tag;
        tagItem.textContent = visibleTagLabels[tag] || tag;
        tagList.appendChild(tagItem);
      });
      venue.insertAdjacentElement('afterend', tagList);
    });
  }

  const optionLabels = {};
  selects.forEach(sel => {
    const dim = sel.dataset.dim;
    optionLabels[dim] = {};
    Array.from(sel.options).forEach(option => {
      if (option.value) optionLabels[dim][option.value] = option.textContent;
    });
  });

  function getDimensionTags(box, dim) {
    const tags = (box.getAttribute('data-tags') || '').split(',').map(t => t.trim());
    return tags.filter(t => dimensionMap[dim].includes(t));
  }

  function matchesCriteria(box, criteria) {
    for (const dim in criteria) {
      if (!getDimensionTags(box, dim).includes(criteria[dim])) return false;
    }
    return true;
  }

  function collectCriteria() {
    const criteria = {};
    selects.forEach(sel => { if (sel.value) criteria[sel.dataset.dim] = sel.value; });
    return criteria;
  }

  function resetFilters() {
    selects.forEach(sel => sel.value = '');
    filterPapers();
  }

  function applyPaperVisibility(criteria) {
    paperBoxes.forEach(box => {
      box.classList.toggle('hidden', !matchesCriteria(box, criteria));
    });
  }

  function filterPapers() {
    let criteria = collectCriteria();
    if (updateFilterOptions(criteria)) criteria = collectCriteria();
    applyPaperVisibility(criteria);
    updateFilterOptions(criteria);
  }

  function updateFilterOptions(criteria) {
    let changed = false;

    selects.forEach(sel => {
      const dim = sel.dataset.dim;
      const available = new Set();

      paperBoxes.forEach(box => {
        const peerCriteria = Object.fromEntries(
          Object.entries(criteria).filter(([key]) => key !== dim)
        );
        if (!matchesCriteria(box, peerCriteria)) return;
        getDimensionTags(box, dim).forEach(tag => available.add(tag));
      });

      if (sel.value && !available.has(sel.value)) {
        sel.value = '';
        changed = true;
      }

      const currentValue = sel.value;
      sel.replaceChildren(new Option('All', ''));
      dimensionMap[dim].forEach(value => {
        if (available.has(value)) sel.appendChild(new Option(optionLabels[dim][value] || value, value));
      });
      sel.value = currentValue;
    });

    return changed;
  }

  selects.forEach(sel => sel.addEventListener('change', filterPapers));

  if (resetBtn) {
    resetBtn.addEventListener('click', resetFilters);
  }

  document.querySelectorAll('.news-paper-link[href^="#pub-"]').forEach(link => {
    link.addEventListener('click', resetFilters);
  });

  arrangePaperFigures();
  renderPaperTags();
  updateFilterOptions({});
});
</script>

---
permalink: /
title: "Yulin Luo - Homepage"
excerpt: "PhD student at Peking University. Research on generalizable embodied foundation models for the open world."
author_profile: true
redirect_from:
  - /about/
  - /about.html
header:
  og_image: images/lyl_photo.png     # 站外分享（Google/微信）用图
  teaser: images/lyl_photo.png        # 站内缩略图
---

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>
My name is <span class="accent-text">Yulin Luo</span> (罗峪霖). I'm a PhD student (since 2023) at the <a href="https://cs.pku.edu.cn/" class="link-accent">School of Computer Science</a>, **Peking University**<img src='images/pkulogo.png' style="height:1em; vertical-align:middle;">, advised by Assistant Professor <a href="https://www.shanghangzhang.com/" class="link-accent">Shanghang Zhang</a>. I received my Bachelor's degree in Automation from **Shanghai Jiao Tong University** in 2023.

<div class="quote-accent">
My research focuses on <span class="accent-text">generalizable embodied foundation models for the open world</span>:
  <ul>
    <li>Building <span class="primary-gradient-text">embodied foundation models</span>🤖 that generalize to open-world objects, skills, and instructions.</li>
    <li>Studying the <span class="primary-gradient-text">co-design of models and data</span>🔁 to push open-world generalization.</li>
  </ul>
</div>

Feel free to reach out if you'd like to discuss research or explore potential collaboration!

<!-- TODO(可选): highlight 卡片。留了一个已填好示例，可再加。 -->
<div class="highlight-blocks">
  <div class="highlight-block floating-card">
    <h3><i class="fas fa-robot"></i> Embodied AI Researcher</h3>
    <ul>
      <li>My <span class="primary-gradient-text">Research Interests</span>:
        generalizable embodied foundation models for the open world,
        with a focus on the co-evolution of models and data
      </li>
      <li><span class="primary-gradient-text">First / co-first author</span>
        at ECCV, AAAI, MICCAI (and more); ~785 citations, h-index 12
        <a href="https://scholar.google.com/citations?user=SgeV4NkAAAAJ" class="link-accent">(Google Scholar)</a>.
      </li>
    </ul>
  </div>

  <!-- TODO: 第二个卡片（例如兴趣爱好），需要你给内容
  <div class="highlight-block floating-card">
    <h3><i class="fas fa-pen-fancy"></i> ...</h3>
    <ul><li>...</li></ul>
  </div>
  -->
</div>

<span class='anchor' id='-news'></span>
# 🔥 News
<!-- TODO: 你的新闻时间线。格式：一行一条，最新在上。 -->
- *2026.07*: &nbsp;🎉 RoboBench is accepted to ECCV 2026.
- *2025.11*: &nbsp;🎉 MoASE is accepted as Oral at AAAI 2026.
- *2025.09*: &nbsp;🎉 SEEA-R1 is accepted to NeurIPS 2025.
- *2025.04*: &nbsp;🎉 RoboMIND is accepted to RSS 2025.
- *2025.01*: &nbsp;🎉 Draw-and-Understand is accepted to ICLR 2025.
- *2024.07*: &nbsp;🎉 SSD-LLM (LLM as Dataset Analyst) is accepted to ECCV 2024.
- *2023.12*: &nbsp;🎉 MoFME is accepted to AAAI 2024.
- *2023.09*: &nbsp;🎓 Started PhD at Peking University, advised by Prof. Shanghang Zhang.
- *2022.06*: &nbsp;🎉 RandStainNA is accepted to MICCAI 2022.

<span class='anchor' id='-educations'></span>
# 🏫 Educations
- *2023.09 - Present*: &nbsp;PhD in Computer Science, Peking University<img src='images/pkulogo.png' style="height:1em; vertical-align:middle;">.
- *2019.09 - 2023.06*: &nbsp;B.Eng. in Automation, Shanghai Jiao Tong University.

<span class='anchor' id='-publications'></span>
# 📃 Publications

<!-- ⭐️ = (共同)第一作者；📧 = 通讯作者。teaser 图默认用占位图 images/500x300.png，
     你把每篇的图放到 images/ 后替换 src 即可。缺 arXiv 链接的用 "#" 占位，后续补。 -->
<div id="publications-wrapper">
  <div id="filter-container"></div>

  <div class='paper-box floating-card' data-tags="First/Co-First Author, Conference, CCF-A, Embodied AI, Benchmark">
    <div class='paper-box-image'>
      <div class="badge pulse-accent">ECCV 2026</div>
      <img src='images/500x300.png' alt="RoboBench teaser" width="100%">
    </div>
    <div class='paper-box-text'>
      <h3>RoboBench: A Comprehensive Evaluation Benchmark for MLLMs as Embodied Brain</h3>
      <div class="paper-short-name">Short name: RoboBench</div>
      <div class="authors"><span class="primary-gradient-text">Yulin Luo</span>⭐️, Chun-Kai Fan⭐️, Menghang Dong⭐️, Jiayi Shi⭐️, Mingkang Zhao⭐️, Bo-Wen Zhang⭐️, et al., Shanghang Zhang📧</div>
      <div class="venue">European Conference on Computer Vision (ECCV), 2026</div>
      <div class="links">
        <a href="https://arxiv.org/abs/2510.17801" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
        <a href="https://robo-bench.github.io/" class="btn-accent"><i class="fas fa-globe"></i> Project</a>
      </div>
    </div>
  </div>

  <div class='paper-box floating-card' data-tags="First/Co-First Author, Conference, CCF-A, Data-centric AI, Data Augmentation">
    <div class='paper-box-image'>
      <div class="badge pulse-accent">ECCV 2024</div>
      <img src='images/500x300.png' alt="SSD-LLM teaser" width="100%">
    </div>
    <div class='paper-box-text'>
      <h3>LLM as Dataset Analyst: Subpopulation Structure Discovery with Large Language Model</h3>
      <div class="paper-short-name">Short name: SSD-LLM</div>
      <div class="authors"><span class="primary-gradient-text">Yulin Luo</span>⭐️, Ruichuan An⭐️, Bocheng Zou, Yiming Tang, Jiaming Liu, Shanghang Zhang📧</div>
      <div class="venue">European Conference on Computer Vision (ECCV), 2024</div>
      <div class="links">
        <a href="https://arxiv.org/abs/2405.02363" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
        <a href="https://llm-as-dataset-analyst.github.io/" class="btn-accent"><i class="fas fa-globe"></i> Project</a>
      </div>
    </div>
  </div>

  <div class='paper-box floating-card' data-tags="First/Co-First Author, Conference, CCF-A, Oral, Model, MoE">
    <div class='paper-box-image'>
      <div class="badge pulse-accent">AAAI 2026 · Oral</div>
      <img src='images/500x300.png' alt="MoASE teaser" width="100%">
    </div>
    <div class='paper-box-text'>
      <h3>Decomposing the Neurons: Activation Sparsity via Mixture of Experts for Continual Test-Time Adaptation</h3>
      <div class="paper-short-name">Short name: MoASE</div>
      <div class="authors">Rongyu Zhang⭐️, Aosong Cheng⭐️, <span class="primary-gradient-text">Yulin Luo</span>⭐️, Gaole Dai, Huanrui Yang, et al., Shanghang Zhang📧</div>
      <div class="venue">AAAI Conference on Artificial Intelligence (AAAI), 2026 &nbsp;(<b>Oral</b>)</div>
      <div class="links">
        <a href="https://arxiv.org/abs/2405.16486" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
        <a href="https://github.com/RoyZry98/MoASE-Pytorch" class="btn-accent"><i class="fab fa-github"></i> Code</a>
      </div>
    </div>
  </div>

  <div class='paper-box floating-card' data-tags="First/Co-First Author, Conference, CCF-B, Medical Imaging, Data Augmentation">
    <div class='paper-box-image'>
      <div class="badge pulse-accent">MICCAI 2022</div>
      <img src='images/500x300.png' alt="RandStainNA teaser" width="100%">
    </div>
    <div class='paper-box-text'>
      <h3>RandStainNA: Learning Stain-Agnostic Features from Histology Slides by Bridging Stain Augmentation and Normalization</h3>
      <div class="paper-short-name">Short name: RandStainNA</div>
      <div class="authors">Yiqing Shen⭐️, <span class="primary-gradient-text">Yulin Luo</span>⭐️, Dinggang Shen, Jing Ke📧</div>
      <div class="venue">Medical Image Computing and Computer Assisted Intervention (MICCAI), 2022</div>
      <div class="links">
        <a href="https://arxiv.org/abs/2206.12694" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
        <a href="https://github.com/yiqings/RandStainNA" class="btn-accent"><i class="fab fa-github"></i> Code</a>
      </div>
    </div>
  </div>

  <div class='paper-box floating-card' data-tags="First/Co-First Author, Preprint, Embodied AI, VLA">
    <div class='paper-box-image'>
      <div class="badge pulse-accent">Preprint 2026</div>
      <img src='images/500x300.png' alt="Look Before Acting teaser" width="100%">
    </div>
    <div class='paper-box-text'>
      <h3>Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models</h3>
      <div class="paper-short-name">Short name: Look Before Acting</div>
      <div class="authors"><span class="primary-gradient-text">Yulin Luo</span>⭐️, Hao Chen⭐️, Zhixuan Wu⭐️, Bo Sui⭐️, Jiaming Liu⭐️, et al., Shanghang Zhang📧</div>
      <div class="venue">arXiv preprint, 2026</div>
      <div class="links">
        <a href="https://arxiv.org/abs/2603.15618" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
      </div>
    </div>
  </div>

  <div class='paper-box floating-card' data-tags="First/Co-First Author, Preprint, Medical Imaging, MLLM">
    <div class='paper-box-image'>
      <div class="badge pulse-accent">Preprint 2024</div>
      <img src='images/500x300.png' alt="Radiology Foundation Model teaser" width="100%">
    </div>
    <div class='paper-box-text'>
      <h3>Expert-Level Vision-Language Foundation Model for Real-World Radiology and Comprehensive Evaluation</h3>
      <div class="paper-short-name">Short name: Radiology VLM</div>
      <div class="authors">Xiaohong Liu⭐️, Guoxing Yang⭐️, <span class="primary-gradient-text">Yulin Luo</span>⭐️, et al.</div>
      <div class="venue">arXiv preprint, 2024</div>
      <div class="links">
        <a href="https://arxiv.org/abs/2409.16183" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
      </div>
    </div>
  </div>

  <div class='paper-box floating-card' data-tags="First/Co-First Author, Preprint, Model, MoE">
    <div class='paper-box-image'>
      <div class="badge pulse-accent">Preprint 2023</div>
      <img src='images/500x300.png' alt="WM-MoE teaser" width="100%">
    </div>
    <div class='paper-box-text'>
      <h3>WM-MoE: Weather-Aware Multi-Scale Mixture-of-Experts for Blind Adverse Weather Removal</h3>
      <div class="paper-short-name">Short name: WM-MoE</div>
      <div class="authors"><span class="primary-gradient-text">Yulin Luo</span>, Rui Zhao, Xiaobao Wei, Jinwei Chen, et al., Shanghang Zhang📧</div>
      <div class="venue">arXiv preprint, 2023</div>
      <div class="links">
        <a href="https://arxiv.org/abs/2303.13739" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
      </div>
    </div>
  </div>

  <div class='paper-box floating-card' data-tags="Conference, CCF-B, Embodied AI, Benchmark">
    <div class='paper-box-image'>
      <div class="badge pulse-accent">RSS 2025</div>
      <img src='images/500x300.png' alt="RoboMIND teaser" width="100%">
    </div>
    <div class='paper-box-text'>
      <h3>RoboMIND: Benchmark on Multi-Embodiment Intelligence Normative Data for Robot Manipulation</h3>
      <div class="paper-short-name">Short name: RoboMIND</div>
      <div class="authors">Kun Wu, Chengkai Hou, Jiaming Liu, et al., <span class="primary-gradient-text">Yulin Luo</span>, et al.</div>
      <div class="venue">Robotics: Science and Systems (RSS), 2025</div>
      <div class="links">
        <a href="https://arxiv.org/abs/2412.13877" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
      </div>
    </div>
  </div>

  <div class='paper-box floating-card' data-tags="Conference, CCF-A, Computer Vision, MLLM">
    <div class='paper-box-image'>
      <div class="badge pulse-accent">ICLR 2025</div>
      <img src='images/500x300.png' alt="Draw-and-Understand teaser" width="100%">
    </div>
    <div class='paper-box-text'>
      <h3>Draw-and-Understand: Leveraging Visual Prompts to Enable MLLMs to Comprehend What You Want</h3>
      <div class="paper-short-name">Short name: Draw-and-Understand</div>
      <div class="authors">Weifeng Lin, Xinyu Wei, Ruichuan An, Peng Gao, Bocheng Zou, <span class="primary-gradient-text">Yulin Luo</span>, et al.</div>
      <div class="venue">International Conference on Learning Representations (ICLR), 2025</div>
      <div class="links">
        <a href="https://arxiv.org/abs/2403.20271" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
      </div>
    </div>
  </div>

  <div class='paper-box floating-card' data-tags="Conference, CCF-A, Embodied AI, Agentic, World Model">
    <div class='paper-box-image'>
      <div class="badge pulse-accent">NeurIPS 2025</div>
      <img src='images/500x300.png' alt="SEEA-R1 teaser" width="100%">
    </div>
    <div class='paper-box-text'>
      <h3>SEEA-R1: Tree-Structured Reinforcement Fine-Tuning for Self-Evolving Embodied Agents</h3>
      <div class="paper-short-name">Short name: SEEA-R1</div>
      <div class="authors">Wanxin Tian, Shijie Zhang, Kun Zhang, Xiaowei Chi, <span class="primary-gradient-text">Yulin Luo</span>, et al.</div>
      <div class="venue">Advances in Neural Information Processing Systems (NeurIPS), 2025</div>
      <div class="links">
        <a href="https://arxiv.org/abs/2506.21669" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
      </div>
    </div>
  </div>

  <div class='paper-box floating-card' data-tags="Conference, CCF-A, Model, MoE">
    <div class='paper-box-image'>
      <div class="badge pulse-accent">AAAI 2024</div>
      <img src='images/500x300.png' alt="MoFME teaser" width="100%">
    </div>
    <div class='paper-box-text'>
      <h3>Efficient Deweather Mixture-of-Experts with Uncertainty-Aware Feature-Wise Linear Modulation</h3>
      <div class="paper-short-name">Short name: MoFME</div>
      <div class="authors">Rongyu Zhang, <span class="primary-gradient-text">Yulin Luo</span>, Jiaming Liu, Huanrui Yang, et al., Shanghang Zhang📧</div>
      <div class="venue">AAAI Conference on Artificial Intelligence (AAAI), 2024</div>
      <div class="links">
        <a href="https://arxiv.org/abs/2312.16610" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
      </div>
    </div>
  </div>

</div>

<span class='anchor' id='-awards'></span>
# 🏆 Awards
- *2023.06*: &nbsp;Shanghai Jiao Tong University <span class="primary-gradient-text">Outstanding Graduate</span>.
- *2021.12*: &nbsp;Huawei <span class="primary-gradient-text">Scholarship</span>.

<span class='anchor' id='-services'></span>
# 👓 Services
- *Conferences*: &nbsp;Reviewer of CVPR, NeurIPS, ICLR, AAAI, ECCV.
<!-- TODO(可选): 期刊审稿 -->

<span class='anchor' id='-interests'></span>
# 😊 Interests
<!-- TODO(可选): 兴趣爱好卡片，参考模板 blog-card 风格。不需要可整节删掉。 -->

<script>
document.addEventListener('DOMContentLoaded', function() {
  const wrapper = document.getElementById('publications-wrapper');
  if (!wrapper) return;

  const filterContainer = document.getElementById('filter-container');
  const paperBoxes = wrapper.querySelectorAll('.paper-box');

  let tagCounts = {};
  let activeTags = new Set();

  paperBoxes.forEach(box => {
    const tagsAttribute = box.getAttribute('data-tags');
    if (tagsAttribute) {
      const tagsList = tagsAttribute.split(',').map(t => t.trim()).filter(t => t);
      const textContainer = box.querySelector('.paper-box-text');
      const linksContainer = box.querySelector('.links');
      if (textContainer && !textContainer.querySelector('.badge-container')) {
        const badgeContainer = document.createElement('div');
        badgeContainer.className = 'badge-container';
        tagsList.forEach(tag => {
          const badge = document.createElement('span');
          badge.className = 'inner-tag-badge';
          badge.textContent = tag;
          badgeContainer.appendChild(badge);
        });
        if (linksContainer) {
          textContainer.insertBefore(badgeContainer, linksContainer);
        } else {
          textContainer.appendChild(badgeContainer);
        }
      }
      tagsList.forEach(tag => { tagCounts[tag] = (tagCounts[tag] || 0) + 1; });
    }
  });

  const sortedTags = Object.keys(tagCounts).sort();
  if (filterContainer) {
    filterContainer.innerHTML = '';
    sortedTags.forEach(tag => {
      const btn = document.createElement('button');
      btn.className = 'filter-btn';
      btn.textContent = `${tag} (${tagCounts[tag]})`;
      btn.onclick = () => {
        if (activeTags.has(tag)) { activeTags.delete(tag); btn.classList.remove('active'); }
        else { activeTags.add(tag); btn.classList.add('active'); }
        filterPapers();
      };
      filterContainer.appendChild(btn);
    });
  }

  function filterPapers() {
    paperBoxes.forEach(box => {
      const boxTagsString = box.getAttribute('data-tags');
      const boxTags = boxTagsString ? boxTagsString.split(',').map(t => t.trim()) : [];
      let isVisible = true;
      if (activeTags.size > 0) {
        isVisible = boxTags.length === 0 ? false
          : Array.from(activeTags).every(activeTag => boxTags.includes(activeTag));
      }
      box.classList.toggle('hidden', !isVisible);
      box.querySelectorAll('.inner-tag-badge').forEach(badge => {
        badge.classList.toggle('active', activeTags.has(badge.textContent));
      });
    });
  }
});
</script>

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

<span class='anchor' id='about-me'></span>
My name is <span class="author-highlight">Yulin Luo</span> (罗峪霖). I'm a PhD student (since 2023) at the <a href="https://cs.pku.edu.cn/" class="link-accent">School of Computer Science</a>, **Peking University**<img src='images/pkulogo.png' style="height:1em; vertical-align:middle;">, advised by Assistant Professor <a href="https://scholar.google.cz/citations?user=voqw10cAAAAJ&hl=zh-CN" class="link-accent">Shanghang Zhang</a>. I received my Bachelor's degree in Automation from **Shanghai Jiao Tong University**<img src='images/sjtulogo.png' style="height:1em; vertical-align:middle;"> in 2023.

<div class="quote-accent">
My research focuses on <span class="accent-text">generalizable embodied foundation models for the open world</span>:
  <ul>
    <li>Building <span class="primary-gradient-text">embodied foundation models</span>🤖 that generalize across objects, skills, embodiments, scenes, and tasks in unstructured, open-world environments.</li>
    <li>Studying the <span class="primary-gradient-text">co-evolution of models and data</span>🔁 to scale embodied intelligence from narrow benchmarks to real-world generalization.</li>
  </ul>
</div>

<div class="highlight-blocks">
  <div class="highlight-block floating-card">
    <h3><i class="fas fa-robot"></i> Embodied AI Researcher</h3>
    <ul>
      <li>My <span class="primary-gradient-text">Research Interests</span>:
        generalizable embodied foundation models for the open world,
        with a focus on the co-evolution of models and data.
      </li>
      <li><span class="primary-gradient-text">Generalization focus</span>:
        L1 in-domain → L2 distribution shift → L3 compositional → L4 causal-mechanistic → L5 open-world continual.
      </li>
      <li><span class="primary-gradient-text">First / co-first author</span>
        of 5 accepted papers at CCF-A/B venues.
      </li>
      <li><span class="primary-gradient-text"><span id="total_cit">~785</span> citations</span>,
        h-index <span id="h_index">12</span>
        <a href="https://scholar.google.com/citations?user=SgeV4NkAAAAJ" class="link-accent">(Google Scholar)</a>.
      </li>
    </ul>
  </div>
</div>

<span class='anchor' id='-news'></span>
# 🔥 News
<!-- TODO: 你的新闻时间线。格式：一行一条，最新在上。 -->
- *2026.07*: &nbsp;🎉 <b>RoboBench</b> is accepted to ECCV 2026. (first author)
- *2025.11*: &nbsp;🎉 <b>MoASE</b> is accepted as Oral at AAAI 2026. (co-first author)
- *2025.09*: &nbsp;🎉 SEEA-R1 is accepted to NeurIPS 2025.
- *2025.04*: &nbsp;🎉 RoboMIND is accepted to RSS 2025.
- *2025.01*: &nbsp;🎉 Draw-and-Understand is accepted to ICLR 2025.
- *2024.07*: &nbsp;🎉 <b>SSD-LLM</b> is accepted to ECCV 2024. (first author)
- *2023.12*: &nbsp;🎉 <b>MoFME</b> is accepted to AAAI 2024.
- *2023.09*: &nbsp;🎓 Started PhD at Peking University, advised by Prof. Shanghang Zhang.
- *2023.06*: &nbsp;🎓 Graduated with B.Eng. in Automation from Shanghai Jiao Tong University.
- *2022.06*: &nbsp;🎉 <b>RandStainNA</b> is accepted to MICCAI 2022. (co-first author)

<span class='anchor' id='-educations'></span>
# 🏫 Educations
- *2023.09 - Present*: &nbsp;PhD in Computer Science, Peking University<img src='images/pkulogo.png' style="height:1em; vertical-align:middle;">.
- *2019.09 - 2023.06*: &nbsp;B.Eng. in Automation, Shanghai Jiao Tong University<img src='images/sjtulogo.png' style="height:1em; vertical-align:middle;">.

<span class='anchor' id='-publications'></span>
# 📃 Publications

<!-- ⭐️ = (共同)第一作者；📧 = 通讯作者。teaser 图默认用占位图 images/500x300.png，
     你把每篇的图放到 images/ 后替换 src 即可。缺 arXiv 链接的用 "#" 占位，后续补。 -->
<div id="publications-wrapper">
  <div id="filter-container" class="filter-bar">
    <div class="filter-group">
      <label for="filter-author">Author Role</label>
      <select id="filter-author" data-dim="author">
        <option value="">All</option>
        <option value="First/Co-First Author">First / Co-First Author</option>
        <option value="Other">Other</option>
      </select>
    </div>
    <div class="filter-group">
      <label for="filter-venue">Venue Tier</label>
      <select id="filter-venue" data-dim="venue">
        <option value="">All</option>
        <option value="CCF-A">CCF-A</option>
        <option value="CCF-B">CCF-B</option>
        <option value="Preprint">Preprint</option>
      </select>
    </div>
    <div class="filter-group">
      <label for="filter-type">Type</label>
      <select id="filter-type" data-dim="type">
        <option value="">All</option>
        <option value="Conference">Conference</option>
        <option value="Oral">Oral</option>
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
        <option value="Model">Model</option>
      </select>
    </div>
    <button id="filter-reset" class="filter-reset-btn">Reset</button>
  </div>

  <div class='paper-box floating-card' data-order="20251017801" data-tags="First/Co-First Author, Conference, CCF-B, Embodied AI, Benchmark">
    <div class='paper-box-image'>
      <div class="badge pulse-accent">ECCV 2026</div>
      <img src='images/robobench.png' alt="RoboBench teaser" width="100%">
    </div>
    <div class='paper-box-text'>
      <h3>RoboBench: A Comprehensive Evaluation Benchmark for MLLMs as Embodied Brain</h3>
      <div class="paper-short-name">Short name: RoboBench</div>
      <div class="authors"><span class="author-highlight">Yulin Luo</span>⭐️, Chun-Kai Fan⭐️, Menghang Dong⭐️, Jiayi Shi⭐️, Mingkang Zhao⭐️, Bo-Wen Zhang⭐️, et al., Shanghang Zhang📧</div>
      <div class="venue">European Conference on Computer Vision (ECCV), 2026</div>
      <div class="links">
        <a href="https://arxiv.org/abs/2510.17801" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
        <a href="https://robo-bench.github.io/" class="btn-accent"><i class="fas fa-globe"></i> Project</a>
        <a href="https://github.com/yulin-luo/RoboBench" class="btn-accent"><i class="fab fa-github"></i> Code</a>
        <a href="https://huggingface.co/datasets/LeoFan01/RoboBench" class="btn-accent"><i class="fas fa-database"></i> Dataset</a>
      </div>
    </div>
  </div>

  <div class='paper-box floating-card' data-order="20240502363" data-tags="First/Co-First Author, Conference, CCF-B, Data-centric AI, Data Augmentation">
    <div class='paper-box-image'>
      <div class="badge pulse-accent">ECCV 2024</div>
      <img src='images/ssdllm.png' alt="SSD-LLM teaser" width="100%">
    </div>
    <div class='paper-box-text'>
      <h3>LLM as Dataset Analyst: Subpopulation Structure Discovery with Large Language Model</h3>
      <div class="paper-short-name">Short name: SSD-LLM</div>
      <div class="authors"><span class="author-highlight">Yulin Luo</span>⭐️, Ruichuan An⭐️, Bocheng Zou, Yiming Tang, Jiaming Liu, Shanghang Zhang📧</div>
      <div class="venue">European Conference on Computer Vision (ECCV), 2024</div>
      <div class="links">
        <a href="https://arxiv.org/abs/2405.02363" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
        <a href="https://llm-as-dataset-analyst.github.io/" class="btn-accent"><i class="fas fa-globe"></i> Project</a>
        <a href="https://github.com/llm-as-dataset-analyst/SSDLLM" class="btn-accent"><i class="fab fa-github"></i> Code</a>
      </div>
    </div>
  </div>

  <div class='paper-box floating-card' data-order="20240516486" data-tags="First/Co-First Author, Conference, CCF-A, Oral, Computer Vision, Model, MoE">
    <div class='paper-box-image'>
      <div class="badge pulse-accent">AAAI 2026 · Oral</div>
      <img src='images/moase.png' alt="MoASE teaser" width="100%">
    </div>
    <div class='paper-box-text'>
      <h3>Decomposing the Neurons: Activation Sparsity via Mixture of Experts for Continual Test-Time Adaptation</h3>
      <div class="paper-short-name">Short name: MoASE</div>
      <div class="authors">Rongyu Zhang⭐️, Aosong Cheng⭐️, <span class="author-highlight">Yulin Luo</span>⭐️, Gaole Dai, Huanrui Yang, et al., Shanghang Zhang📧</div>
      <div class="venue">AAAI Conference on Artificial Intelligence (AAAI), 2026 &nbsp;(<b>Oral</b>)</div>
      <div class="links">
        <a href="https://arxiv.org/abs/2405.16486" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
        <a href="https://github.com/RoyZry98/MoASE-Pytorch" class="btn-accent"><i class="fab fa-github"></i> Code</a>
      </div>
    </div>
  </div>

  <div class='paper-box floating-card' data-order="20220612694" data-tags="First/Co-First Author, Conference, CCF-B, Medical Imaging, Data Augmentation">
    <div class='paper-box-image'>
      <div class="badge pulse-accent">MICCAI 2022</div>
      <img src='images/randstainna.png' alt="RandStainNA teaser" width="100%">
    </div>
    <div class='paper-box-text'>
      <h3>RandStainNA: Learning Stain-Agnostic Features from Histology Slides by Bridging Stain Augmentation and Normalization</h3>
      <div class="paper-short-name">Short name: RandStainNA</div>
      <div class="authors">Yiqing Shen⭐️, <span class="author-highlight">Yulin Luo</span>⭐️, Dinggang Shen, Jing Ke📧</div>
      <div class="venue">Medical Image Computing and Computer Assisted Intervention (MICCAI), 2022</div>
      <div class="links">
        <a href="https://arxiv.org/abs/2206.12694" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
        <a href="https://github.com/yiqings/RandStainNA" class="btn-accent"><i class="fab fa-github"></i> Code</a>
      </div>
    </div>
  </div>

  <div class='paper-box floating-card' data-order="20230313739" data-tags="First/Co-First Author, Preprint, Computer Vision, Model, MoE">
    <div class='paper-box-image'>
      <div class="badge pulse-accent">Preprint 2023</div>
      <img src='images/wmmoe.png' alt="WM-MoE teaser" width="100%">
    </div>
    <div class='paper-box-text'>
      <h3>WM-MoE: Weather-Aware Multi-Scale Mixture-of-Experts for Blind Adverse Weather Removal</h3>
      <div class="paper-short-name">Short name: WM-MoE</div>
      <div class="authors"><span class="author-highlight">Yulin Luo</span>, Rui Zhao, Xiaobao Wei, Jinwei Chen, et al., Shanghang Zhang📧</div>
      <div class="venue">arXiv preprint, 2023</div>
      <div class="links">
        <a href="https://arxiv.org/abs/2303.13739" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
      </div>
    </div>
  </div>

  <div class='paper-box floating-card' data-order="20241213877" data-tags="Other, Conference, CCF-B, Embodied AI, Benchmark">
    <div class='paper-box-image'>
      <div class="badge pulse-accent">RSS 2025</div>
      <img src='images/robomind.png' alt="RoboMIND teaser" width="100%">
    </div>
    <div class='paper-box-text'>
      <h3>RoboMIND: Benchmark on Multi-Embodiment Intelligence Normative Data for Robot Manipulation</h3>
      <div class="paper-short-name">Short name: RoboMIND</div>
      <div class="authors">Kun Wu, Chengkai Hou, Jiaming Liu, et al., <span class="author-highlight">Yulin Luo</span>, et al.</div>
      <div class="venue">Robotics: Science and Systems (RSS), 2025</div>
      <div class="links">
        <a href="https://arxiv.org/abs/2412.13877" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
        <a href="https://x-humanoid-robomind.github.io/" class="btn-accent"><i class="fas fa-globe"></i> Project</a>
        <a href="https://github.com/x-humanoid-robomind/x-humanoid-robomind.github.io" class="btn-accent"><i class="fab fa-github"></i> Github</a>
        <a href="https://huggingface.co/datasets/x-humanoid-robomind/RoboMIND" class="btn-accent"><i class="fas fa-database"></i> Dataset</a>
        <a href="https://modelscope.cn/collections/X-Humanoid/RoboMIND20" class="btn-accent"><i class="fas fa-database"></i> ModelScope</a>
      </div>
    </div>
  </div>

  <div class='paper-box floating-card' data-order="20240320271" data-tags="Other, Conference, CCF-A, Computer Vision, MLLM">
    <div class='paper-box-image'>
      <div class="badge pulse-accent">ICLR 2025</div>
      <img src='images/drawandunderstand.png' alt="Draw-and-Understand teaser" width="100%">
    </div>
    <div class='paper-box-text'>
      <h3>Draw-and-Understand: Leveraging Visual Prompts to Enable MLLMs to Comprehend What You Want</h3>
      <div class="paper-short-name">Short name: Draw-and-Understand</div>
      <div class="authors">Weifeng Lin, Xinyu Wei, Ruichuan An, Peng Gao, Bocheng Zou, <span class="author-highlight">Yulin Luo</span>, et al.</div>
      <div class="venue">International Conference on Learning Representations (ICLR), 2025</div>
      <div class="links">
        <a href="https://arxiv.org/abs/2403.20271" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
      </div>
    </div>
  </div>

  <div class='paper-box floating-card' data-order="20250621669" data-tags="Other, Conference, CCF-A, Embodied AI, Agentic, World Model">
    <div class='paper-box-image'>
      <div class="badge pulse-accent">NeurIPS 2025</div>
      <img src='images/seear1.png' alt="SEEA-R1 teaser" width="100%">
    </div>
    <div class='paper-box-text'>
      <h3>SEEA-R1: Tree-Structured Reinforcement Fine-Tuning for Self-Evolving Embodied Agents</h3>
      <div class="paper-short-name">Short name: SEEA-R1</div>
      <div class="authors">Wanxin Tian, Shijie Zhang, Kun Zhang, Xiaowei Chi, <span class="author-highlight">Yulin Luo</span>, et al.</div>
      <div class="venue">Advances in Neural Information Processing Systems (NeurIPS), 2025</div>
      <div class="links">
        <a href="https://arxiv.org/abs/2506.21669" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
      </div>
    </div>
  </div>

  <div class='paper-box floating-card' data-order="20231216610" data-tags="Other, Conference, CCF-A, Computer Vision, Model, MoE">
    <div class='paper-box-image'>
      <div class="badge pulse-accent">AAAI 2024</div>
      <img src='images/mofme.png' alt="MoFME teaser" width="100%">
    </div>
    <div class='paper-box-text'>
      <h3>Efficient Deweather Mixture-of-Experts with Uncertainty-Aware Feature-Wise Linear Modulation</h3>
      <div class="paper-short-name">Short name: MoFME</div>
      <div class="authors">Rongyu Zhang, <span class="author-highlight">Yulin Luo</span>, Jiaming Liu, Huanrui Yang, et al., Shanghang Zhang📧</div>
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
    author: ['First/Co-First Author', 'Other'],
    venue: ['CCF-A', 'CCF-B', 'Preprint'],
    type: ['Conference', 'Oral'],
    domain: ['Embodied AI', 'Computer Vision', 'Medical Imaging', 'Data-centric AI'],
    focus: ['VLA', 'Benchmark', 'Agentic', 'World Model', 'MoE', 'Data Augmentation', 'MLLM', 'Model']
  };

  const visibleTagLabels = {
    'First/Co-First Author': 'First / Co-first'
  };
  const hiddenVisibleTags = new Set(['Other', 'Conference']);

  function renderPaperTags() {
    paperBoxes.forEach(box => {
      if (box.querySelector('.paper-tags')) return;
      const shortName = box.querySelector('.paper-short-name');
      if (!shortName) return;

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
      shortName.insertAdjacentElement('afterend', tagList);
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
    resetBtn.addEventListener('click', () => {
      selects.forEach(sel => sel.value = '');
      filterPapers();
    });
  }

  renderPaperTags();
  updateFilterOptions({});
});
</script>

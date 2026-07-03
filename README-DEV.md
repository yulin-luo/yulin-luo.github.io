# Yulin Luo's Personal Homepage — Developer Notes

> 维护者：Yulin Luo
> 用途：记录本站搭建、部署、内容更新的流程与踩坑经验，避免重复踩坑。

---

## 1. 项目结构

- `_pages/about.md`：首页主体内容（About / News / Educations / Publications / Awards / Services / Interests）。
- `_config.yml`：站点元信息、作者、插件、SEO。
- `assets/css/accent-enhancements.css`：自定义样式（强调色、卡片、paper-short-name 等）。
- `images/`：头像、校徽、论文 teaser 图、favicon。
- `google_scholar_crawler/`：自动抓取 Google Scholar 引用数据。
- `_site/`：Jekyll 构建产物（已加入 `.gitignore`，不提交）。
- `Gemfile` / `Gemfile.lock`：Ruby 依赖。

---

## 2. 本地开发环境

### 2.1 安装 Ruby 和依赖

```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install -y ruby ruby-dev build-essential zlib1g-dev

# 安装 bundler
gem install bundler --no-document

# 安装项目依赖
cd /mnt/luoyulin_code/luoyulin/experience_v4/personal_web
bundle install
```

### 2.2 重要版本踩坑

- **不要使用 `github-pages` gem**。它锁定 Jekyll 3.9，与 Ruby 3.2 不兼容（会报 `undefined method 'tainted?'` 错误）。
- 本站使用 **Jekyll 4.x**（见 `Gemfile`）。
- **去掉 `hawkins`** 插件。它只支持 Jekyll 3.x，会导致 bundle 依赖冲突。
- 需要显式安装 `_config.yml` 里用到的插件：
  - `jekyll-paginate`
  - `jekyll-gist`
  - `jekyll-feed`
  - `jekyll-sitemap`
  - `jekyll-seo-tag`
  - `jekyll-redirect-from`

### 2.3 本地预览

```bash
bundle exec jekyll serve
# 打开 http://127.0.0.1:4000
```

### 2.4 资源命名规范

- 文件名只使用 **ASCII 字符**（字母、数字、`-`、`_`、`.`）。
- **不要**在文件名里用 `×`（乘号）等特殊符号，否则 Jekyll 构建会报编码错误。
- 参考：原来的 `favicon-32×32.png` 被重命名为 `favicon-32x32.png`。

---

## 3. 部署流程

本站采用 **本地构建 + 推送到 `gh-pages` 分支** 的方式部署，绕开 GitHub Actions 的 `deploy-pages` / `upload-pages-artifact` 相关问题和 Node 20 deprecation 警告。

### 3.1 GitHub Pages 设置

1. 打开仓库 Settings → Pages。
2. Build and deployment → Source 选择 **Deploy from a branch**。
3. Branch 选择 **`gh-pages`** / `/(root)`，点击 Save。

### 3.2 本地构建并部署

```bash
cd /mnt/luoyulin_code/luoyulin/experience_v4/personal_web

# 1. 构建生产站点
JEKYLL_ENV=production bundle exec jekyll build

# 2. 进入构建产物目录
cd _site

# 3. 初始化/推送到 gh-pages 分支（首次）
git init
git checkout -b gh-pages
git add .
git commit -m "Deploy site"
git push git@github.com:yulin-luo/yulin-luo.github.io.git gh-pages --force

# 4. 清理本地 _site（避免污染源码仓库）
cd ..
rm -rf _site
```

### 3.3 自动化部署（可选）

仓库里保留了 `.github/workflows/deploy.yml`，使用 `peaceiris/actions-gh-pages@v4` 自动构建并推送到 `gh-pages` 分支。

如果开启，每次 push 到 `main` 都会自动部署。但因为 GitHub Actions 环境版本和缓存不稳定，**目前以本地构建为准**。

---

## 4. 内容更新规范

### 4.1 修改首页内容

编辑 `_pages/about.md`。

### 4.2 添加/修改论文

每篇论文使用如下结构：

```html
<div class='paper-box floating-card' data-tags="First/Co-First Author, Conference, CCF-A, Embodied AI, Benchmark">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">ECCV 2026</div>
    <img src='images/robobench.png' alt="RoboBench teaser" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>Paper Title</h3>
    <div class="paper-short-name">Short name: RoboBench</div>
    <p>Authors ...</p>
    <p><em>Conference/Journal Name</em> ...</p>
    <p>Links / Code / Project</p>
    <p><b>Highlight:</b> ...</p>
  </div>
</div>
```

### 4.3 论文 tag 分级体系

每篇论文的 `data-tags` 按以下层级分类：

- **作者位次**：`First/Co-First Author`、`Other`
- **中稿层次**：`CCF-A`、`CCF-B`、`Preprint`
- **中稿类型**：`Conference`、`Journal`、`Oral`、`Poster`
- **领域**：`Embodied AI`、`Computer Vision`、`Medical Imaging`、`Data-centric AI`
- **关注重心/技术路线**：`VLA`、`Benchmark`、`Agentic`、`World Model`、`MoE`、`Data Augmentation`、`MLLM`

避免散装的 tag，尽量落在上述层级里。

### 4.4 论文 teaser 图

- 推荐尺寸：宽度约 500px，高度约 300px。
- 来源：从 arXiv 下载源文件中的 PDF figure，然后转换/裁剪。
- 常用命令：

```bash
# 下载 arXiv 源
cd /tmp
wget https://arxiv.org/e-print/2409.16183 -O source.tar.gz
tar -xzf source.tar.gz

# 找到 figure PDF（通常在 figures/ 或主目录）
# 转换为 png
pdftoppm -png -r 150 figure.pdf output
# 或 ImageMagick
convert -density 150 figure.pdf -resize 500x300^ output.png
```

- 转换后放到 `images/` 目录，并在 `_pages/about.md` 中引用。
- 注意：某些 arXiv 论文源文件不是标准 gzip 格式，下载可能失败（如 Radiology VLM），此时保留占位图 `images/500x300.png`。

---

## 5. Google Scholar 引用自动更新

### 5.1 配置 Secret

1. 打开仓库 Settings → Secrets and variables → Actions。
2. New repository secret：
   - Name: `GOOGLE_SCHOLAR_ID`
   - Value: `SgeV4NkAAAAJ`

### 5.2 工作原理

- 爬虫脚本：`google_scholar_crawler/main.py`
- 使用 `scholarly` 库抓取 Google Scholar 数据。
- 生成两个 JSON 文件：
  - `results/gs_data.json`：完整学者数据。
  - `results/gs_data_shieldsio.json`：shields.io 格式引用数徽章。
- 通过 `.github/workflows/google_scholar_crawler.yaml` 每天 08:00 UTC 运行一次，结果推送到 `google-scholar-stats` 分支。
- 首页通过 jsdelivr CDN 读取该分支数据：
  ```html
  https://cdn.jsdelivr.net/gh/yulin-luo/yulin-luo.github.io@google-scholar-stats/google-scholar-stats/gs_data_shieldsio.json
  ```

### 5.3 手动运行

```bash
cd google_scholar_crawler
pip install -r requirements.txt
GOOGLE_SCHOLAR_ID=SgeV4NkAAAAJ python main.py
```

---

## 6. GitHub Actions 踩坑记录

### 6.1 最初的 Jekyll Actions workflow 超时 6 小时

- 原因：GitHub cache 服务不稳定，`setup-ruby` 的 `bundler-cache: true` 卡住。
- 尝试：改为 `bundler-cache: false` + 手动 `bundle install`。
- 结果：build 能跑完，但 deploy 阶段仍偶发失败，并伴随 Node 20 deprecation 警告。

### 6.2 最终方案

放弃 GitHub Pages 的 artifact/deploy 流程，改用 **本地构建 + `gh-pages` 分支**。彻底绕开：

- `actions/deploy-pages` / `actions/upload-pages-artifact`
- Node 20 相关 deprecation 警告
- GitHub cache 服务不稳定

保留的 `.github/workflows/deploy.yml` 作为自动部署后备，但主流程以本地构建为准。

---

## 7. 常用命令速查

```bash
# 本地预览
bundle exec jekyll serve

# 生产构建
JEKYLL_ENV=production bundle exec jekyll build

# 推送到 gh-pages（在 _site/ 内）
git push git@github.com:yulin-luo/yulin-luo.github.io.git gh-pages --force

# 手动运行 Scholar 爬虫
GOOGLE_SCHOLAR_ID=SgeV4NkAAAAJ python google_scholar_crawler/main.py
```

---

## 8. TODO / 待完善

- [ ] 补齐剩余论文（MC-LLaVA、WoW、Wow-wo-val、MoASE++）的 teaser 图和 tag。
- [ ] 替换 Radiology VLM 的占位图。
- [ ] 删除/归档 David Dai 原模板的 `_posts/` 博客和 `self_introduction.md` 旧介绍。
- [ ] 决定 Interests 部分内容或移除该 section。
- [ ] 定期验证 Google Scholar 爬虫是否正常工作。

---

## 9. 参考

- [AcadHomepage](https://github.com/RayeRen/acad-homepage.github.io) Jekyll theme
- [Jekyll 官方文档](https://jekyllrb.com/docs/)
- [GitHub Pages 文档](https://docs.github.com/en/pages)
- [scholarly 库](https://github.com/scholarly-python-package/scholarly)

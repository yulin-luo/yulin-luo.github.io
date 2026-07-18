# Yulin Luo 个人主页 — Handoff 文档

> 创建时间：2026-07-03
> 当前接手任务：修复 `https://yulin-luo.github.io/` 的 sidebar 与正文重叠问题

---

## 1. 当前状态

- **站点地址**: https://yulin-luo.github.io/
- **源码仓库**: https://github.com/yulin-luo/yulin-luo.github.io
- **部署方式**: GitHub Actions 官方 Pages 部署（已生效）
- **本地目录**: `/mnt/luoyulin_code/luoyulin/experience_v4/personal_web/`

---

## 2. 已完成修复（已 push 到 main，Actions 已部署）

| 问题 | 修复文件 | 说明 |
|---|---|---|
| 页面 `<head>` 内嵌套重复的 `<html>/<head>` | `_includes/head.html` | 已清理为只保留 `<base target="_blank">` |
| Publications 下拉过滤器点击无反应，JS 报错 `filterContainer is not defined` | `_pages/about.md` | 已改为 `const filterContainer = document.getElementById('filter-container');` 并加空值保护 |
| 引用数 `~785 citations` 写死，无法随 Google Scholar 更新 | `_pages/about.md` | 已包在 `<span id="total_cit">~785</span>` 中 |
| 部署不生效（线上一直卡在旧版） | `.github/workflows/deploy.yml` | 已改为 `actions/upload-pages-artifact@v3` + `actions/deploy-pages@v4` 官方部署 |
| GitHub Pages Source 设置错误 | 仓库 Settings → Pages | 已改为 **Source: GitHub Actions** |

验证线上已更新的标志（curl 检查）：
- `<html lang="en" class="no-js">` 数量为 1
- `const filterContainer = document.getElementById('filter-container');` 存在
- `<span id="total_cit">` 存在

---

## 3. 仍未解决的问题

### 3.1 Sidebar 与正文重叠（P0）

**现象**: 在桌面端浏览器中，左侧 sidebar（头像 + 姓名 + bio + 联系方式）与右侧 main content 发生重叠。具体表现为：
- sidebar 的文字/链接侵入正文区域
- “Yulin Luo is a PhD student at Peking University...” 这段文字与 About 段落重叠
- 参考用户截图（2026-07-03）

**可能原因**:
1. `accent-enhancements.css` 中对 `.sidebar` 设置了 `max-width: 220px`，但主题默认布局可能没有正确分配 main content 的 margin/offset。
2. 主题本身对 sidebar sticky + width 的计算与自定义样式冲突。
3. `_config.yml` 中 `author_profile: true` 与自定义 sidebar 样式叠加。
4. `author__urls-wrapper` 中 `site.description` 较长，撑开了 sidebar 宽度。

**建议排查方向**:
- 检查 `assets/css/main.css` 中 `.sidebar`、`.page`、`.page__content` 的默认 grid/float 布局。
- 对比原始 AcadHomepage 主题的 sidebar 宽度（默认约 250px），看是否因为当前 sidebar 太窄导致文字换行后溢出。
- 尝试给 main content 增加 `margin-left` 或 padding，确保与 sidebar 不重叠。
- 考虑使用 CSS Grid/Flex 明确分隔 sidebar 和 main content，而不是依赖主题默认的浮动布局。

### 3.2 Google Scholar Citation Workflow 未手动触发验证（P1）

- Workflow 文件: `.github/workflows/google_scholar_crawler.yaml`
- 当前环境缺少 `gh` CLI 和 GitHub token，无法自动触发。
- 需要用户手动在 [Actions → Get Citation Data](https://github.com/yulin-luo/yulin-luo.github.io/actions/workflows/google_scholar_crawler.yaml) 点击 **Run workflow**。
- 同时确认仓库 Secret 已设置: `GOOGLE_SCHOLAR_ID = SgeV4NkAAAAJ`。

---

## 4. 本地开发环境

```bash
cd /mnt/luoyulin_code/luoyulin/experience_v4/personal_web
ruby -v        # 3.2.3
bundle -v      # 4.0.15
bundle exec jekyll -v  # 4.4.1
bundle exec jekyll serve      # http://127.0.0.1:4000
JEKYLL_ENV=production bundle exec jekyll build  # 构建到 _site/
```

**注意**: 不要升级 `tokenizers` 等依赖；本站使用 Jekyll 4.x，不是 GitHub Pages 默认的 Jekyll 3.9。

---

## 5. 关键文件

| 文件 | 作用 |
|---|---|
| `_pages/about.md` | 首页主体内容（About / News / Educations / Publications / Awards / Services / Interests） |
| `_includes/head.html` | `<head>` 模板 |
| `_includes/author-profile.html` | 左侧 sidebar 模板 |
| `assets/css/accent-enhancements.css` | 自定义样式（sidebar 宽度、paper-box、filter-bar 等） |
| `_config.yml` | 站点配置、作者信息 |
| `.github/workflows/deploy.yml` | GitHub Actions 部署 workflow |
| `.github/workflows/google_scholar_crawler.yaml` | Google Scholar 引用自动更新 workflow |
| `README-DEV.md` | 本项目的开发者笔记 |

---

## 6. 建议下一步（给 codex）

1. 在本地 `bundle exec jekyll serve`，打开 Chrome DevTools 检查 sidebar 和 main content 的实际盒模型。
2. 修复 `accent-enhancements.css` 中的 sidebar/main content 布局冲突。
3. 本地验证无误后 push 到 `main`。
4. 等待 GitHub Actions 跑完（约 1–2 分钟），再访问 https://yulin-luo.github.io/ 确认。
5. 提醒用户手动触发 Google Scholar workflow 并验证引用数更新。

---

## 7. 参考资料

- 原始模板: [AcadHomepage](https://github.com/RayeRen/acad-homepage.github.io)
- Jekyll 文档: https://jekyllrb.com/docs/
- GitHub Pages 文档: https://docs.github.com/en/pages
- 本目录 README-DEV.md 记录了部署流程和踩坑经验

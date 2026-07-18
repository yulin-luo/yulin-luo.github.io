# Personal Homepage Reference Library

This folder keeps raw snapshots and structured notes for academic personal homepages that are useful references for improving Yulin Luo's homepage.

## References

| Site | Local raw snapshot | Local notes | Main lessons |
|---|---|---|---|
| https://arctanxarc.github.io/ | `raw/arctanxarc.github.io.html` | `notes/arctanxarc.github.io.txt` | Strong personal motivation block, explicit contact section, clear academic evidence sections, project cards with code/star evidence. |
| https://tianxingchen.github.io/ | `raw/tianxingchen.github.io.html` | `notes/tianxingchen.github.io.txt` | Dense but scannable left-profile/top-profile style, icon-based social row, highlighted news, compact publication cards, strong project/community evidence. |
| https://rongyu.me/ | `raw/rongyu.me.html` | `notes/rongyu.me.txt` | Research-path framing, grants/internships/talks/teaching as extended identity evidence, visible CCF/CAS labels and GitHub star badges. |

## Reusable Lessons

### First-Screen Identity

- Keep the researcher's name, role, affiliation, advisor, and one-sentence academic brand immediately visible.
- Use icon links for Email, GitHub, Google Scholar, CV, and Homepage instead of long text rows when space is tight.
- Preserve a short bio on the left or top area so the page does not feel empty, but avoid repeating the same research focus sentence.

### Academic Brand

- State the research agenda in one compact sentence before listing evidence.
- For Yulin's current homepage, the best compact brand remains: `Open-World Generalization for Embodied Intelligence`.
- Follow the three-axis explanation: model generalization, embodied data/benchmark construction, and model-data co-evolution.

### News

- Make news items more than venue announcements: add a short phrase describing what the work contributes.
- Highlight venue names or awards, not every abbreviation uniformly.
- Use anchors from news items to publication cards when the item mentions a specific paper.
- Keep news inside a bounded scroll or collapsed window if the list grows too long.

### Publications

- Use complete project images or method/teaser figures, not partial screenshots with white margins.
- Put visually secondary tags near venue/resource metadata, not above author names.
- Keep resource links on one line where possible: Paper / Project / Code / Dataset / Demo.
- Sort publications with a declared rule. For this homepage, use reverse chronological arXiv/release order unless the user asks for Google Scholar ordering.

### Evidence Beyond Papers

- Education, internships, awards, service, talks, and selected open-source projects can support the researcher's identity when kept concise.
- Do not add unreliable visitor counters or numbers that can be manually set without evidence.
- Show GitHub stars only for real repositories when useful, and remember stars are repository-specific and cannot be merged across separate repos.

## Update Workflow

1. Add a URL to the benchmark list.
2. Fetch the HTML snapshot into `raw/`.
3. Extract headings, representative links, images, class tokens, and text sample into `notes/`.
4. Update this README with concrete lessons, not generic praise.
5. Apply only lessons that fit Yulin's academic brand and current site structure.

Use the skill at `../../skills/visual-communication/personal-homepage-benchmark/` for future scans and improvement passes.

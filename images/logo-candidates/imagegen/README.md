# Yulin Luo Logo Imagegen Candidates

This folder is reserved for AI-generated logo candidates for the personal website favicon / site mark.

Current status:
- Local programmatic candidates are available one level up in `images/logo-candidates/`.
- The OpenAI-compatible endpoint in `/mnt/luoyulin_code/luoyulin/.codex/config.toml` is reachable for `/models`.
- `/images/generations` currently returns `502 upstream_error` for `gpt-image-2`, `gpt-image-1.5`, and `gpt-image-1`.
- `/responses` with `tools: [{"type":"image_generation"}]` returns encrypted response content only, not a directly usable PNG/base64 payload.

Do not replace the live favicon from this folder until a candidate is visually selected.

## Directions to generate

1. `yl-openworld-imagegen.png`  
   Open-world YL monogram: bold `YL`, dark navy base, subtle open-world trajectory / constellation / horizon grid.

2. `yl-embodied-brain-imagegen.png`  
   Embodied brain mark: bold `YL`, abstract robot-head / embodied-brain neural motif, minimal and favicon-legible.

3. `yl-generalization-ladder-imagegen.png`  
   Generalization ladder: bold `YL`, abstract five-level ascent toward open-world horizon, no tiny L1-L5 labels.

4. `yl-model-data-loop-imagegen.png`  
   Model-data loop: bold `YL`, orbital feedback loop connecting model / data / embodied-world nodes.

Palette: deep navy `#012F63`, near-black, coral `#FE667B`, cyan/blue accents.
Avoid: human face, mascot robot, extra words, dense circuits, watermark, small unreadable text.

\
#!/usr/bin/env python3
from pathlib import Path
import base64
import json
import re
import time
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parents[3]
CFG = Path('/mnt/luoyulin_code/luoyulin/.codex/config.toml')
OUTDIR = Path(__file__).resolve().parent

cfg = CFG.read_text(errors='replace')
base_url = re.search(r'(?m)^base_url\s*=\s*"([^"]+)"', cfg).group(1).rstrip('/')
token = re.search(r'(?m)^experimental_bearer_token\s*=\s*"([^"]+)"', cfg).group(1)
headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}

def request_json(path, payload=None, timeout=420):
    data = None if payload is None else json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(base_url + path, data=data, headers=headers, method='GET' if data is None else 'POST')
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, json.loads(r.read().decode('utf-8', errors='replace'))
    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8', errors='replace')
        raise RuntimeError(f'HTTP {e.code}: {body[:2500]}')

prompts = [
    ('yl-openworld-imagegen.png', 'Create a polished square personal academic logo for Yulin Luo, an embodied AI researcher focused on open-world generalization for robot intelligence. Dominant readable mark: bold YL monogram. Integrate a subtle open-world trajectory: horizon grid, constellation nodes, and one upward path suggesting generalization beyond closed benchmarks. Premium minimal vector-like raster logo, clean tech-academic brand, crisp edges. Centered square mark, strong silhouette at favicon size, generous padding, rounded-square or circular dark base allowed. Palette: deep navy #012F63, near-black, accent coral pink #FE667B, small cyan/blue highlights. Text must be exactly "YL" only. No extra words, no face, no robot mascot, no clutter, no watermark.'),
    ('yl-embodied-brain-imagegen.png', 'Create a polished square personal academic logo for Yulin Luo representing embodied foundation models and robot intelligence. Dominant readable mark: bold YL monogram. Integrate a very abstract robot head / embodied brain motif with subtle neural nodes and sensor arcs around or behind the monogram. Minimal vector-like raster logo, academic AI lab aesthetic, premium and simple. Palette: deep navy #012F63, graphite, accent coral pink #FE667B, cyan highlights. Text must be exactly "YL" only. Favicon-legible, no human face, no cartoon robot, no extra text, no watermark, avoid dense circuit-board clutter.'),
    ('yl-generalization-ladder-imagegen.png', 'Create a polished square personal academic logo for open-world generalization in embodied intelligence. Dominant readable mark: bold YL monogram. Add a simplified five-level ascent or ladder/path from closed in-domain tasks toward an open-world horizon, using abstract steps without tiny labels. Minimal vector-like raster logo, clean scientific branding, crisp modern mark. Centered square, YL remains dominant, ladder/path is secondary and readable as upward progression. Palette: deep navy #012F63, black, accent coral pink #FE667B, cyan/blue highlights. Text must be exactly "YL" only. Do not write L1-L5 labels, no small unreadable text, no extra words, no watermark, avoid clutter.'),
    ('yl-model-data-loop-imagegen.png', 'Create a polished square personal academic logo for model-data co-evolution in embodied AI. Dominant readable mark: bold YL monogram. Surround it with a clean orbital loop connecting three abstract nodes: model, data, and embodied world/robot. The loop should suggest continual scaling and feedback. Minimal vector-like raster logo, premium academic/AI startup feel, crisp edges. Palette: deep navy #012F63, near-black, accent coral pink #FE667B, cyan highlights. Text must be exactly "YL" only. Favicon-legible, no extra words, no face, no detailed robot, no watermark, avoid busy diagrams.'),
]

_, models = request_json('/models', timeout=30)
ids = [m.get('id') for m in models.get('data', []) if isinstance(m, dict)]
model = 'gpt-image-2' if 'gpt-image-2' in ids else ('gpt-image-1.5' if 'gpt-image-1.5' in ids else 'gpt-image-1')
print('using_model', model)

for filename, prompt in prompts:
    out = OUTDIR / filename
    payloads = [
        {'model': model, 'prompt': prompt, 'n': 1, 'size': '1024x1024', 'quality': 'high', 'output_format': 'png'},
        {'model': model, 'prompt': prompt, 'n': 1, 'size': '1024x1024', 'quality': 'high'},
        {'model': model, 'prompt': prompt, 'n': 1, 'size': '1024x1024'},
    ]
    print('generating', filename, flush=True)
    start = time.time()
    resp = None
    last = None
    for payload in payloads:
        try:
            _, resp = request_json('/images/generations', payload, timeout=420)
            break
        except Exception as exc:
            last = exc
            msg = str(exc).lower()
            if not any(k in msg for k in ['quality', 'output_format', 'unknown', 'unrecognized', 'invalid']):
                raise
    if resp is None:
        raise RuntimeError(last)
    item = (resp.get('data') or [{}])[0]
    b64 = item.get('b64_json') or item.get('b64') or item.get('image')
    if b64:
        raw = base64.b64decode(b64)
    elif item.get('url'):
        with urllib.request.urlopen(item['url'], timeout=180) as r:
            raw = r.read()
    else:
        raise RuntimeError(f'Unsupported image response for {filename}: {json.dumps(item)[:1200]}')
    out.write_bytes(raw)
    print('wrote', out, len(raw), 'bytes', round(time.time() - start, 1), 'seconds')

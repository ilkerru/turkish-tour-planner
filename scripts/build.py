import os, glob, yaml
from jinja2 import Environment, FileSystemLoader
ROOT = os.path.dirname(os.path.dirname(__file__))
ITIN_DIR = os.path.join(ROOT, 'itineraries')
TPL_DIR = os.path.join(ROOT, 'templates')
DOCS_DIR = os.path.join(ROOT, 'docs')
env = Environment(loader=FileSystemLoader(TPL_DIR), autoescape=False, trim_blocks=True, lstrip_blocks=True)
os.makedirs(DOCS_DIR, exist_ok=True)
items = []
for path in sorted(glob.glob(os.path.join(ITIN_DIR, '*.yaml'))):
    with open(path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        if data: items.append(data)
with open(os.path.join(DOCS_DIR, 'index.md'), 'w', encoding='utf-8') as f:
    f.write(env.get_template('index.md.j2').render(items=items))
for data in items:
    with open(os.path.join(DOCS_DIR, f"{data['id']}.md"), 'w', encoding='utf-8') as f:
        f.write(env.get_template('itinerary.md.j2').render(data=data))
print(f"Built {len(items)} itineraries → docs/")
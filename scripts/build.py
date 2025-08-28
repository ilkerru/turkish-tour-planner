import os
import glob
import yaml
from jinja2 import Environment, FileSystemLoader

ROOT = os.path.dirname(os.path.dirname(__file__))
ITIN_DIR = os.path.join(ROOT, 'itineraries')
TPL_DIR = os.path.join(ROOT, 'templates')
DOCS_DIR = os.path.join(ROOT, 'docs')

env = Environment(loader=FileSystemLoader(TPL_DIR), autoescape=False, trim_blocks=True, lstrip_blocks=True)

os.makedirs(DOCS_DIR, exist_ok=True)

# Load itineraries
items = []
for path in sorted(glob.glob(os.path.join(ITIN_DIR, '*.yaml'))):
    with open(path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        if not data:
            continue
        items.append(data)

# Write each itinerary page
itinerary_tpl = env.get_template('itinerary.md.j2')
for data in items:
    out_path = os.path.join(DOCS_DIR, f"{data['id']}.md")
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(itinerary_tpl.render(data=data))

# Write index page
index_tpl = env.get_template('index.md.j2')
with open(os.path.join(DOCS_DIR, 'index.md'), 'w', encoding='utf-8') as f:
    f.write(index_tpl.render(items=items))

print(f"Built {len(items)} itineraries → docs/")

# turkish-tour-planner
Türkiye’de şehir şehir programlı gezi turları planlamak için hafif, tekrarlanabilir ve GitHub Pages'e yayınlanabilir bir repo şablonu.

## Özellikler
- YAML ile şehir/tema bazlı itinerári yazımı
- Jinja2 şablonlarıyla Markdown üretimi
- MkDocs + Material tema ile statik site
- GitHub Actions ile otomatik deploy

## Hızlı Başlangıç
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python scripts/build.py
mkdocs serve
```

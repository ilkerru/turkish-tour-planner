# İstanbul — Yürünebilir Rotalar (GitHub Pages)

Bu repo, **İstanbul'un farklı ilçelerinde** (Fatih, Kuzguncuk, Beyoğlu, Üsküdar, Kadıköy) yürüyüş mesafesine göre gruplanmış gezi planlarını içerir.  
Her rota:

- **Yürüyüş klasterleri** (yakın duraklar)
- **Yeme‑içme önerileri**
- **Dini mekân ziyaret saatleri**
- **Müze/çarşı kapalı günleri**
- **Bilet/rezervasyon bağlantıları**

## İçerik

- `itineraries/` → Her bölge için YAML formatında ham rota verisi.
- `templates/` → Jinja2 şablonları (`itinerary.md.j2`, `index.md.j2`).
- `scripts/build.py` → YAML → `docs/*.md` dönüştürücüsü.
- `docs/` → MkDocs’un kullandığı Markdown dokümanları (otomatik üretilir).
- `.github/workflows/gh-pages.yml` → GitHub Actions ile otomatik build & Pages yayını.
- `requirements.txt` → Gerekli Python paketleri.

## Kullanım

### Yerelde Önizleme

```bash
python -m venv .venv && source .venv/bin/activate   # (Win: .venv\Scripts\activate)
pip install -r requirements.txt
python scripts/build.py
mkdocs serve   # http://127.0.0.1:8000
```

### GitHub Pages Yayını

1. Repo’yu GitHub’a yükleyin.
2. `main` dalına push edin.
3. **Settings → Pages → Source: GitHub Actions** seçin.
4. Her push’tan sonra Actions çalışır ve site otomatik güncellenir.

## Örnek Rotalar

- **Fatih** — 3 gün (Sultanahmet, Eminönü, Fener‑Balat)
- **Kuzguncuk** — 1 gün (İcadiye, sahil, bostan)
- **Beyoğlu** — 2 gün (Galata, Karaköy, İstiklal, Pera, Taksim)
- **Üsküdar** — 1 gün (Mihrimah, Şemsipaşa, Kız Kulesi, Çamlıca)
- **Kadıköy** — 1 gün (Çarşı, Süreyya Operası, Barış Manço Evi, Moda, Yeldeğirmeni)

---

© 2025 — Gezi planları bilgilendirme amaçlıdır. Saatler/kapalı günler değişebilir, resmi kaynaklardan teyit ediniz.

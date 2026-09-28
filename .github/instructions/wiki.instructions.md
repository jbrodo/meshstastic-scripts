---
description: "Use when writing OKF v0.2 wiki concepts about Heltec hardware and Meshtastic."
applyTo: "wiki/**/*.md"
---
# Wiki OKF

- Seguire [OKF v0.2](https://raw.githubusercontent.com/GoogleCloudPlatform/knowledge-catalog/refs/heads/main/okf/SPEC.md).
- Per i concetti usare frontmatter YAML parseabile con `type` non vuoto;
  `index.md` e `log.md` sono riservati. Solo l'indice radice puo dichiarare
  `okf_version` nel frontmatter.
- Aggiungere fonti in `sources` e collegare le affermazioni verificabili con
  footnote basate sugli `id` delle fonti. Non inventare `verified` o timestamp
  di ispezioni hardware non avvenute.
- Usare link Markdown tra concetti del bundle; mantenere l'indice aggiornato.
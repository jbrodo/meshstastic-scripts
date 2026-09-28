---
type: Playbook
title: Ispezione del nodo locale
description: Lettura USB controllata senza modifica della configurazione o invio radio.
tags: [workflow, usb, testing]
status: draft
sources:
  - id: cli-doc
    resource: https://meshtastic.org/docs/software/python/cli/
    title: Guida Meshtastic Python CLI
  - id: cp210x-driver
    resource: https://www.silabs.com/software-and-tools/usb-to-uart-bridge-vcp-drivers?tab=downloads
    title: Download ufficiale CP210x VCP di Silicon Labs
---
# Preparazione

1. Collegare l'[Heltec V3](heltec-v3.md) con Meshtastic installato via USB.
2. Su Windows verificare la porta con
    `uv run python -m serial.tools.list_ports -v`. Se il CP2102 compare in
    Gestione dispositivi con codice 28 e manca la porta USB, installare il
    [driver CP210x VCP ufficiale](https://www.silabs.com/software-and-tools/usb-to-uart-bridge-vcp-drivers?tab=downloads)
    e controllare nuovamente l'elenco.[^cp210x-driver]
3. Identificare la porta corretta nel sistema; specificare `--port` se sono
    collegati piu dispositivi.[^cli-doc]
4. Chiudere Web Flasher, Web Client e altri programmi che usano la seriale
    prima di avviare Python; un solo client puo aprire la porta alla volta.

# Esecuzione

```powershell
uv run python main.py --port COM5
uv run python main.py --port COM5 --json
```

`COM5` e la porta osservata nella sessione del 28 settembre 2026, non una
porta universale. Sostituirla con quella rilevata sul proprio PC.
La CLI legge solo il nodo locale tramite l'[API Meshtastic](meshtastic.md),
chiude la connessione anche in caso di errore e non chiede telemetria remota.
Prima di condividere il JSON, rimuovere identificativi e dati di posizione.

# Verifica senza dispositivo

```powershell
py -3.10 -m unittest -v test_main
```

Un test simulato non dimostra compatibilita con ogni firmware o porta USB:
la verifica fisica richiede un dispositivo reale e conferma esplicita.

[^cli-doc]: Guida CLI Python Meshtastic, opzione `--port`.
[^cp210x-driver]: Download del driver CP210x VCP dal produttore Silicon Labs.
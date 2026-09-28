---
name: meshtastic-workflow
description: "Use when extending Heltec LoRa 32 V3 Meshtastic USB inspection, investigating serial failures, or updating the OKF device wiki with hardware evidence."
---
# Workflow Meshtastic

1. Apri [l'indice OKF](../../../wiki/index.md), poi il concetto hardware o API
   interessato; controlla le fonti ufficiali collegate e marca le ipotesi.
2. Determina se il compito richiede sola lettura, configurazione, flash o
   trasmissione. Per ogni azione non di sola lettura chiedi consenso esplicito,
   porta, revisione hardware, banda e regione prima di toccare il dispositivo.
3. Riproduci senza hardware tramite mock quando possibile. Se serve USB reale,
   chiedi la porta e usa solo quella indicata; non usare output completo in log
   o commit senza anonimizzare identificativi, posizione e chiavi.
4. Modifica codice e concetti OKF insieme quando cambia un comportamento
   documentato: `type`, `sources`, `status` e link devono rimanere coerenti.
   Non scrivere `verified` per un test simulato.
5. Esegui `uv run python -m unittest -v test_main` e verifica `--help`. Riferisci
   separatamente prove locali e verifica sul dispositivo fisico.
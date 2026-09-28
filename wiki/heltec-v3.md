---
type: Hardware Device
title: Heltec LoRa 32 V3/V3.1
description: Scheda ESP32-S3 con transceiver SX1262 supportata da Meshtastic.
resource: https://meshtastic.org/docs/hardware/devices/heltec-automation/lora32/?heltec=v3
tags: [heltec, esp32, lora, meshtastic]
status: draft
sources:
  - id: heltec-doc
    resource: https://meshtastic.org/docs/hardware/devices/heltec-automation/lora32/?heltec=v3
    title: Meshtastic HELTEC LoRa 32 V3/V3.1
---
# Hardware

La V3/V3.1 usa ESP32-S3FN8 e radio Semtech SX1262; dispone di display OLED
da 0,96 pollici, pulsanti User/Reset e non integra GPS.[^heltec-doc]
Il connettore LoRa e U.FL/IPEX; controllare che l'antenna sia collegata prima
di usare la radio. Le varianti di frequenza non sono intercambiabili: verificare
la banda dell'esemplare e le regole del paese.[^heltec-doc]

# Collegamento

Usare USB-C per la connessione seriale alla [CLI locale](inspection.md). La
documentazione segnala che la ricarica puo dare problemi con cavi USB-C/USB-C
e consiglia USB-A/USB-C; segnala anche l'assenza di protezione ESD sulla porta
USB-C del bridge CP2102.[^heltec-doc]

# Pin I2C

Le definizioni Meshtastic indicano SDA GPIO41 e SCL GPIO42.[^heltec-doc]
Non collegare sensori o alimentazioni senza verificare schema e tensioni
della propria revisione hardware.

[^heltec-doc]: Documentazione Meshtastic Heltec LoRa 32.
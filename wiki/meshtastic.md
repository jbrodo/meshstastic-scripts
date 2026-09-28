---
type: Reference
title: Meshtastic e API seriale Python
description: Rete mesh LoRa e API locale per ottenere informazioni dal nodo.
resource: https://meshtastic.org/docs/introduction/
tags: [meshtastic, python, serial]
status: draft
sources:
  - id: intro
    resource: https://meshtastic.org/docs/introduction/
    title: Introduzione a Meshtastic
  - id: python-api
    resource: https://python.meshtastic.org/serial_interface.html
    title: API Python SerialInterface
  - id: node-api
    resource: https://python.meshtastic.org/mesh_interface.html
    title: API Python MeshInterface
---
# Rete

Meshtastic usa LoRa per comunicazioni mesh decentralizzate; i dispositivi
possono ritrasmettere i messaggi ricevuti.[^intro] Il nodo locale trattato in
questo progetto e l'[Heltec LoRa 32 V3](heltec-v3.md).

# API

`SerialInterface(devPath=...)` apre la connessione USB; se il percorso manca,
la libreria tenta di trovare un dispositivo compatibile.[^python-api]
`getMyNodeInfo()` restituisce il dizionario del nodo locale oppure `None`;
`close()` chiude l'interfaccia.[^node-api] L'apertura della sessione scambia
messaggi di protocollo via USB: "sola lettura" qui indica che lo script non
modifica impostazioni e non chiama API di invio di pacchetti LoRa.

[^intro]: Introduzione ufficiale Meshtastic.
[^python-api]: Documentazione Python SerialInterface.
[^node-api]: Documentazione Python MeshInterface.
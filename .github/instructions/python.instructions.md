---
description: "Use when editing Python Meshtastic serial inspection, CLI behavior or hardware tests."
applyTo: "**/*.py"
---
# Codice Python

- Usare `SerialInterface` solo per operazioni locali esplicitamente richieste.
- Chiudere sempre la connessione, anche se la lettura fallisce.
- Non chiamare `sendText`, `sendData`, `sendTelemetry` o metodi di modifica nelle
  funzioni di ispezione.
- Testare `--port`, `--json`, dati mancanti e gestione degli errori con mock;
  nessun test automatico deve aprire la porta USB reale.
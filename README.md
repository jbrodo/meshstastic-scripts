# Meshtastic Scripts

CLI Python per leggere via USB le informazioni del nodo locale Meshtastic, pensata
per Heltec LoRa 32 V3/V3.1. Non installa firmware, non cambia la configurazione
radio e non invia messaggi nella mesh. La connessione seriale scambia comunque
messaggi di protocollo con il dispositivo. Il riepilogo mostra le metriche
locali gia disponibili, senza richiedere telemetria remota.

## Avvio

Richiede Python 3.10+ e un Heltec con firmware Meshtastic collegato via USB.
Installare le dipendenze e individuare prima la porta seriale del dispositivo:

```powershell
uv sync --python 3.10
uv run python -m serial.tools.list_ports -v
```

Usare con `--port` la porta effettivamente rilevata (per esempio `COM7`,
non necessariamente `COM4`); senza `--port` la libreria cerca un dispositivo:

```powershell
uv run python main.py
uv run python main.py --port COM7 --json
```

`COM7` e solo un esempio. Se nell'elenco compare soltanto `COM1` con hardware
`ACPI\PNP0501`, Windows non vede l'Heltec via USB: controllare che sia acceso,
provare un cavo dati USB-A/USB-C e un'altra porta USB, poi verificare in
Gestione dispositivi se manca il [driver CP210x VCP per Windows di Silicon Labs](https://www.silabs.com/software-and-tools/usb-to-uart-bridge-vcp-drivers?tab=downloads).
Il codice 28 del bridge CP2102 indica un driver mancante; dopo l'installazione
ricontrollare la porta con `uv run python -m serial.tools.list_ports -v`.
Non provare `COM1` come porta
del nodo. Su Linux/macOS usare la porta rilevata (ad esempio `/dev/ttyUSB0`).
Chiudere altri client seriali prima di avviare la CLI. L'output JSON puo
contenere identificativi, posizione o altri metadati del nodo: non pubblicarlo
senza revisione.

Se la porta CP210x compare ma la connessione Meshtastic va in timeout, Windows
ha aperto la seriale ma lo script non ha ricevuto il completamento della
sessione dal dispositivo (attesa SDK di circa 30 secondi). Verificare che
nessun altro client usi la porta e che la scheda esegua firmware Meshtastic
per Heltec V3/V3.1, non un firmware Heltec generico. Non eseguire flash o reset
come parte di questa diagnosi senza una decisione esplicita.

Se non si usa `uv`: creare un venv con Python 3.10+, poi eseguire
`python -m pip install -e .` e `python main.py --port` seguito dalla porta
effettivamente rilevata.

```powershell
uv run python -m unittest -v test_main
```

I test simulano il dispositivo; l'accesso USB reale non e verificato dai test.

## Hardware e conoscenza

Verificare antenna, banda e normativa locale prima di usare la radio. Per la
prima installazione del firmware usare il [flasher ufficiale](https://flasher.meshtastic.org/)
e la documentazione del produttore; questo progetto non effettua il flash.
La [wiki OKF v0.2](wiki/index.md) riunisce hardware, protocollo e flusso operativo
con riferimenti alle fonti e al [registro delle attivita](wiki/log.md). Le personalizzazioni Copilot sono in `.github/`:
l'agente `Meshtastic Maintainer`, il prompt `/inspect-node` e la skill
`meshtastic-workflow` per modifiche che coinvolgono USB o radio.

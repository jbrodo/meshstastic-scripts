# Meshtastic Scripts

- Questo repository usa Python 3.10+, `uv` e l'SDK Python `meshtastic`.
- Leggere [l'indice OKF](../wiki/index.md) prima di modificare codice o fatti hardware.
- Rispettare la provenienza: ogni nuova voce `wiki/*.md` deve avere `type`,
  `sources` e uno `status` appropriato. Non aggiungere `verified` senza controllo reale.
- Il flusso predefinito e una lettura del nodo locale via USB. Non eseguire flash,
  reset, modifiche della configurazione o invio LoRa senza richiesta esplicita;
  chiedere porta, modello/revisione, banda/regione e consenso prima di azioni che
  cambiano lo stato del dispositivo o trasmettono via radio.
- Non mettere in repository chiavi di canale, token, ID privati o JSON grezzi
  acquisiti dal dispositivo. Mascherare i dati nelle segnalazioni di bug.
- Verificare con `uv run python -m unittest -v test_main`; i test simulati non
  equivalgono a una prova sul dispositivo fisico.
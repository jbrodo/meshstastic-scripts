# Registro aggiornamenti

## 2026-09-28

* **Diagnosi**: Windows mostrava solo `COM1` (`ACPI\PNP0501`); il bridge CP2102
  USB era rilevato con codice 28 (driver mancante).
* **Aggiornamento**: l'utente ha installato il driver CP210x VCP per Windows
  dal [sito Silicon Labs](https://www.silabs.com/software-and-tools/usb-to-uart-bridge-vcp-drivers?tab=downloads).
  In seguito e stata osservata una porta CP210x `COM5`. Vedi
  [ispezione locale](inspection.md).
* **Osservazione**: il log condiviso dall'utente mostra che il Web Flasher ha
  scritto il firmware Meshtastic per Heltec V3 e che il dispositivo si e
  avviato. La regione LoRa risultava `UNSET`, con trasmissione disabilitata.
  Non sono stati salvati log grezzi, MAC, identificativi o chiavi.
* **Limite**: la lettura Python su `COM5` ha raggiunto la porta ma e andata
  in timeout durante l'handshake. Il Web Client ha poi segnalato che non
  riusciva ad aprire la seriale. Una sessione USB funzionante con la CLI
  resta da confermare; non attribuire il blocco a una causa hardware certa.
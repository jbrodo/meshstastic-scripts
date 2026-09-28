"""Read a local Meshtastic node over USB without modifying its settings."""

import argparse
import json
import sys


def read_node(port: str | None = None) -> dict:
    from meshtastic.mesh_interface import MeshInterface
    from meshtastic.serial_interface import SerialInterface

    try:
        interface = SerialInterface(devPath=port)
    except MeshInterface.MeshInterfaceError as error:
        raise ConnectionError(f"Connessione Meshtastic non completata: {error}") from error
    try:
        info = interface.getMyNodeInfo()
        if info is None:
            raise ValueError("Il dispositivo non ha restituito informazioni sul nodo")
        return info
    finally:
        interface.close()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Legge le informazioni del nodo Meshtastic via USB")
    parser.add_argument("--port", help="Porta seriale, per esempio COM3 o /dev/ttyUSB0")
    parser.add_argument("--json", action="store_true", help="Stampa il risultato come JSON")
    args = parser.parse_args(argv)

    try:
        info = read_node(args.port)
    except (ConnectionError, ImportError, OSError, ValueError) as error:
        print(f"Impossibile leggere il nodo: {error}", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(info, indent=2, default=str))
    else:
        user = info.get("user", {})
        print(f"Nodo: {user.get('longName', 'sconosciuto')} ({user.get('id', 'id sconosciuto')})")
        print(f"Numero: {info.get('num', 'sconosciuto')}")
        metrics = info.get("deviceMetrics") or {}
        for field, label, unit in (
            ("batteryLevel", "Batteria", "%"),
            ("voltage", "Tensione", "V"),
            ("channelUtilization", "Canale occupato", "%"),
            ("airUtilTx", "Tempo TX", "%"),
        ):
            if field in metrics:
                print(f"{label}: {metrics[field]}{unit}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

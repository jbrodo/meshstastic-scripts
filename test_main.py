import contextlib
import io
import json
import sys
import types
import unittest
from unittest.mock import Mock, patch

import main


class NodeTests(unittest.TestCase):
    def setUp(self):
        self.interface = Mock()
        self.interface.getMyNodeInfo.return_value = {
            "num": 123,
            "user": {"longName": "Heltec", "id": "!123"},
        }
        serial_module = types.ModuleType("meshtastic.serial_interface")
        serial_module.SerialInterface = Mock(return_value=self.interface)
        mesh_module = types.ModuleType("meshtastic.mesh_interface")
        mesh_module.MeshInterface = type("MeshInterface", (), {
            "MeshInterfaceError": type("MeshInterfaceError", (Exception,), {}),
        })
        meshtastic_module = types.ModuleType("meshtastic")
        meshtastic_module.serial_interface = serial_module
        meshtastic_module.mesh_interface = mesh_module
        self.modules = patch.dict(sys.modules, {
            "meshtastic": meshtastic_module,
            "meshtastic.mesh_interface": mesh_module,
            "meshtastic.serial_interface": serial_module,
        })
        self.modules.start()
        self.addCleanup(self.modules.stop)
        self.serial = serial_module.SerialInterface
        self.connection_error = mesh_module.MeshInterface.MeshInterfaceError

    def test_reads_selected_port_and_closes(self):
        self.assertEqual(main.read_node("COM4")["num"], 123)
        self.serial.assert_called_once_with(devPath="COM4")
        self.interface.close.assert_called_once()

    def test_closes_when_node_is_missing(self):
        self.interface.getMyNodeInfo.return_value = None
        with self.assertRaisesRegex(ValueError, "non ha restituito"):
            main.read_node()
        self.interface.close.assert_called_once()

    def test_closes_when_reading_node_raises(self):
        self.interface.getMyNodeInfo.side_effect = RuntimeError("read failed")
        with self.assertRaisesRegex(RuntimeError, "read failed"):
            main.read_node()
        self.interface.close.assert_called_once()

    def test_json_output(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            result = main.main(["--port", "COM4", "--json"])
        self.assertEqual(result, 0)
        self.assertEqual(json.loads(output.getvalue())["num"], 123)
        self.serial.assert_called_once_with(devPath="COM4")

    def test_summary_shows_available_local_metrics(self):
        self.interface.getMyNodeInfo.return_value["deviceMetrics"] = {
            "batteryLevel": 82, "voltage": 4.1,
        }
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            result = main.main([])
        self.assertEqual(result, 0)
        self.assertIn("Batteria: 82%", output.getvalue())
        self.assertIn("Tensione: 4.1V", output.getvalue())
        self.assertNotIn("Tempo TX", output.getvalue())

    def test_error_output(self):
        self.interface.getMyNodeInfo.return_value = None
        errors = io.StringIO()
        with contextlib.redirect_stderr(errors):
            result = main.main([])
        self.assertEqual(result, 1)
        self.assertIn("Impossibile leggere", errors.getvalue())

    def test_connection_timeout_is_reported_without_traceback(self):
        self.serial.side_effect = self.connection_error("Timed out waiting for connection completion")
        errors = io.StringIO()
        with contextlib.redirect_stderr(errors):
            result = main.main(["--port", "COM5"])
        self.assertEqual(result, 1)
        self.assertIn("Connessione Meshtastic non completata", errors.getvalue())
        self.interface.getMyNodeInfo.assert_not_called()


if __name__ == "__main__":
    unittest.main()
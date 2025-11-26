import unittest
import subprocess
import requests
import time
import os

class TestEndToEnd(unittest.TestCase):
    def test_backend_api(self):
        url = "http://localhost:5000/api/devices"
        try:
            response = requests.get(url)
            self.assertEqual(response.status_code, 200)
            data = response.json()
            self.assertIn('status', data)
            self.assertEqual(data['status'], 'success')
        except Exception as e:
            self.fail(f"Backend API test failed: {e}")

    def test_app_collect_and_send(self):
        # Este teste assume que o app pode ser executado e gera o arquivo relatorio_celular.pdf
        # Depois tenta enviar esse arquivo via POST para o backend
        # Por limitações do ambiente o teste manual é recomendado,
        # mas deixamos este passo para integração futura automatizada
        self.skipTest("Teste manual recomendado para app GUI com geração de PDF e envio.")

if __name__ == '__main__':
    unittest.main()

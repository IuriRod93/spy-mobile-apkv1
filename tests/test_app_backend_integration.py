import unittest
import requests
import json

SERVER_URL = "https://147.79.111.118"

class TestBackendAPI(unittest.TestCase):
    def test_api_test_endpoint(self):
        url = f"{SERVER_URL}/api/test/"
        response = requests.get(url, verify=False)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('status', data)
        self.assertEqual(data['status'], 'success')

    def test_api_device_info_post(self):
        url = f"{SERVER_URL}/api/device-info/"
        payload = {
            "imei": "test_device_12345",
            "device_info": {
                "bateria_nivel": 85,
                "bateria_carregando": True,
                "armazenamento_total": 128000,
                "armazenamento_usado": 64000,
                "armazenamento_livre": 64000
            }
        }
        response = requests.post(url, json=payload, verify=False)
        self.assertIn(response.status_code, [200, 201])

    def test_api_localizacao_post(self):
        url = f"{SERVER_URL}/api/localizacao/"
        payload = {
            "imei": "test_device_12345",
            "latitude": -23.55052,
            "longitude": -46.633308
        }
        response = requests.post(url, json=payload, verify=False)
        self.assertIn(response.status_code, [200, 201])

    def test_api_atividade_rede_post(self):
        url = f"{SERVER_URL}/api/atividade-rede/"
        payload = {
            "imei": "test_device_12345",
            "ip": "192.168.1.100",
            "wifi_status": "connected"
        }
        response = requests.post(url, json=payload, verify=False)
        self.assertIn(response.status_code, [200, 201])

if __name__ == '__main__':
    unittest.main()

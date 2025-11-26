from flask import Flask, request, jsonify
from datetime import datetime
import json
import os
import sqlite3

app = Flask(__name__)

# Configuração
DATA_DIR = "received_data"
os.makedirs(DATA_DIR, exist_ok=True)

def init_database():
    """Inicializa o banco de dados SQLite"""
    conn = sqlite3.connect('mobile_data.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mobile_devices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            device_model TEXT,
            android_version TEXT,
            manufacturer TEXT,
            ip_address TEXT,
            collection_time TEXT,
            received_time TEXT,
            raw_data TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

@app.route('/api/mobile-data', methods=['POST'])
def receive_mobile_data():
    """Endpoint para receber dados dos celulares"""
    try:
        data = request.json
        received_time = datetime.now().isoformat()
        
        # Salva os dados brutos em arquivo
        filename = f"device_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        filepath = os.path.join(DATA_DIR, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        # Salva no banco de dados
        device_data = data.get('device_data', {})
        basic_info = device_data.get('basic_info', {})
        network_info = device_data.get('network_info', {})
        
        conn = sqlite3.connect('mobile_data.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO mobile_devices 
            (device_model, android_version, manufacturer, ip_address, collection_time, received_time, raw_data)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            basic_info.get('model', 'Unknown'),
            basic_info.get('android_version', 'Unknown'),
            basic_info.get('manufacturer', 'Unknown'),
            network_info.get('ip_address', 'Unknown'),
            device_data.get('collection_time', 'Unknown'),
            received_time,
            json.dumps(data)
        ))
        
        conn.commit()
        conn.close()
        
        print(f"Dados recebidos de: {basic_info.get('model', 'Unknown')}")
        
        return jsonify({
            'status': 'success',
            'message': 'Dados recebidos com sucesso',
            'received_at': received_time
        }), 200
        
    except Exception as e:
        print(f"Erro ao processar dados: {e}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/devices', methods=['GET'])
def get_devices():
    """Endpoint para listar dispositivos registrados"""
    try:
        conn = sqlite3.connect('mobile_data.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT device_model, android_version, manufacturer, ip_address, 
                   collection_time, received_time 
            FROM mobile_devices 
            ORDER BY received_time DESC
        ''')
        
        devices = cursor.fetchall()
        conn.close()
        
        result = []
        for device in devices:
            result.append({
                'model': device[0],
                'android_version': device[1],
                'manufacturer': device[2],
                'ip_address': device[3],
                'collection_time': device[4],
                'received_time': device[5]
            })
        
        return jsonify({
            'status': 'success',
            'devices': result,
            'count': len(result)
        }), 200
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

if __name__ == '__main__':
    init_database()
    app.run(host='0.0.0.0', port=5000, debug=True)
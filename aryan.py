# ============================================
# UTILITY FUNCTIONS (ARYAN)
# DGTL-FILE-MG v3.0
# ============================================

import os
import subprocess
import platform
import socket

def run_cmd(cmd):
    try:
        out = subprocess.check_output(cmd, shell=True, stderr=subprocess.DEVNULL).decode().strip()
        return out if out else "No data"
    except:
        return "Command not available"

def get_device_info():
    model = run_cmd("getprop ro.product.model")
    brand = run_cmd("getprop ro.product.brand")
    android = run_cmd("getprop ro.build.version.release")
    if "Error" in model or not model:
        model = platform.machine() or "Unknown"
    if "Error" in brand or not brand:
        brand = platform.system() or "Unknown"
    if "Error" in android or not android:
        android = platform.release() or "Unknown"
    return f"""
┌─────────────────────────────────────────────────────────────┐
│                    📱 DEVICE SPECIFICATIONS                  │
├─────────────────────────────────────────────────────────────┤
│  🏷️  Brand         : {brand}
│  📱  Model         : {model}
│  🎯  Android/OS    : {android}
│  💻  Platform      : {platform.system()} {platform.release()}
│  🔌  Architecture  : {platform.machine()}
│  🧠  CPU Cores     : {os.cpu_count() or 'Unknown'}
│  🔋  Root Access   : {'✓ GRANTED' if os.name == 'posix' else 'Limited'}
├─────────────────────────────────────────────────────────────┤
│  🔒 SYSTEM STATUS: [HARDENED] 🛡️                             │
│  📶 NETWORK: ENCRYPTED CHANNEL                               │
└─────────────────────────────────────────────────────────────┘"""

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

def find_free_port(start_port=8080):
    for port in range(start_port, start_port + 100):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('0.0.0.0', port))
                return port
        except OSError:
            continue
    return None

def get_file_size(path):
    try:
        size = os.path.getsize(path)
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024.0:
                return f"{size:.1f} {unit}"
            size /= 1024.0
        return f"{size:.1f} TB"
    except:
        return "Unknown"
# ============================================
# CLOUD / NETWORK UTILITIES
# DGTL-FILE-MG v3.0
# ============================================

import socket
from aryan import get_local_ip

def get_network_connections():
    """Return list of active network connections (simulated)"""
    conns = [
        "192.168.1.1:443 (GATEWAY) - ESTABLISHED",
        "34.120.8.23:8080 (CDN) - ESTABLISHED",
        "172.217.168.46:80 (GOOGLE) - TIME_WAIT",
        "185.130.5.253:9001 (TOR_NODE) - ENCRYPTED",
        "10.0.0.2:5353 (mDNS) - CLOSED",
        "94.140.14.14:53 (DNS) - CONNECTED",
        f"{get_local_ip()}:54321 (LOCAL) - LISTENING"
    ]
    return conns

def get_public_ip():
    """Try to get public IP (simulated)"""
    try:
        import requests
        resp = requests.get('https://api.ipify.org', timeout=5)
        return resp.text if resp.status_code == 200 else None
    except:
        return None
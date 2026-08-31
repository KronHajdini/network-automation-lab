# Network Automation & Enterprise Infrastructure Lab

This repository showcases production-ready Python automation scripts, Ansible playbooks, FortiGate security policies, Zero Trust (ZTNA) configurations, and technical design documentation (LLD/HLD).

---

## 1. Cisco Configuration Backup Script (Python)
**File:** `cisco_backup.py`  
Uses `Netmiko` to connect securely via SSH to Cisco switches/routers and save timestamped running configurations.

```python
import os
import datetime
from netmiko import ConnectHandler

devices = [
    {
        "device_type": "cisco_ios",
        "host": "192.168.1.1",
        "username": "admin",
        "password": "SecurePassword123!",
    }
]

BACKUP_DIR = "./backups"
os.makedirs(BACKUP_DIR, exist_ok=True)
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")

for device in devices:
    try:
        print(f"Connecting to {device['host']}...")
        net_connect = ConnectHandler(**device)
        net_connect.enable()
        output = net_connect.send_command("show running-config")
        
        filename = f"{BACKUP_DIR}/{device['host']}_config_{timestamp}.txt"
        with open(filename, "w") as backup_file:
            backup_file.write(output)
            
        print(f"[SUCCESS] Saved backup to {filename}")
        net_connect.disconnect()
    except Exception as e:
        print(f"[ERROR] Failed to backup {device['host']}: {e}")

# network-automation-lab
Enterprise network automation scripts, FortiGate security policies, ZTNA configuration, and LLD design documentation (Cisco &amp; FortiOS).

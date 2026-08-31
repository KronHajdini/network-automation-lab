import os
import datetime
from netmiko import ConnectHandler

# List of target network devices
devices = [
    {
        "device_type": "cisco_ios",
        "host": "192.168.1.1",
        "username": "admin",
        "password": "SecurePassword123!",
    },
    {
        "device_type": "cisco_ios",
        "host": "192.168.1.2",
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
        
        # Pull active configuration
        output = net_connect.send_command("show running-config")
        
        # Write to timestamped text file
        filename = f"{BACKUP_DIR}/{device['host']}_config_{timestamp}.txt"
        with open(filename, "w") as backup_file:
            backup_file.write(output)
            
        print(f"[SUCCESS] Saved backup to {filename}")
        net_connect.disconnect()
        
    except Exception as e:
        print(f"[ERROR] Failed to backup {device['host']}: {e}")

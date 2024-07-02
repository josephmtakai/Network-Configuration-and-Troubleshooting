# Network Configuration and Troubleshooting

This project includes scripts for automating network configuration backup, DNS management, and IP address management.

## Table of Contents

- [Configuration Backup (PowerShell)](#configuration-backup-powershell)
- [DNS Management (Python)](#dns-management-python)
- [IP Address Management (IPAM) (Python)](#ip-address-management-ipam-python)
- [Testing](#testing)

## Configuration Backup (PowerShell)

This script automates the backup of network device configurations (e.g., routers, switches).

### Script

```powershell
# PowerShell Script for Network Configuration Backup

# Define the list of network devices
$devices = @("192.168.1.1", "192.168.1.2")

# Define credentials for accessing network devices
$username = "admin"
$password = ConvertTo-SecureString "password" -AsPlainText -Force
$credential = New-Object System.Management.Automation.PSCredential($username, $password)

# Define the backup directory
$backupDir = "C:\NetworkBackups"

# Ensure the backup directory exists
if (-not (Test-Path $backupDir)) {
    New-Item -ItemType Directory -Path $backupDir
}

# Loop through each device and backup the configuration
foreach ($device in $devices) {
    # Define the backup file path
    $backupFile = Join-Path $backupDir "$($device)_config.txt"
    
    # Use SSH to connect to the device and retrieve the configuration
    $config = ssh $credential@$device 'show running-config'

    # Save the configuration to a file
    $config | Out-File -FilePath $backupFile
}

Usage
Save the script to a file named BackupNetworkConfig.ps1.
Open PowerShell as an administrator.
Navigate to the directory where the script is saved.

Execute the script:
powershell: .\BackupNetworkConfig.ps1
Verify the backup files in the specified directory (e.g., C:\NetworkBackups).
DNS Management (Python)
This script automates DNS record management tasks, such as adding or updating DNS records.

Script:
import dns.resolver
import dns.update
import dns.query

# Define the DNS server
dns_server = '192.168.1.100'

# Function to add a DNS record
def add_dns_record(zone, name, record_type, value):
    update = dns.update.Update(zone)
    update.add(name, 300, record_type, value)
    response = dns.query.tcp(update, dns_server)
    print(response)

# Function to update a DNS record
def update_dns_record(zone, name, record_type, value):
    update = dns.update.Update(zone)
    update.replace(name, 300, record_type, value)
    response = dns.query.tcp(update, dns_server)
    print(response)

# Example usage
zone = 'example.com'
add_dns_record(zone, 'test', 'A', '192.168.1.50')
update_dns_record(zone, 'test', 'A', '192.168.1.51')

Usage
Ensure you have dnspython installed:
sh
Copy code
pip install dnspython
Save the script to a file named dns_management.py.
Open a terminal or command prompt.
Navigate to the directory where the script is saved.
Execute the script:
sh
Copy code
python dns_management.py
Verify the DNS records on your DNS server.
IP Address Management (IPAM) (Python)
This script manages IP address allocations and maintains an IP address database.

Script:
import sqlite3

# Connect to the IPAM database (creates if not exists)
conn = sqlite3.connect('ipam.db')
c = conn.cursor()

# Create the IP addresses table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS ip_addresses
             (id INTEGER PRIMARY KEY, ip TEXT, allocated_to TEXT, status TEXT)''')

# Function to add an IP address
def add_ip_address(ip, allocated_to):
    c.execute("INSERT INTO ip_addresses (ip, allocated_to, status) VALUES (?, ?, ?)",
              (ip, allocated_to, 'allocated'))
    conn.commit()

# Function to release an IP address
def release_ip_address(ip):
    c.execute("UPDATE ip_addresses SET status = 'available', allocated_to = NULL WHERE ip = ?", (ip,))
    conn.commit()

# Function to get all IP addresses
def get_all_ip_addresses():
    c.execute("SELECT * FROM ip_addresses")
    return c.fetchall()

# Example usage
add_ip_address('192.168.1.100', 'Device1')
release_ip_address('192.168.1.100')
print(get_all_ip_addresses())

# Close the connection
conn.close()

Usage
Save the script to a file named ipam.py.
Open a terminal or command prompt.
Navigate to the directory where the script is saved.
Execute the script:

sh
Copy code
python ipam.py
Verify the IP address entries in the ipam.db SQLite database.
Testing
Follow these steps to test each script:

Configuration Backup (PowerShell):

Set up test network devices with valid credentials.
Save and run BackupNetworkConfig.ps1 as described in the usage section.
Verify the backup files in the specified directory.
DNS Management (Python):

Ensure dnspython is installed.
Save and run dns_management.py as described in the usage section.
Verify the DNS records on your DNS server.
IP Address Management (IPAM) (Python):

Ensure sqlite3 is available.
Save and run ipam.py as described in the usage section.
Verify the IP address entries in the ipam.db SQLite database.
Adjust the scripts and test environments as needed to match your specific network setup and requirements.


Save this content in a file named `README.md` in the root directory of your project. This will provide clear instructions for setting up, using, and testing each script in your Network Configuration and Troubleshooting program.

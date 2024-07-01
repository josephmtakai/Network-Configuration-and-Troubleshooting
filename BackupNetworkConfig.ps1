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

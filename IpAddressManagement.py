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

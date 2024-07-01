import dns.resolver
import dns.update
import dns.query
import dns.exception

# Define the DNS server
dns_server = '192.168.1.100'

# Function to add a DNS record
def add_dns_record(zone, name, record_type, value):
    try:
        update = dns.update.Update(zone)
        update.add(name, 300, record_type, value)
        response = dns.query.tcp(update, dns_server)
        print("Add record response:", response)
    except dns.exception.DNSException as e:
        print("Error adding DNS record:", e)

# Function to update a DNS record
def update_dns_record(zone, name, record_type, value):
    try:
        update = dns.update.Update(zone)
        update.replace(name, 300, record_type, value)
        response = dns.query.tcp(update, dns_server)
        print("Update record response:", response)
    except dns.exception.DNSException as e:
        print("Error updating DNS record:", e)

# Example usage
zone = 'example.com'
add_dns_record(zone, 'test', 'A', '192.168.1.50')
update_dns_record(zone, 'test', 'A', '192.168.1.51')

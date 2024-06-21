import os
import tabulate
from catalystwan.session import create_manager_session
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Get credentials from environment variables or prompt user
url = os.getenv("SDWAN_URL") or input("URL: ")
username = os.getenv("SDWAN_USERNAME") or input("Username: ")
password = os.getenv("SDWAN_PASSWORD") or input("Password: ")

with create_manager_session(url=url, username=username, password=password) as session:
    # Get tunnel health data
    for tunnel in session.api.dashboard.get_tunnel_health().data:
        print(
            f"Verifying {tunnel.name} Tunnel:\n"
            f"      - Tunnel State: {tunnel.state}\n"
            f"      - Tunnel Endpoints: local system {tunnel.local_system_ip}, remote system {tunnel.remote_system_ip}\n"
            f"      - Tunnel Metrics: Jitter {tunnel.jitter}, Latency {tunnel.latency}, Packet Loss {tunnel.loss_percentage}\n"
        )

    # Get all the devices in the SDWAN fabric
    devices = session.api.devices.get()

    # Build headers for the table
    headers = ["Device ID", "Hostname", "Model", "Site ID", "Status", "CPU Load", "Memory Usage"]
    table = list()

    # Parse devices and extract ID, hostname, model, site ID, status, CPU load and memory usage
    for device in devices:
        tr = [device.id, device.hostname, device.model, device.site_id, device.status, device.cpu_load, device.memUsage]
        table.append(tr)
    
    # Print table using tabulate
    try:
        print(tabulate.tabulate(table, headers, tablefmt="fancy_grid"))
    except UnicodeEncodeError:
        print(tabulate.tabulate(table, headers, tablefmt="grid"))
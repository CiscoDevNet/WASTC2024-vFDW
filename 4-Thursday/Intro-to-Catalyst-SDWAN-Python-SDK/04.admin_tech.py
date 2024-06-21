import os
from catalystwan.session import create_manager_session
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Get credentials from environment variables or prompt user
url = os.getenv("SDWAN_URL") or input("URL: ")
username = os.getenv("SDWAN_USERNAME") or input("Username: ")
password = os.getenv("SDWAN_PASSWORD") or input("Password: ")

with create_manager_session(url=url, username=username, password=password) as session:
    # Get the admin tech file for the Manager
    admin_tech_file = session.api.admin_tech.generate("10.10.1.1")
    session.api.admin_tech.download(admin_tech_file)
    session.api.admin_tech.delete(admin_tech_file)
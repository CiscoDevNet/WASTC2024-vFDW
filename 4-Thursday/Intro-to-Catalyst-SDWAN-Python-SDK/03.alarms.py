import os
from catalystwan.utils.alarm_status import Severity
from catalystwan.session import create_manager_session
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Get credentials from environment variables or prompt user
url = os.getenv("SDWAN_URL") or input("URL: ")
username = os.getenv("SDWAN_USERNAME") or input("Username: ")
password = os.getenv("SDWAN_PASSWORD") or input("Password: ")

with create_manager_session(url=url, username=username, password=password) as session:
    # Get a all the alarms in the fabric
    alarms = session.api.alarms.get()
    print(alarms)

    # Get non-viewed alarms
    #not_viewed_alarms = session.api.alarms.get().filter(viewed=False)

    # Get critical alarms from the last 48 hours
    #n = 48
    #critical_alarms = session.api.alarms.get(from_time=n).filter(severity=Severity.CRITICAL)
    #print(critical_alarms)
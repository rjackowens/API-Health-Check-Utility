import requests
import urllib3

#Disables insecure certificate errors
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

master = {
    "environment" : {
        1: "https://DEV-01:443/",
        2: "https://DEV-02:443/",
        3: "https://QA-01:443/",
        4: "https://QA-02:443/",
        5: "https://PROD-01:443/",
        6: "https://PROD-02:443/",
        },
    "service" : {
        1: "AuthenticationService",
        2: "CalendarService",
        3: "CollectionService",
        4: "CustomerService",
        5: "DistributionService",
        6: "EquipmentService",
        7: "EventService",
        8: "FieldService",
        9: "FileService",
        10: "LaunchService",
        11: "OrderingService",
        12: "PartListingService",
        13: "ReportService",
        14: "UnderwriterService",
        15: "UserService"
        },
    "endpoint" : {
        "Version": "/api/Version?api-version=1.0",
        "Health": "/health"
        }
    }

def getStatus(x):
    status = requests.get(x, verify=False)
    return status.status_code

def getHealth(y):
    status = getStatus(y)
    if status is 200:
        print(y + " is healthy")
    else:
        print(y + " is NOT healthy. Response is " + str(status))

for service in master["service"].values():
    for environment in master["environment"].values():
        URL = []
        URL.append(environment + service + master["endpoint"]["Health"])
        getHealth(''.join(URL))

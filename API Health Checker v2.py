import requests
import urllib3
import Dictionary

#Disables insecure certificate errors
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def getStatus(x):
    status = requests.get(x, verify=False)
    return status.status_code

def getHealth(y):
    status = getStatus(y)
    if status is 200:
        print(y + " is healthy")
    else:
        print(y + " is NOT healthy. Response is " + str(status))

for keys, values in Dictionary.master["service"].items():
        print(keys, values)

selection = int(input("\nSelect Service: "))

def selectEndpoint(x):
    return {
        1: "authentication",
        2: "commissions",
        3: "configuration",
        4: "customer",
        5: "distributor",
        6: "equipment",
        7: "event", #nonexistent
        8: "fieldrep",
        9: "filehandler",
        10: "launchpad",
        11: "order", #nonexistent
        12: "parts",
        13: "reporting",
        14: "underwriting", #nonexistent
        15: "user"
        }[x]

selectedEndpoint = str(selectEndpoint(selection))

if selection == 7 or selection == 11 or selection == 14: 
        print ("\nNo API endpoints currently exist for this service ")
        exit()

for environment in Dictionary.master["environment"].values(): #All Environments
        for endpoint in Dictionary.master[selectedEndpoint].values(): #Selected Endpoint
                URL = []
                URL.append(environment + Dictionary.master["service"][selection] + endpoint)
                getHealth(''.join(URL))

import socket
import requests
import urllib3
from flask import Flask

app = Flask(__name__)

#Disables insecure certificate errors
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def getStatus(x):
    status = requests.get(x, verify=False)
    return status.status_code

def getHealth(y):
    status = getStatus(y)
    if status is 200:
        return ("Healthy")
    else:
        return (y + " is NOT healthy. Response is " + str(status))
        
@app.route("/health")
def health():
    return getHealth("https://google.com/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

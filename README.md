# API-Health-Check-Utility
This tool quickly checks for HTTP 200 response codes of API endpoints across environments. 

**Configuration**

Replace the values of `environment` `service` and `endpoint` in the master dictionary.

**Usage**
After updating the dictionary, simply run the script to see the response status of your selected API endpoints. The script iterates first by service name and then by environment. By default, only a single API endpoint filter runs at a time. You can easily update this value by replacing `master["endpoint"]["Health"])` with `master["endpoint"]["{VALUE}"])`.

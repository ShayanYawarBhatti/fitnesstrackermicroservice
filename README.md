# Microservice A – Workout Logger

## How to Request Data

Send a POST request to `/log_workout` with:
```json
{
  "name": "Jogging",
  "date": "08/04/2025",
  "duration": 30
}
Example:
import requests
data = {"name": "Jogging", "date": "08/04/2025", "duration": 30}
requests.post("http://localhost:5000/log_workout", json=data)

How to Receive Data
Send a GET request to /weekly_workouts.

Example:
import requests
r = requests.get("http://localhost:5000/weekly_workouts")
print(r.json())


Mitigation Plan:
A. Teammate:** Rylie Shaniyo  
B. Status:** Microservice complete  
C. Not done?:** N/A  
D. Access:** Clone my repo and run `python microservice_a.py` locally  
E. Can’t access?** Message me via Discord or email before Aug 5  
F. Report issues by:** Aug 5, 11:59 PM  
G. Notes:**
- Make sure Python and Flask are installed  
- Data is stored in-memory  
- No database yet  
- All requests are JSON-based

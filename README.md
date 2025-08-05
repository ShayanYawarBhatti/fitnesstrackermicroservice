# Microservice A – Workout Logger
## Communication Contract
This document outlines how another program(the main program) can communicate with the microservice.The contract is stable and can be relied upon for integration

## How to Request Data
Send a POST request to `/log_workout` with:
{
  "name": "Jogging",
  "date": "08/04/2025",
  "duration": 30
}

Example:
import requests
data = {"name": "Jogging", "date": "08/04/2025", "duration": 30}
requests.post("http://localhost:5000/log_workout", json=data)


## How to Receive Data
Send a GET request to /weekly_workouts.

Example:
import requests
r = requests.get("http://localhost:5000/weekly_workouts")
print(r.json())




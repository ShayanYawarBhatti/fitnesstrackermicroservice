import requests
from datetime import datetime

# Log a workout
print("Logging a workout...")
r1 = requests.post("http://localhost:5000/log_workout", json={
    "name": "Jogging",
    "date": datetime.now().strftime("%m/%d/%Y"),
    "duration": 30
})
print("Log response:", r1.json())

# Get workouts this week
print("Getting weekly workouts...")
r2 = requests.get("http://localhost:5000/weekly_workouts")
print("Weekly workouts:", r2.json())

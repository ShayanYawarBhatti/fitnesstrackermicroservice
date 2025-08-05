from flask import Flask, request, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)
workouts = []

@app.route('/log_workout', methods=['POST'])
def log_workout():
    data = request.get_json()
    name = data.get("name")
    date_str = data.get("date")
    duration = data.get("duration")

    if not name or not date_str or not duration:
        return jsonify({"error": "Missing name, date, or duration"}), 400
    try:
        datetime.strptime(date_str, "%m/%d/%Y")
        duration = int(duration)
    except:
        return jsonify({"error": "Invalid date or duration"}), 400

    workouts.append({
        "name": name,
        "date": date_str,
        "duration": duration
    })
    return jsonify({"message": "Workout logged"}), 200

@app.route('/weekly_workouts', methods=['GET'])
def weekly_workouts():
    now = datetime.now()
    start_of_week = now - timedelta(days=now.weekday())
    this_week = [
        w for w in workouts
        if datetime.strptime(w["date"], "%m/%d/%Y") >= start_of_week
    ]
    return jsonify(this_week), 200

if __name__ == '__main__':
    app.run(debug=True)

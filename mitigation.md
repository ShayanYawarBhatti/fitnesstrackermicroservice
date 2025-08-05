
# 🛡️ Mitigation Plan – Fitness Tracker Microservice
This document outlines how to respond if the microservice fails or behaves unexpectedly.

---

## 1. ❌ Cannot Access the Microservice

**Check:**
- Ensure Python and Flask are installed
- Confirm `python microservice_a.py` is running
- Verify it's accessible at `http://127.0.0.1:5000`

**Fix:**
- Restart the server
- Check terminal for error messages
- Try on another local machine

---

## 2. 🐞 If `/log_workout` or `/weekly_workouts` Fails

**Symptoms:**
- HTTP 400 Bad Request
- Empty or unexpected JSON

**Steps:**
- Double-check the request format (especially `MM/DD/YYYY`)
- Use a tool like Postman or Curl to test
- Review server logs for traceback

---

## 3. 📢 Reporting the Issue

Please share:
- OS + Python version
- Error message or stack trace
- The exact request body you used
- A screenshot if possible

---

## 4. 🔁 Resetting the Microservice

Since this microservice uses in-memory storage (a list), restarting it clears the data.

To restart:
```bash
CTRL+C  # to stop
python microservice_a.py  # to start again

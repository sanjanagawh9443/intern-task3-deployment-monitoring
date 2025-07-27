import random
import time

def check_uptime():
    status = random.choice(["UP", "DOWN"])
    response_time = round(random.uniform(0.1, 1.5), 2)
    print(f"🌐 STATUS: {status} | Response Time: {response_time}s")
    if status == "DOWN":
        print("🔴 ALERT: System is currently DOWN!")
    else:
        print("🟢 All systems operational.")

# Run the function
check_uptime()


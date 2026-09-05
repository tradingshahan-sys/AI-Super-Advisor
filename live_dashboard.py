import time
import json
import os
import datetime

class LiveDashboard:
    def __init__(self, memory_file="omni_memory.json"):
        self.memory_file = memory_file
        self.status = "24/7 Live Monitoring Active"

    def fetch_latest_intelligence(self):
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    return data.get("global_database", [])
            except Exception:
                return []
        return [{"Status": "Waiting for data streams..."}]

    def render_continuous_display(self):
        print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] === OMNI-ADVISOR 24/7 LIVE DASHBOARD ===")
        while True:
            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            insights = self.fetch_latest_intelligence()
            
            print(f"\n[{timestamp}] --- Active Data Stream ---")
            for item in insights[-5:]: # Shows the last 5 critical items captured
                print(f" -> {item}")
            
            # Refresh interval for continuous 24/7 monitoring
            time.sleep(10)

if __name__ == "__main__":
    dashboard = LiveDashboard()
    dashboard.render_continuous_display()

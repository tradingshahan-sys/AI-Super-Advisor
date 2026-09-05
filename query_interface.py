import json
import os

class OmniQueryInterface:
    def __init__(self, memory_file="omni_memory.json"):
        self.memory_file = memory_file

    def analyze_and_categorize_memory(self, filter_keyword=None):
        if not os.path.exists(self.memory_file):
            print("[Query Engine]: No database or memory file detected yet.")
            return

        with open(self.memory_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            records = data.get("global_database", [])

        print(f"\n[Omni Query Engine]: Total stored records -> {len(records)}")
        print("--------------------------------------------------")
        
        categories = {}
        for idx, item in enumerate(records, 1):
            for key, value in item.items():
                if filter_keyword and filter_keyword.lower() not in key.lower() and filter_keyword.lower() not in str(value).lower():
                    continue
                print(f"[{idx}] Category/Key: {key}")
                print(f"     Content: {value}\n")

if __name__ == "__main__":
    interface = OmniQueryInterface()
    print("=== INTELLIGENCE QUERY SYSTEM ACTIVE ===")
    interface.analyze_and_categorize_memory()

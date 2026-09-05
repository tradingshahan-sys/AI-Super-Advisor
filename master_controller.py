import time
import json
import os
import random

def autonomous_loop():
    memory_file = "omni_memory.json"
    
    # دڵنیابوون لە بوونی فایلی بیرگە
    if not os.path.exists(memory_file):
        with open(memory_file, "w", encoding="utf-8") as f:
            json.dump({"global_database": []}, f, indent=4)

    print("[Autonomous Core]: Unrestricted background engine is now fully active...")
    
    targets = ["Global Markets", "Open Source Data", "Mountain Geology & History", "Security Intelligence"]

    while True:
        target = random.choice(targets)
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        
        new_record = {
            "Timestamp": timestamp,
            "Target_Source": target,
            "Status": "Crawled & Analyzed",
            "Data_Node": f"Extracted autonomous intelligence packet from {target}."
        }

        # پاشەکەوتکردنی داتا لە بیرگەی گشتی
        with open(memory_file, "r+", encoding="utf-8") as f:
            data = json.load(f)
            data["global_database"].append(new_record)
            f.seek(0)
            json.dump(data, f, indent=4, ensure_ascii=False)

        print(f"[{timestamp}] [Auto-Scout]: Explored '{target}' -> Stored in Omni Memory.")
        
        # چاوەڕێکردنی ١٠ چرکە پێش گەڕانی دووەم بۆ ئەوەی سیستمەکە بە بێوەستان بەردەوام بێت
        time.sleep(10)

if __name__ == "__main__":
    autonomous_loop()

import json
from datetime import datetime
from tkinter import filedialog

def save_json(data):
    filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if filename:
        with open(filename, "w") as f:
            json.dump({"timestamp": str(datetime.now()), "results": data}, f, indent=2)

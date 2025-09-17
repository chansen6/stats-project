import csv
import os
from datetime import datetime

def print_stats(stats):
    print("\n--- Stats Report ---")
    for key, value in stats.items():
        if isinstance(value, float):
            value = round(value, 2)
        print(f"{key}: {value}")

def export_stats(stats, folder="data"):
    # Make sure folder exists
    os.makedirs(folder, exist_ok=True)

    # Create timestamped filename (YYYY-MM-DD_HH-MM-SS)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{folder}/stats_{timestamp}.csv"

    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Metric", "Value"])
        for key, value in stats.items():
            if isinstance(value, float):
                value = round(value, 2)
            writer.writerow([key, value])

    print(f"\nReport saved to {filename}")
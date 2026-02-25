import psutil

print("=== Running Processes ===\n")

for process in psutil.process_iter(['pid', 'name']):
    print(f"PID: {process.info['pid']} | Name: {process.info['name']}")

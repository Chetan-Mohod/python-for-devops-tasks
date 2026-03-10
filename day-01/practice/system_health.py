import psutil

def get_threshold():
    cpu_threshold = int(input("Enter current CPU threshold:"))
    disk_threshold = int(input("Enter current disk threshold:"))
    memory_threshold = int(input("Enter current memory threshold:"))
    
    current_cpu = psutil.cpu_percent(interval=1)
    current_disk = psutil.disk_usage('/').percent
    current_memory = psutil.virtual_memory().percent
    print("-----System Metrics----")
    print("Current CPU (%):",current_cpu)
    print("Current disk usage (%):",current_disk)
    print("Current Memory (%):",current_memory)
    print("-----------------------")

    if current_cpu > cpu_threshold:
        print("CPU Alert Email sent...")
    if current_disk > disk_threshold:
        print("Disk Usage Alert Email sent...")
    if current_memory > memory_threshold:
        print("Memory Alert: Threshold exceeded!")
    if current_cpu <= cpu_threshold and current_disk <= disk_threshold and current_memory <= memory_threshold:
        print("Everything is in safe state")

get_threshold()

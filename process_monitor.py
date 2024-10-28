import psutil
import time

def show_processes():
    """
    Shows basic information about running processes.
    """
    while True:
        # Clear the terminal screen
        print("\033c", end="")
        
        print("=== Process Monitor ===")
        print(f"Total CPU Usage: {psutil.cpu_percent()}%")
        print(f"Memory Usage: {psutil.virtual_memory().percent}%")
        print("\nTop 5 Processes:")
        print("-" * 50)
        print("ID    | Name                | CPU%")
        print("-" * 50)
        
        # Get all processes and their CPU usage
        processes = []
        for proc in psutil.process_iter():
            try:
                # Get basic info
                pid = proc.pid
                name = proc.name()[:15]  # Trim long names
                cpu = proc.cpu_percent()
                
                # Only add if we got valid CPU usage
                if cpu is not None and cpu > 0:
                    processes.append({
                        'pid': pid,
                        'name': name,
                        'cpu': cpu
                    })
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        
        # Sort by CPU usage and show top 5
        processes.sort(key=lambda x: x['cpu'], reverse=True)
        for proc in processes[:5]:
            print(f"{proc['pid']:<6}| {proc['name']:<19}| {proc['cpu']:>4.1f}%")
        
        # Letting CPU values accumulate / this is a sleep buffer
        time.sleep(2)

# Running the system
try:
    show_processes()
except KeyboardInterrupt:
    print("\nMonitor stopped!")
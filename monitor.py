import psutil
import time
def get_cpu_usage():
    cpu = psutil.cpu_percent(interval=1)
    return cpu


def get_memory_usage():
 memory = psutil.virtual_memory()
 return memory.percent


def get_disk_usage():
    disk = psutil.disk_usage("C:\\")
    return disk.percent
def check_alerts(cpu, memory, disk):
   print("\n===== SYSTEM ALERTS =====")
   if cpu >= 80:
         print("WARNING: CPU USAGE IS HIGH!")
   else:
         print("CPU usage is normal.")
   if memory >= 80:
            print("WARNING: MEMORY USAGE IS HIGH!")
   else:
            print("Memory usage is normal.")
   if disk >= 90:
               print("WARNING: LOW DISK SPACE!")
   else:
               print("Disk space is sufficient.")

def get_processes():
 running_processes =list(psutil.process_iter())[:10]  # Limit to first 10 processes
 process_info =[]
 for process in running_processes:
    try:
        process.cpu_percent()
    except(psutil.NoSuchProcess,psutil.AccessDenied):pass
    time.sleep(1)
 for process in running_processes:
    try:
        cpu_usage = round(process.cpu_percent(),2)
        memory_usage = round(process.memory_percent(),3)
        process_info.append({"PID": process.pid,
                             "Name": process.name(),
                             "CPU Usage": cpu_usage,
                             "Memory Usage": memory_usage})   
    except(psutil.NoSuchProcess,psutil.AccessDenied):pass
 return process_info
 

def main():
   cpu = get_cpu_usage()
   memory = get_memory_usage()
   disk = get_disk_usage()
   system_info = {
      "CPU Usage": cpu,
      "Memory Usage": memory,
      "Disk Usage": disk
   }
   check_alerts(cpu, memory, disk)
   processes = get_processes()
   print("\n===== TOP 10 PROCESSES =====")
   print(f"{'PID':<10}{'Process Name':<25}{'CPU Usage (%)':<10}{'Memory Usage (%)':<10}")
   print("-" * 60)
   for process in processes:
      print(
         f"{process['PID']:<10}"
        f"{process['Name']:<25}"
        f"{process['CPU Usage']:<10}"
        f"{process['Memory Usage']:<10}"
      )
   return system_info
system_info =main()  
print("\n===== SYSTEM MONITOR =====")
print(f"CPU Usage: {system_info['CPU Usage']:.2f}%")
print(f"Memory Usage: {system_info['Memory Usage']:.2f}%")
print(f"Disk Usage: {system_info['Disk Usage']:.2f}%")

import psutil
import time
def get_cpu_usage():
    cpu = psutil.cpu_percent()
    return cpu


def get_memory_usage():
 memory = psutil.virtual_memory()
 return memory.percent


def get_disk_usage():
    disk = psutil.disk_usage("C:\\")
    return disk.percent

def get_processes():
 running_processes = psutil.process_iter()

 for process in running_processes:
    cpu_usage = process.cpu_percent(interval=1)
    memory_usage = process.memory_percent()

    print("PID:",process.pid,"Process:",process.name(),"CPU:",cpu_usage,"%","Memory:",memory_usage,"%")
 

def main():
   cpu = get_cpu_usage()
   memory = get_memory_usage()
   disk = get_disk_usage()
   print("CPU Usage:", cpu, "%")
   print("Memory Usage:", memory, "%")
   print("Disk Usage:", disk, "%")
   get_processes()
main()   
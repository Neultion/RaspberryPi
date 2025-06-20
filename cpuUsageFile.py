import psutil
from time import sleep
from datetime import datetime
file  = open("/home/thlinh04/sourchProject/Demo/cpu_usage_log.txt",'w')
temp = 1
while True:
    if temp > 10: break
    cpu_usage = psutil.cpu_percent(interval = 1, percpu = True)
    cpu_usage_mean = sum([i/len(cpu_usage) for i in cpu_usage])
    cpu_usage_mean = round(cpu_usage_mean, 3)
    print(f"cpu usage(%) : {cpu_usage_mean}%")
    data = f"Line {temp} : {datetime.now().strftime('%Y/%m/%d %HH %MM %SS')} \t cpu usage(%) : {cpu_usage_mean}% \n"
    file.write(data)
    sleep(1)
    temp+=1
file.close()
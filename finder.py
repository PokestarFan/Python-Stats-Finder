'''
Python Stats Finder
Made by PokestarFan
Start Date: 6/23/2017
Lisence: GNU General Public Lisence
'''

# All of the imports go here
import os #for  writing the file, no shady business
import datetime #dated files
import psutil #collecting stats
import time #wait


#Definitions
def get_used_ram(): #get the used ram in system
    used_ram=round(psutil.virtual_memory().used /(1024 ** 3),2)
    return used_ram

def get_free_ram(): #get the free ram in system
    free_ram=round(psutil.virtual_memory().available /(1024 ** 3),2)
    return free_ram

def get_percent_ram(): #get the percent ram in system
    percent_ram=psutil.virtual_memory().percent
    return percent_ram

def get_cpu_percent(): #get the cpu percent_ram
    percent_cpu=psutil.cpu_percent(interval=1)
    return percent_cpu

def create_dir(): #create monthly/yearly directories
    year_exists=os.path.isdir((str(datetime.datetime.now().year)))
    if year_exists:
        os.chdir(str(datetime.datetime.now().year))
    else:
        os.mkdir(str(datetime.datetime.now().year))
        os.chdir(str(datetime.datetime.now().year))
    month_exists=os.path.isdir((str(datetime.datetime.now().month)))
    if month_exists:
        os.chdir(str(datetime.datetime.now().month))
    else:
        os.mkdir(str(datetime.datetime.now().month))
        os.chdir(str(datetime.datetime.now().month))

def write_results(timestamp):
    used_ram=get_used_ram()
    free_ram=get_free_ram()
    percent_ram=get_percent_ram()
    percent_cpu=get_cpu_percent()
    towrite=str("\n")+str(timestamp)+str(",")+str(percent_cpu)+str(",")+str(used_ram)+str(",")+str(free_ram)+str(",")+str(percent_ram)
    opening_text=str("Timestamp, CPU (%), USed RAM (GB), Free Ram (GB), Percent of RAM Used")
    today_file=open(str(datetime.datetime.now().day)+".csv", 'a+')
    if os.stat(str(datetime.datetime.now().day)+".csv").st_size == 0:
        today_file.write(opening_text)
        today_file.write(str(towrite))
    else:
        today_file.write(str(towrite))


#actual execution
create_dir()
times_executed=0
while True:
    times_executed=1+times_executed
    timestamp=time.strftime("%H:%M:%S")
    write_results(timestamp)
    print("Executed "+str(times_executed)+" times today")
    time.sleep(300)

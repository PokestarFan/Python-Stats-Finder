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

def get_percent_ram(): #get the free ram in system
    percent_ram=psutil.virtual_memory().percent
    return percent_ram

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
    towrite=str("\n")+str(timestamp)+str(,)+str(used_ram)+str(,)+str(free_ram)+str(,)+str(percent_ram)
    if os.stat(str(datetime.datetime.now().day).csv).st_size == 0:
        today_file=open(str(datetime.datetime.now().day).csv, 'w') as file
        today_file.write("timestamp, usedram, freeram, rampercentused")
        today_file.write(str(towrite))
        today_file.close()
    elif os.stat(str(datetime.datetime.now().day).csv).st_size < :
        today_file=open(str(datetime.datetime.now().day).csv, 'w') as file
        today_file.truncate()
        today_file.close()
        write_results()
    else:
        today_file=open(str(datetime.datetime.now().day).csv, 'w') as file
        today_file.write(str(towrite)))
        today_file.close()


#actual execution
create_dir()
while True:
    timestamp=time.strftime("%H:%M:%S")
    write_results(timestamp)
    time.sleep(300)

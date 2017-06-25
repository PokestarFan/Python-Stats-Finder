'''
Python Stats Finder
Made by PokestarFan
Start Date: 6/23/2017
Lisence: GNU General Public Lisence
'''

# All of the imports go here
import os #for  writing the file, no shady business
import datetime
import psutil


#Definitions
def get_used_ram(used_ram):
    used_ram=round(psutil.virtual_memory().used /(1024 ** 3),2)
    return used_ram

def get_free_ram(free_ram):
    free_ram=round(psutil.virtual_memory().available /(1024 ** 3),2)
    return free_ram

def get_ram():
    get_free_ram()
    get_used_ram()

def create_dir(year_exists, month_exists):
    if year_exists==true:
        os.chdir(str(datetime.datetime.now().year))
    else:
        os.mkdir(str(datetime.datetime.now().year))
        os.chdir(str(datetime.datetime.now().year))
    if month_exists==true:
        os.chdir(str(datetime.datetime.now().month))
    else:
        os.mkdir(str(datetime.datetime.now().month))
        os.chdir(str(datetime.datetime.now().month))

def write_results():
    open('workfile', 'w')


#actual execution
year_exists=os.path.isdir((str(datetime.datetime.now().year)))
month_exists=os.path.isdir((str(datetime.datetime.now().year)+'\\'+(str(datetime.datetime.now().month)))
create_dir(year_exists, month_exists)

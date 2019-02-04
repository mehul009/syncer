import shutil as shu         # librery for the copy file
import pandas as pd
import os
import time 
from numpy import array
from termcolor import *
import colorama
colorama.init()


t_start = time.time()
#function for copy file 
def copy(path,folder,cp_dir= False) :
    list_object = os.listdir(str(path))       
    list_file = []
     
    for object in list_object :
        try :              # to saprate out dir and file 
            os.chdir(str(path) +'\\' + str(object))
        except NotADirectoryError :
            list_file.append(object)
            
    for file1 in list_file :
        list_object.remove(file1)
        
    if cp_dir == True :
        list_dir = list_object
        if len(list_dir) > 0 :
            for dir in list_dir :               # if folder contain folder than chek recursively 
                copy(str(path) + str(dir) + '\\', str(folder) + '\\' + str(dir) + '\\',cp_dir=True)
        
        
    if not os.path.exists(drive_home + '\\' + folder):  # making directory if not present
        os.makedirs(drive_home + '\\' + folder)
        
    drive_folder = str(drive_home)  + '\\' + folder
    os.chdir(drive_folder)
    
    list_object_drive_folder = os.listdir(str(drive_folder))
    list_file_new = []
    
    for file_drive in list_object_drive_folder :
        try :
            list_file.remove(file_drive)
        except ValueError :
            pass
            
    list_file_new = list_file
                
    if len(list_object_drive_folder) == 0:
        list_file_new = list_file

    
    for new_file in list_file_new :
        t1 = time.time()
        size = os.path.getsize(path + str(new_file))
        total_size.append(size)
        print(path + str(new_file) + ' \nsize = ' + '{:.2f}'.format(size/10**6) + ' Mb ')
        shu.copy(path + str(new_file) , drive_folder)
        t2 = time.time()
        t = t2-t1
        mbps = size/(t* 10**6)
        print('with '+ '{:.2f}'.format(mbps) + ' Mbps' + '\n')


#file opration  
drive_home = os.getcwd()       # home dir of drive

file = pd.read_csv('shutil.csv')   # read file shutil.csv

total_size = []


#copy with directory
i = 0
k = 0

dr = colored('copy started for drive "D"','red')
print(dr)
for drive in ['D']:
    while k<len(file[str(drive)]):
        try:                 # exception if column value is more than dataframe
            folder = file.at[k, str(drive)]
        except KeyError:
            break
    
        folder = file.at[k, str(drive)]         # get data from file
        folder_path = str(drive) + ":" + str(folder) + "\\"  
        
        if str(folder)=='nan':
            break
    
        try:                 # exception if column value is nan
            list_object = os.listdir(str(folder_path))       
        except FileNotFoundError:
            wrng = colored('"' + str(folder_path)+'" is not there','red','on_yellow')
            print('\n' + wrng + '\n')
            k =k + 1
            continue 
    
        copy(folder_path,folder,cp_dir=True)
    
        os.chdir(drive_home)
    
        k = k + 1


    
total_file = len(total_size)
size = array(total_size)
t_size = size.sum()

t_end = time.time()
FILE = colored('\nTotal ' + str(total_file) + ' file copied on disk \n','green')
SIZE = colored('Total size  ' + '{:.2f}'.format(t_size/10**6) + ' Mb \n','green') 
TIME = colored('Total time ' + '{:.2f}'.format(t_end-t_start)+ ' sec \n','green')
SPEED = colored('Avrage speed ' + '{:.2f}'.format(t_size/((t_end-t_start)*(10**6))) + ' Mbps','green')
print( FILE + SIZE + TIME + SPEED)

i = 0
k = 0

dr = colored('copy started for drive "E"','red')
print(dr)
for drive in ['E']:
    while k<len(file[str(drive)]):
        try:                 # exception if column value is more than dataframe
            folder = file.at[k, str(drive)]
        except KeyError:
            break
    
        folder = file.at[k, str(drive)]         # get data from file
        folder_path = str(drive) + ":" + str(folder) + "\\"  
        
        if str(folder)=='nan':
            break
    
        try:                 # exception if column value is nan
            list_object = os.listdir(str(folder_path))       
        except FileNotFoundError:
            wrng = colored('"' + str(folder_path)+'" is not there','red','on_yellow')
            print('\n' + wrng + '\n')
            k =k + 1
            continue 
    
        copy(folder_path,folder,cp_dir=True)
    
        os.chdir(drive_home)
    
        k = k + 1


    
total_file = len(total_size)
size = array(total_size)
t_size = size.sum()

t_end = time.time()
FILE = colored('\nTotal ' + str(total_file) + ' file copied on disk \n','green')
SIZE = colored('Total size  ' + '{:.2f}'.format(t_size/10**6) + ' Mb \n','green') 
TIME = colored('Total time ' + '{:.2f}'.format(t_end-t_start)+ ' sec \n','green')
SPEED = colored('Avrage speed ' + '{:.2f}'.format(t_size/((t_end-t_start)*(10**6))) + ' Mbps','green')
print( FILE + SIZE + TIME + SPEED)
input()

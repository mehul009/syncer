import shutil as shu         # librery for the copy file
import pandas as pd
import os
import time 
from numpy import array


t_start = time.time()
#function for copy file 
def copy(path,folder,cp_dir= False) :
    list_object = os.listdir(str(path))       
    list_file = []
     
    for object in list_object :
        try :              # to saprate out dir and file 
            os.chdir(str(path) +'/' + str(object))
        except NotADirectoryError :
            list_file.append(object)
            
    for file1 in list_file :
        list_object.remove(file1)
        
    if cp_dir == True :
        list_dir = list_object
        if len(list_dir) > 0 :
            for dir in list_dir :               # if folder contain folder than chek recursively 
                copy(str(path) + str(dir) + '/', str(folder) + '/' + str(dir) + '/',cp_dir=True)
        
        
    if not os.path.exists(drive_home + '/' + folder):  # making directory if not present
        os.makedirs(drive_home + '/' + folder)
        
    drive_folder = str(drive_home)  + '/' + folder
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
        print(path + str(new_file) + ' size = ' + '{:.2f}'.format(size/10**6) + ' Mb \n')
        shu.copy(path + str(new_file) , drive_folder)
        t2 = time.time()
        t = t2-t1
        mbps = size/(t* 10**6)
        print('with '+ '{:.2f}'.format(mbps) + ' Mbps' + '\n')
        
        
        
#file opration        
os.chdir('/home/mehul09/copy/')     # for cheking purpose only  
drive_home = os.getcwd()       # home dir of drive

file = pd.read_csv('shutil.csv')   # read file shutil.csv

total_size = []



# only file copy system
i = 0
k = 0
while k<len(file['only_file']) :
    try:                 # exception if column value is more than dataframe
        folder = file.at[k, 'only_file']
    except KeyError:
        break
    
    folder = file.at[k, 'only_file']         # get data from file
    folder_path = '/home/mehul09/' + str(folder) + '/'   # /home/mehul09 is home folder
    
    if str(folder)=='nan':
        break
    
    
    try:                 # exception if column value is nan
        list_object = os.listdir(str(folder_path))       
    except FileNotFoundError:
        print(str(folder_path)+'is not there ')
        k = k + 1
        continue
    
    copy(folder_path,folder)
    os.chdir(drive_home)
    
    k = k + 1

#copy with directory
i = 0
k = 0

while k<len(file['with_dir']):
    try:                 # exception if column value is more than dataframe
        folder = file.at[k, 'with_dir']
    except KeyError:
        break
    
    folder = file.at[k, 'with_dir']         # get data from file
    folder_path = '/home/mehul09/' + str(folder) + '/'   # /home/mehul09 is home folder
    
    if str(folder)=='nan':
        break
    
    try:                 # exception if column value is nan
        list_object = os.listdir(str(folder_path))       
    except FileNotFoundError:
        print(str(folder_path)+' is not there \n\n')
        k =k + 1
        continue 
    
    copy(folder_path,folder,cp_dir=True)
    
    os.chdir(drive_home)
    
    k = k + 1
    
    
total_file = len(total_size)
size = array(total_size)
t_size = size.sum()

t_end = time.time()
print('\nTotal ' + str(total_file) + ' file copied on disk \n' + 'Total size  ' + '{:.2f}'.format(t_size/10**6) + ' Mb' + ' \nTotal time ' + '{:.2f}'.format(t_end-t_start)+ ' sec' + '\nAvrage speed ' + '{:.2f}'.format(t_size/((t_end-t_start)*(10**6))) + ' Mbps')

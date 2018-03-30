import shutil as shu         # librery for the copy file
import pandas as pd
import os

home = '/home/mehul09/'    # must have to change
drive_home = os.getcwd()       # home dir of drive

file = pd.read_csv('shutil.csv')   # read file shutil.csv

i = 0
k = 0

while i == 0:
    try:                 # exception if column value is more than dataframe
        folder = file.at[k, 'only_file']
    except KeyError:
        break
    
    folder = file.at[k, 'only_file']         # get data from file
    folder_path = home + str(folder) + '/'   # /home/mehul09 is home folder
    
    try:                 # exception if column value is nan
        list_object = os.listdir(str(folder_path))       
    except FileNotFoundError:
        break
    
    list_object = os.listdir(str(folder_path))    # list all object on path   
    list_file = []
     
    for object in list_object :
        try :              # to saprate out dir and file 
            os.chdir(str(folder_path) + object)
        except NotADirectoryError :
            list_file.append(object)
            
    for file1 in list_file :
        list_object.remove(file1)
        
    list_dir = list_object
        
        
    if not os.path.exists(drive_home + '/' + folder):  # making directory if not present
        os.makedirs(drive_home + '/' + folder)
        
    drive_folder = str(drive_home)  + '/' + folder
    os.chdir(drive_folder)
    
    list_object_drive_folder = os.listdir(str(drive_folder))
    list_file_new = []
    
    for file_drive in list_object_drive_folder :
        try :                                # find a new file 
            list_file.remove(file_drive)
        except ValueError :
            pass
            
    list_file_new = list_file
                
    if len(list_object_drive_folder) == 0:
        list_file_new = list_file

    
    for new_file in list_file_new :            # copy those new file
        print(folder_path + new_file)
        shu.copy(folder_path + str(new_file) , drive_folder)
        
    
    os.chdir(drive_home)
    
    k = k + 1
                
    
def copy_dir (path,folder) :
    list_object = os.listdir(str(path))       
    list_file = []
     
    for object in list_object :
        try :              # to saprate out dir and file 
            os.chdir(str(path) +'/' + str(object))
        except NotADirectoryError :
            list_file.append(object)
            
    for file1 in list_file :
        list_object.remove(file1)
        
    list_dir = list_object
    if len(list_dir) > 0 :
        for dir in list_dir :               # if folder contain folder than chek recursively 
            copy_dir(str(path) + str(dir) + '/', str(folder) + '/' + str(dir) + '/')
        
        
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
        print(path + str(new_file))
        shu.copy(path + str(new_file) , drive_folder)
        
        
i = 0
k = 0

while i == 0:
    try:                 # exception if column value is more than dataframe
        folder = file.at[k, 'with_dir']
    except KeyError:
        break
    
    folder = file.at[k, 'with_dir']         # get data from file
    folder_path = home + str(folder) + '/'   # /home/mehul09 is home folder
    
    try:                 # exception if column value is nan
        list_object = os.listdir(str(folder_path))       
    except FileNotFoundError:
        break
    
    copy_dir(folder_path,folder)
    
    os.chdir(drive_home)
    
    k = k + 1

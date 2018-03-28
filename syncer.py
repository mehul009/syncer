import shutil as shu   # librery for copy
import pandas as pd
import os
  
 
pwd = os.getcwd()                   # find working directory(use at end loop)
file = pd.read_csv('shutil.csv')  # read database file

i = 0
k = 0

while k == 0:            # main loop for only_file
    try:                 # exception if column value is more than dataframe
        copy_folder = file.at[i, 'only_file']
    except KeyError:
        break
    
    
    copy_folder = file.at[i, 'only_file']         # get data from file
    copy_folder_o = '/home/mehul09/' + copy_folder + '/'   # /home/mehul09 is home folder
   
    try:                 # exception if column value is nan
        list = os.listdir(copy_folder_o)       
    except FileNotFoundError:
        break
    list = os.listdir(copy_folder_o)       # find list of database's path
    je = 1
    j = 0
    while j < je :      # second loop
        if not os.path.exists(os.getcwd() + '/' + copy_folder):  # making directory if not present
            os.makedirs(os.getcwd() + '/' + copy_folder)     
            
        os.chdir(os.getcwd() + '/' + copy_folder)    # change the directory as require

        for o in list:                               # remove all dir
            try:
                shu.copy(copy_folder_o + str(o), os.getcwd())
            except IsADirectoryError:
                list.remove(o)

        je = len(list)
        for f in os.listdir(os.getcwd()) :
            if f == list[j]:
                j = j + 1     # if file is same than increase value

        if j < len(list) :        # if j in in limit than go for copy
            shu.copy(copy_folder_o + str(list[j]), os.getcwd())  # copy the file

        os.chdir(pwd)                      # after copy going into main directory
        j = j + 1

    i = i + 1
                    
os.chdir(pwd)   # go into main folder of disk


i = 0
k = 0

def copy (path):
    os.chdir(pwd)
    folder_o = '/home/mehul09/' + path + '/'
    list1 = os.listdir(folder_o)
    je = 1
    j =0
    while j < je :
        if not os.path.exists(os.getcwd() + '/' + path):  # making directory if not present
            os.makedirs(os.getcwd() + '/' + path)
        os.chdir(os.getcwd() + '/' + path)
        
        for o in list1:
            try :
                shu.copy(folder_o + str(o), os.getcwd())
            except IsADirectoryError:
                pwd2 = os.getcwd()
                copy(path + '/' + o )
                list1.remove(o)
                os.chdir(pwd2)
        
        je = len(list1)
        for f in os.listdir(os.getcwd()) :
            if j<len(list1):
                if f == list1[j]:
                    j = j + 1     # if file is same than increase value

        if j < len(list1) :        # if j in in limit than go for copy
            shu.copy(folder_o + str(list1[j]), os.getcwd())  # copy the file
        j = j + 1
        os.chdir(pwd)
    
while k == 0:            # main loop for only_file
    try:                 # exception if column value is more than dataframe
        copy_folder = str(file.at[i, 'with_dir'])
    except KeyError:
        break
    
    copy_folder = str(file.at[i, 'with_dir'])         # get data from file
    copy_folder_o = '/home/mehul09/' + copy_folder + '/'
    try:                 # exception if column value is nan
        list = os.listdir(copy_folder_o)
    except FileNotFoundError:
        break
    
    list = os.listdir(copy_folder_o)
    je = 1
    j =0
    while j < je :
        if not os.path.exists(os.getcwd() + '/' + copy_folder):  # making directory if not present
            os.makedirs(os.getcwd() + '/' + copy_folder)
        os.chdir(os.getcwd() + '/' + copy_folder)
        
        for o in list:
            try :
                shu.copy(copy_folder_o + str(o), os.getcwd())
            except IsADirectoryError:
                pwd1 = os.getcwd()
                copy(copy_folder + '/' + o )
                list.remove(o)
                os.chdir(pwd1)
        
        je = len(list)
        for f in os.listdir(os.getcwd()) :
            if j<len(list):
                if f == list[j]:
                    j = j + 1     # if file is same than increase value

        if j < len(list) :        # if j in in limit than go for copy
            shu.copy(copy_folder_o + str(list[j]), os.getcwd())  # copy the file

        os.chdir(pwd)                      # after copy going into main directory
        j = j + 1

    i = i + 1
                    
os.chdir(pwd)   # go into main folder of disk


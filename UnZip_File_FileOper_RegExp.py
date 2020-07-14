import os
import shutil
import re

''' 
    Program to extract a zip file 
    navigate to each file under this zip  
    find the files that contains phone number as ###-####-#### format (in digit)
'''

''' extract a zip folder'''
extracted_folder = shutil.unpack_archive('C:\\Users\\shyam\\Downloads\\Python_Test.zip','C:\\Users\\shyam\\Downloads\\','zip')

# for j in os.listdir('C:\\Users\\shyam\\Downloads\\Python_Test\\'):
#      path = 'C:\\Users\\shyam\\Downloads\\Python_Test\\' + j
#      print (os.listdir(path))

''' use os.walk function to navigate to each folder and sub-folder and files'''

for folder, sub_folders, files in os.walk('C:\\Users\\shyam\\Downloads\\Python_Test'):
    # print (f"Currently looking at {folder}")
    folder_path = folder

    # print(f"Sub folders are :")
    # for subfolder in sub_folders:
    #     print ( f"sub folder name : {subfolder}")
    # print(f"Files are :")

    for f in files:

        complete_file_path = folder_path + '\\' + f
        # print(f"File path is {complete_file_path}")
        file = open(complete_file_path,'r')
        file_content = file.read()
        file.close()
        pattern = re.compile(r'\d{3}-\d{4}-\d{4}')
        matches = pattern.finditer(file_content)
        for match in matches:
            print(match)
            print(match.group())

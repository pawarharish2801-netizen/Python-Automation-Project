import sys
import schedule 
from colorama import init, Fore, Style
import time 
import os
import shutil
import hashlib 
import zipfile

##Function Name : creat_zip
## Input         : folder (path of folder to compress)
## Output        : zip_name (name of created zip file)
## Description   : Used to create a zip archive of the given folder with timestamp
## Author        : Harish Mahendra Pawar
## Date          : 12/12/2025
def creat_zip(folder):
    timestamp = time.strftime("%Y-%m%d_%H-%M-%S")

    zip_name = folder + "_" + timestamp +  ".zip"

    #open the zip file

    zobj = zipfile.ZipFile(zip_name ,'w', zipfile.ZIP_DEFLATED)

    for root , dirs, files in os.walk(folder):
        for file in files:
            full_path = os.path.join(root,file)
            relative = os.path.relpath(full_path,folder)

            zobj.write(full_path,relative)
    zobj.close()

    return zip_name 

##Function Name : calculate_hash
## Input         : path (file path)
## Output        : MD5 hash string of the file
## Description   : Used to calculate MD5 hash of a file for integrity comparison
## Author        : Harish Mahendra Pawar
## Date          : 12/12/2025
def calculate_hash(path):
    hobj = hashlib.md5()
    
    fobj = open(path ,"rb")

    while(True):
        data = fobj.read(1024)

        if not data:
            break
        else:
            hobj.update(data)
    fobj.close()
    return hobj.hexdigest()

##Function Name : BackupFiles
## Input         : Source (source directory), Destination (backup directory)
## Output        : copied_files (list of newly copied or updated files)
## Description   : Used to backup new and updated files from source to destination
## Author        : Harish Mahendra Pawar
## Date          : 12/12/2025
def BackupFiles(Source, Destination):

    copied_files = []

    print("Creating the backup folder for backup process...")

    os.makedirs(Destination ,exist_ok=True)

    for root , dirs , files in os.walk(Source):

        for file in files:
            src_path = os.path.join(root,file)
            
            relative = os.path.relpath( src_path , Source)
            dest_path = os.path.join(Destination , relative)

            os.makedirs(os.path.dirname(dest_path), exist_ok=True)

            if((not os.path.exists(dest_path)) or (calculate_hash(src_path) != calculate_hash(dest_path))):
                shutil.copy2(src_path , dest_path)
                copied_files.append(relative)
    return copied_files

##Function Name : MarvellousDataShieldStart
## Input         : Source (source directory, default "Data")
## Output        : Nothing
## Description   : Used to start backup process, copy files and create zip archive
## Author        : Harish Mahendra Pawar
## Date          : 12/12/2025
def HarisShieldStart(Source = "Data"):
    Border = "*"*60
    BackupName = "HaribhauBackup"

    print(f"{Fore.GREEN}Success : {Style.RESET_ALL}",end=" ")
    print("Backup Process Started Successfully at :",time.ctime())

    files = BackupFiles(Source , BackupName)

    zip_file = creat_zip(BackupName)

    print(Border)
    print("Backup completed succesfully")
    print("Files copied : ",len(files))
    print("Zip file gets created with name : ",zip_file)
    print(Border)


##Function Name : main
## Input         : Command line arguments (sys.argv)
## Output        : Nothing
## Description   : Used to handle command line options and schedule periodic backup
## Author        : Harish Mahendra Pawar
## Date          : 12/12/2025
def main():

    Border = "-"* 60
    print(Border)
    print("----------------- Hari's Data Shield System --------------")
    print(Border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script is used to :")
            print("1 : Takes auto backup at the given time")
            print("2 : Backup only new and updated file ")
            print("3 : Create an archive of the backup periodically")

        elif(sys.argv[1] == "--U" or sys.argv[1] == "--u"):
            print("Use the automation script as  : ")
            print("python ScriptName.py <TimeInterval> <SourceDirectory> ")
            print("TimeInterval     : The time in minutes for periodic scheduling ")
            print("SourceDirectory  : Name of directory to do Backup")

        else:
            print(f"{Fore.RED}Error : {Style.RESET_ALL}",end=" ")
            print("Unable to proceed as there is no other option")
            print("Please use --h or --u to get more details")

    elif (len(sys.argv)==3 ):
        
        #Apply the Scheduler
        schedule.every(int(sys.argv[1])).minutes.do(MarvellousDataShieldStart, sys.argv[2])

        print(f"{Fore.GREEN}Success : {Style.RESET_ALL}",end=" ")
        print("Data Shield System Started Successfully ....")
        print("Time Interval in Minutes : " , sys.argv[1])
        print("Press Ctrl + C to stop the execution : (For Windows)")
        print("Press Ctrl + Z to stop the execution : (For Linux/macOS)")
        
        #Wait Till Abort
        while True:
            schedule.run_pending()
            time.sleep(1)
    
    else:
            print(f"{Fore.RED}Error :{Style.RESET_ALL}",end=" ")
            print("Invalid No of Command Line Argument")
            print("Unable to proceed as there is no other option")
            print("Please use --h or --u to get more details")
    
    print(Border)
    print("--------------- Thank you for using our Script -------------")
    print(Border)

if __name__ == "__main__":
    main()

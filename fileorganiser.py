import os       #operating system 
import shutil   #standard utility

#Taking name of the folder as an input
folder=input("enter the name of the folder that you want to sort: ")

#To find the items inside the folder
listoffiles=os.listdir(folder)

#To go through each file again & again
for file in listoffiles:
    name,ext=os.path.splitext(file)

    #To store the extension type
    # : - selects all
    ext=ext[1:]

    #If we encounter a folder, then we will continue to the next file
    if ext=="":
        continue

    #MOVING FILES TO THEIR RESPECTIVE FOLDERS
    #If folder already exists - move the file to that folder
    if os.path.exists(folder+"/"+ext):
        #move(source, destination)
        shutil.move(folder+"/"+file,folder+"/"+ext+"/"+file)

    #If folder does not exist - create folder & then move the file to that folder
    else:
        os.makedirs(folder+"/"+ext)
        shutil.move(folder+"/"+file,folder+"/"+ext+"/"+file)



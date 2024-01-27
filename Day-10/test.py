# number = input("please provide a number: ")
# print(number)

# 1st step:
#folders = input ("please provide folders name with spaces in between: ").split()
#print(folders)

#step 2

#folders = input ("please provide folders name with spaces in between: ").split()

#for folder in folders:
 #   print(folder)

# step 3 & 4 Write actual logic to identify the module  (os module) and print files

#import os
#folders = input("please provide folders name with spaces in between: ").split()
#for folder in folders:
#    files = os.listdir(folder)
#    print(" ==== listing files for the folder - " + folder)
#
#   for file in files:
#        print(file)

# step 5 : exceptional handling

import os
folders = input("please provide folders name with spaces in between: ").split()
for folder in folders:

    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("please provide valid folder name, this folder does not exist: " + folder )
        continue
    except PermissionError:
        print("you do not have access permission to this folder: " + folder)
        continue

    print(" ==== listing files for the folder - " + folder)

    for file in files:
        print(file)




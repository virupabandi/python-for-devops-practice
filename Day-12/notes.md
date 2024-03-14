## what is file operations?
Ans: if you want to Read a file or update a file or delete a file then you need file operations concept in python.

- This can be done by using shell script also but there shell script does not work with windows system. For windows system we have to write powershell script. so we cannot write 2 scripts in order to avoid all such things devops engr use python scripting. 

ex: if you want to upgrade the changes 


## what are file operations?
1. read operation
2. write operation
3. update server.config file.


Steps to write algorithm.
1. opening file with read mode
2. Read the file to Store all lines as variable that are there in the file 
3. Open the file in write mode
4. update the line in the file where you want to update. To update the file here we use if condition.


## How to write algorithm

# function (def) udpate_server_config(input 1 is file path, input 2 is property as key, value to be udpated):
def update_server_config(file_path, key, value):
    with open("file_path", "r") as file:
        lines = file.readlines()          # readlines is a inbuilt function. it reads server_config file and store as file as object

    with open(file_path, "w") as file:
        for line in lines:
            if key in line:
                file.write(key + "=" + value + "\n")
            else:
                file.write(line)


update_server_config("server.conf", "MAX_CONNECTIONS", "1000")           
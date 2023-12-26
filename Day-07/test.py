import sys

type = sys.argv[1]

if type == "t2.micro":

    print("ok, will create instance for you")

    # python test.py t2.micro

else:
    print("your input is not t2.micro hence we cannot create instance for you")

    # python test.py t2.medium

# (Above block of code does not work if you have more than 2 conditions. then if you have more than 2 conditions,
# you should use the below block of the code).
#-----------------------------------------------------------------------------------------------------------------    

import sys

type = sys.argv[1]

if type == "t2.micro":
    print("it will charge you 2 dollar per day")

    # python test.py t2.micro

elif type == "t2.medium":
    print("it will charge 4 dollar per day")

    #python test.py t2.medium

elif type == "t2.xlarge":
    print("it will charge 8 dollar per day")

    #python test.py t2.xlarge

else:
    print("Please provide valid instance type")

    # python test.py t2.abc
what are the steps to write the programme,

Step 1: Read the input from the User?
        (command line arguments or env vars or input)
        Input is nothing but similar to the command line arguments and env var like it reads input from the user but 
        input executes at the runtime.

        Eg: number = input("please provide a number")
            print (number)
            
            then output will be asking user to give number and that would be the output which will print.
            
            ## use case 1 of input: while executing terraform files, it will ask for yes or no after the apply or destroy
            # 2nd use case: installing any software it will ask you for yes or no.


Step 2: we need to write a for loop on the each folder provided by the user to list the files

step 3: To identify files module is required in python to perform this action.

step 4: print files.

step 5: handle any known errors.

        while finding files in the folder, if you give folder name which is not present the dir as input the you will get an error. To avoid these kind of error is known as exceptional handling.

        Exceptional handling Means: you are okay with the known error instead of terminating the programme execution.


        num1 = sys.argv[1]
num2 = sys.argv[2]
for number in dev:
    
try:
    div = num1/num2
except ZeroDivisionError:
    print("please dont provide zero as division element: ")
    continue
print(div)



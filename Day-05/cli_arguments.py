import sys      # sys module we should import it even though it comes with python installation.

def addition(num1,num2):
    add = num1 + num2
    return add

def sub(num1,num2):
    s = num1 - num2
    return s

def mul(num1,num2):
    m = num1 * num2
    return m

# Pass arguments here, by default arguments read as string
#num1 = int(sys.argv[1])             # it is value of argument 1 in the command in which we are passing input to the program
#operation = sys.argv[2]             # it is argument 2, which is the operation that we are going to perform 
#num2 = int(sys.argv[3])             # it is value of argument 3 in the command in which we are passing input to the program

# define operation here that we are going to perform
#if operation == "addition":         # Operation is addition
#    output = addition (num1, num2)  # Output would be addition
#    print (output)                  # Print the output


# Pass arguments here as float here because float take both float and int value.
num1 = float(sys.argv[1])             # it is value of argument 1 in the command in which we are passing input to the program
operation = sys.argv[2]             # it is argument 2, which is the operation that we are going to perform 
num2 = float(sys.argv[3])             # it is value of argument 3 in the command in which we are passing input to the program

# define operation here that we are going to perform
if operation == "addition":         # Operation is addition
    output = addition (num1, num2)  # Output would be addition
    print (output)                  # Print the output
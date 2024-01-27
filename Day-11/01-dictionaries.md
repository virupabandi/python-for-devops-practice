# Dictionaries
Dictionaries are most commonly used data types in python by DevOps engineers life. 
Eg: As a devops engineer, you write python script to interact with Jeera or aws most of the times, let say you are 
interacting with aws  and it will return to you with json format and you convert this json in to dictionaries in python and performs the task.

# the purpose of using dictionary data type is
- To store the properties of data (ec2_instance)
- we need key value pair to store the properties 
- to declare dictionaries in python we curly braces and between the curly braces we start writing the script
- 



## Overview:
A dictionary in Python is a data structure that allows you to store and retrieve values using keys. It is also known as a hashmap or associative array in other programming languages. Dictionaries are implemented as hash tables, providing fast access to values based on their keys.

## Creating a Dictionary:
```python
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
```

## Accessing Values:
```python
print(my_dict['name'])  # Output: John
```

## Modifying and Adding Elements:
```python
my_dict['age'] = 26  # Modifying a value
my_dict['occupation'] = 'Engineer'  # Adding a new key-value pair
```

## Removing Elements:
```python
del my_dict['city']  # Removing a key-value pair
```

## Checking Key Existence:
```python
if 'age' in my_dict:
    print('Age is present in the dictionary')
```

## Iterating Through Keys and Values:
```python
for key, value in my_dict.items():
    print(key, value)
```
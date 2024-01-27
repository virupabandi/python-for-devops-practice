# writing dictionary for single student.

student_info = {
    "name": "viru",
    "age" : "10",
    "class" : "11"
}


print(student_info["name"])

# write dictionary for multiple resource or students. 
#Here we have to use list because we have to write list of dictionaries.

ec2_instances_info = [
    {},             # dictionary 1
    {},             # dictionary 2
    {},             # dictionary 3
    {},             # dictionary 4
]


ec2_instances_info =[
    {
        "id": "instance-001",
        "type": "t2.micro"
    },
    {
        "id": "instance-002",
        "type": "t2.medium"
    },
    {
        "id": "instance-003",
        "type": "t2.xlarge"
    }
]

print(ec2_instances_info[1]["type"])

print(ec2_instances_info[2]["id"])



# tedious way: not good way of coding
std1 = "viru"
std2 = "ram"
std3 = "john"
std4 = "tim"

print(std1)
print(std2)
print(std3)
print(std4)

# lists, this is how we have to write

students_name = ["viru", "ram", "john", "tim"]
print(students_name)

# example real time use cases

s3_bucket_lists = ["viru_demo_bucket", "ram_demo_bucket", "john_demo_bucket", "tim_demo_bucket"]
print(s3_bucket_lists)

# python list.py

# now add new element to the list

s3_bucket_lists = ["viru_demo_bucket", "ram_demo_bucket", "john_demo_bucket", "tim_demo_bucket"]
s3_bucket_lists.append("new_s3_bucket")

print(s3_bucket_lists) # now check python list.py


# lets now learn how to remove element from list
#s3_bucket_lists = ["viru_demo_bucket", "ram_demo_bucket", "john_demo_bucket", "tim_demo_bucket"]

#s3_bucket_lists.remove("john_demo_bucket")

print(s3_bucket_lists) # now check python list.py

# now check the length of the list
print(len(s3_bucket_lists))  # now check python list.py

# now print any 1 element from the list. Element numbering starts from 0, 1,2,3 4, ,,,,,,,,
print(s3_bucket_lists[2])   # now check python list.py



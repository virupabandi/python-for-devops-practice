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


# now slicing the list, slicing is nothing but it will create the new list out of the existing list.
#print(s3_bucket_lists[0:2]) # no name to the new list 
# python list.py

new_list = print(s3_bucket_lists[0:3])
#python list.py

# sort the numbers in order
numbers = [1, 20, 15]
numbers.sort()
print(numbers)  #python test.py


#concatenating the string
print(s3_bucket_lists[0] + s3_bucket_lists[2])
#python test.py

print(s3_bucket_lists[0] + "+" + s3_bucket_lists[2])
#python test.py

print(s3_bucket_lists[0] + "--" + s3_bucket_lists[2])
#python test.py

#list heterogenous nature: which means all kind of data type (integer, float, string) can be used in the list as element.

random_list = [1,2,3, "ram", "abhi", 7.5]
print(random_list)
#python list.py

print(random_list[5])

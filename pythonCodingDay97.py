my_list = [60, 70, 80, 90, 100]
result = my_list[4::-1]
print (result)

"""
This Python code creates a list my_list containing integers 
[60, 70, 80, 90, 100]. Then, it creates a new list result by slicing 
my_list starting from index 4 (which is the last element) and moving 
backwards with a step of -1, effectively reversing the order of elements 
in the list.

Here's the breakdown:

my_list[4::-1]: This slicing operation starts from index 4 (the last element 
in the list) and moves backwards (-1 step) until the beginning of the 
list. So it effectively selects elements starting from the last element 
of my_list and goes backwards until the first element.

print(result): This prints the newly created list result, which contains 
the reversed order of elements from my_list.
"""
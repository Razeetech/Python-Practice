def fun(a, *args, s = '!'):
        print(a, s)
        for i in args :
            print(i, s)
fun(10)

"""
This code defines a function named fun that takes at least one argument (a) and any number of additional arguments (*args). It also has a default argument s set to '!'.

Here's a breakdown of the code:

def fun(a, *args, s='!'):

This line defines a function named fun.
a is a required positional argument.
*args collects any additional positional arguments into a tuple.
s='!' sets a default value of '!' for the keyword argument s.
print(a, s)

This line prints the value of a and s.
for i in args:

This line starts a loop iterating over each item in the args tuple.
print(i, s)

Inside the loop, this line prints the current item from args along with the value of s.
Finally, fun(10) is called, passing 10 as the value for a. Since no additional arguments are provided, args will be an empty tuple.
"""
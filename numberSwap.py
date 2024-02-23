#1 swap using temporary values:
a = 5
b = 10

temp = a
a = b
b = temp

print("After swapping using temporal value a =", a, "b = ", b )

#2 usin tuple unpacking
a = 7
b = 12

a, b = b, a
print("after swapping  using tuple unpackinga =", a, "b = ", b)

#using XOR bitwise operation
a = 20
b = 16

a = a ^ b
b = a ^ b
a  = a ^ b
print("after swapping using XOR =", a, "b = ", b)
'''Write a Python script that asks the user for three integer inputs: a, b, and c. Calculate the
result of (a ** b). Then, find the floor division of this result by c. Finally, find the modulus of the
floor division result with the number a. Print the final answer.'''
#
# 
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
#power calulate a and b
pow = a ** b
#floor division pow and c
flr_div = pow // c
#Modulus division result with a
modulus = flr_div%a
print("Result is: ",modulus)
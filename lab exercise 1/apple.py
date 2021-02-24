# N students take K apples and distribute them among each other evenly.
# The remaining (the undivisible) part remains in the basket. How many apples will remain in the basket.
# How many apples will remain in the basket? The program reads the numbers N and K.
# It should print the two answers for the questions above.
n = int(input("Enter the total number of students"))
k = int(input("Enter the total number of apples"))
s = k//n
r = k%n
print("The number of apples each student will be getting is",s)
print("The remaining numbers in the basket is",r)


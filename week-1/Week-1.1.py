Write a program to convert strings to an integer and float and display its type.

a=int(input())
b=float(input())
c=round(b,1)
print(a,end=",")
print(type(a))
print(c,end=",")
print(type(c))

Sample Output:
10,<class 'int'>
10.9,<class 'float'>

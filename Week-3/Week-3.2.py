a=int(input())

b=int(input())

c=int(input())

if(a==b and b==c):

    print("That's a equilateral triangle")

elif(a!=b and b==c or a==b and b!=c):

    print("That's a isosceles triangle")

elif(a!=b and b!=c):

    print("That's a scalene triangle")


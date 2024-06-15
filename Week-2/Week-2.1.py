An online retailer sells two products: widgets and gizmos. Each widget weighs 75 grams. Each gizmo weighs 112 grams. Write a program that reads the number of widgets and the number of gizmos from the user. Then your program should compute and display the total weight of the parts.


n=int(input())
p1=int(input())
p2=int(input())
p3=int(input())
p4=int(input())
if(p1%n==0):
    print("True",end=" ")
else:
    print("False",end=" ")
if(p2%n==0):
    print("True",end=" ")
else:
    print("False",end=" ")
if(p3%n==0):
    print("True",end=" ")
else:
    print("False",end=" ")
if(p4%n==0):
    print("True",end=" ")
else:
    print("False",end=" ")
Sample Input
10
20
Sample Output
The total weight of all these widgets and gizmos is 2990 grams.

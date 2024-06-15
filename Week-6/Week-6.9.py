
In this exercise, you will create a program that reads words from the user until the user enters a blank line. After the user enters a blank line your program should display each word entered by the user exactly once. The words should be displayed in the same order that they were first entered. For example, if the user enters:
Input: 
first
second
first
third
second

a,c=[],[]
    b=input()
    a.append(b)
for i in range(len(a)):
    if(a[i] not in c):
        c.append(a[i])
        print(a[i])

In the 1800s, the battle of Troy was led by Hercules. He was a superstitious person. He believed that his crew can win the battle only if the total count of the weapons in hand is in multiple of 3 and the soldiers are in an even number of count. Given the total number of weapons and the soldier's count, Find whether the battle can be won or not according to Hercules's belief. If the battle can be won print True otherwise print False.

a=int(input())
b=int(input())
if(a%3==0 and b%2==0):
    print("True")
else:
    print("False")
Sample Input:
32
43
Sample Output:'
False

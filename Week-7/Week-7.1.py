Abundant Number
An abundant number is a number for which the sum of its proper divisors is greater than the number itself. Proper divisors of the number are those that are strictly lesser than the number.

Input Format:
Take input an integer from stdin
Output Format:
Return Yes if given number is Abundant. Otherwise, print No
Example input:
12
Output:
Yes

def abundant(n):
    l,s=[],0
    for i in range(1,int(n//2)+1):
        if(n%i==0):
            l.append(i)
    for i in l:
        s+=i
    if(s>n):
        return("Yes")
    else:
        return("No")

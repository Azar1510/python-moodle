Given a string S which is of the format USERNAME@DOMAIN.EXTENSION, the program must print the EXTENSION, DOMAIN, USERNAME in the reverse order.

Input Format:
The first line contains S.

Output Format:
The first line contains EXTENSION.
The second line contains DOMAIN.
The third line contains USERNAME.


a = input()
ext = a.split('@')[0]
dom = a.split('@')[1].split('.')[0]
userno = a.find('.')
user = a[userno+1:]
print(user)
print(dom, end='\n')
print(ext,end='\n')


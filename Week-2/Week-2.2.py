In London, every year during Dasara there will be a very grand doll show. People try to invent new dolls of different varieties. The best-sold doll's creator will be awarded with a cash prize. So people broke their heads to create dolls innovatively. Knowing this competition, Mr.Lokpaul tried to create a doll that sings only when an even number is pressed and the number should not be zero and greater than 100.
 IF Lokpaul wins print true, otherwise false.



a=int(input())
if(a>0 and a<100 and a%2==0):
    print("True")
else:
    print("False")
Sample Input
10
Sample Output
True

Alfred buys an old scooter for Rs. X and spends Rs. Y on its repairs. If he sells the scooter for Rs. Z (Z>X+Y). Write a program to help Alfred to find his gain percent. Get all the above-mentioned values through the keyboard and find the gain percent.


buys=int(input())
repair=int(input())
sells=int(input())
g=(((sells-(buys+repair))/(buys+repair))*100)
print("{:.2f}".format(g), "is the gain percent.")

Sample Input:
10000
250
15000
Sample Output:
46.34 is the gain percent.

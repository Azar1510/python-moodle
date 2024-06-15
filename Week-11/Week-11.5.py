Develop a Python program that safely calculates the square root of a number provided by the user. Handle exceptions for negative inputs and non-numeric inputs.
Input Format:
User inputs a number.
Output Format:
Print the square root of the number or an error message if an exception occurs.

try:
    a=float(input())
    if(a<0):
        print("Error: Cannot calculate the square root of a negative number.")
    else:
        print("The square root of",a,"is {:.2f}".format(a**0.5))
except:
    print("Error: could not convert string to float")

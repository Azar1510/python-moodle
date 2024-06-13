a=int(input())
b=(a*0.04)+a
c=b+(b*0.04)
d=c+(c*0.04)
print("Balance as of end of Year 1: ${:.2f}.".format(b))
print("Balance as of end of Year 2: ${:.2f}.".format(c))
print("Balance as of end of Year 3: ${:.2f}.".format(d))

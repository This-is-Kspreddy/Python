#PROGRAM TO CALCULATE THE AREA OF THE TRIANGLE
a=float(input("Enter First Side : "))
b=float(input("Enter Second Side : "))
c=float(input("Enter Third Side : "))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**1/2
print('Area Of Traingle is :', area)

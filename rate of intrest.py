#PROGRAMME TO CALCULATE THE EMI
p=int(input('Enter Prinicple Amount : '))
t=int(input('Enter Total Number Of Years You Want To Pay : '))
r=float(input('Enter The Rate Of Intrest : '))
si=(p*t*r)/100
emi =si*p/t*12
print(emi)

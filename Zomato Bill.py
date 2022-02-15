bir=120
nv_bir=200
dum_bir=280
bong_chi=350
pot_bir=400
a1=input('Customer Name : ')
a2=int(input('Mobile Number : +91'))
c1=int(input('Number Of Biryani : '))
c2=int(input('Number Of N.v Biryani : '))
c3=int(input('Number Of Dum Biryani : '))
c4=int(input('Number Of Bongu Chicken : '))
c5=int(input('Number Of Pot Biryani : '))
cc=input('Enter Coupon Code :')
bill=(bir*c1)+(nv_bir*c2)+(dum_bir*c3)+(bong_chi*c4)+(pot_bir*c5)
print('Bill Payable : ',bill)
if bill<=500:
    if cc=='MYBILL' :
        dis=bill*50/100
        tax=0
    if cc=='HELLO' :
        dis=bill*30/100
        tax=0
elif bill>=200:
    if cc=='MYBILL' :
        dis=bill*20/100
        tax=bill*12/100
else:
    print('Invalid Coupon Code')
mainbill=bill-dis+tax
print('Total Amount Tax Incl... : ',bill+tax)
#print('Total Tax : ',tax)
print('Total Discount : ',dis)
print('Bill Amount : ',mainbill)
print('-------------------------------------THANKS FOR CHOOSING OUR APP------------------------------------')
    

from decimal import *
getcontext().prec = 8
print('What is the value of your shipment?')
value = input()
value = Decimal(value)
mpf = Decimal()
mpf = value * Decimal(.003464)
landed_cost = Decimal()
if mpf >= Decimal(485) :
  mpf = 485
elif mpf <= Decimal(25) :
  mpf = 25
else: mpf = value * Decimal(.003464)
landed_cost = str(value + mpf)
print('The cost plus merchandise fee is $' +landed_cost)

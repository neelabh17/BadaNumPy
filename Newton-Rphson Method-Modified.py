import math
from BadaNumNeelabh1 import * 
n=int(input("Which numbers inverse you wish to find out: "))
divisor=bigNum()
divisor.setInput(n)
starter=bigNum()
divident=int(input("Enter Divident: "))
d2=bigNum()
d2.setInput(divident)
p=d2.length-divisor.length
starter.setInput(pow(10,p))

starter2=bigNum()
starter2.setInput(2*pow(10,divisor.length+p))
for i in range(math.ceil(math.log(abs(p)+1,2))+10):

	# print(math.floor(i), end="::")
	# starter.showOutput()
	# print("\n")
	starter=divideByPowerOfTen(multiplyBigNum(starter,subBigNum(starter2,multiplyBigNum(divisor,starter))),divisor.length+p)


q=divideByPowerOfTen(multiplyBigNum(starter,d2),divisor.length+p)

# print("q1: ",end="")
# q.showOutput()
# print("\nq2: ",end="")
# print(divident//n)
one=bigNum()
one.setInput(1)

fc=multiplyBigNum(addBigNum(q,one),divisor).compare(d2)
while(fc==-1 or fc==0):
	q=addBigNum(q,one)
	fc=multiplyBigNum(addBigNum(q,one),divisor).compare(d2)
q.showOutput()


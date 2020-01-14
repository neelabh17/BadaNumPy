import cmath
import math
import random
import time
base=1000000
def timing(f):

	def wrap(*args):
		time1=time.time()
		ret =f(*args)
		time2=time.time()
		print('{:s} function took {:.3f} ms'.format(f.__name__,(time2-time1)*1000.0))
		return ret
	return wrap
class bigNum():
	def __init__(self):
		self.numArray=[]
		self.length=0
		self.isNegative=False
		self.parityMaintainer=1
		

	def setInput(self,input):
		inp=str(input)
		l=len(inp)
		if(inp[0]=='-'):
			self.isNegative=True
			self.parityMaintainer=-1
			
			# i=1
			# while(i<l):
			# 	if(l-1-i+1<6):
			# 		self.numArray.append(int(inp[i:l]))
			# 	else:
			# 		self.numArray.append(int(inp[i:i+6]))	
			# 	i+=6		
			i=l-1
			while(i>=1):
				if(i<6):
					self.numArray.append(int(inp[1:i+1]))
				else:
					self.numArray.append(int(inp[i-5:i+1]))
				i-=6
			# for i in range(1,l):
			# 	self.numArray.append(int(inp[i]))

		else:
			i=l-1
			while(i>=0):
				if(i+1<6):
					self.numArray.append(int(inp[0:i+1]))
				else:
					self.numArray.append(int(inp[i-5:i+1]))
				i-=6
			# i=0
			# while(i<l):
			# 	if(l-1-i+1<6):
			# 		self.numArray.append(int(inp[i:l]))
			# 	else:
			# 		self.numArray.append(int(inp[i:i+6]))
			# 	i+=6
			# for i in range(l):
			# 	self.numArray.append(int(inp[i]))
		self.numArray.reverse()
		self.length=len(self.numArray)

	def getInput(self):
		inp=input()
		l=len(inp)
		if(inp[0]=='-'):
			self.isNegative=True
			self.parityMaintainer=-1
			
			# i=1
			# while(i<l):
			# 	if(l-1-i+1<6):
			# 		self.numArray.append(int(inp[i:l]))
			# 	else:
			# 		self.numArray.append(int(inp[i:i+6]))	
			# 	i+=6		
			i=l-1
			while(i>=1):
				if(i<6):
					self.numArray.append(int(inp[1:i+1]))
				else:
					self.numArray.append(int(inp[i-5:i+1]))
				i-=6
			# for i in range(1,l):
			# 	self.numArray.append(int(inp[i]))

		else:
			i=l-1
			while(i>=0):
				if(i+1<6):
					self.numArray.append(int(inp[0:i+1]))
				else:
					self.numArray.append(int(inp[i-5:i+1]))
				i-=6
		self.numArray.reverse()
		self.length=len(self.numArray)

	
	def showOutput(self):

		if(self.isNegative==True):
			print("-",end="")
		print(self.numArray[0],end="")
		for i in range(1,self.length):
			print(str(self.numArray[i]).zfill(6),end="")
		print("\n",end="")

	def makeNegative(self):
		if(self.isNegative==True):
			self.isNegative=False
			self.parityMaintainer=1
			
		else:
			self.isNegative=True
			self.parityMaintainer=-1
			

	def compareMod(self,otherNumber):
		if(self.length>otherNumber.length):
			return 1
		elif(self.length<otherNumber.length):
			return -1
		else:
			flag=0
			for i in range(self.length):
				if(otherNumber.numArray[i]<self.numArray[i]):
					flag=1
					break;
				elif(otherNumber.numArray[i]>self.numArray[i]):
					flag=-1
					break
			return flag


	def compare(self,otherNumber):#1 self greater than other -1 for self less than other 0 for both equal
		if(self.isNegative==False and otherNumber.isNegative==False):
			return self.compareMod(otherNumber)
		elif(self.isNegative==False and otherNumber.isNegative==True):
			return 1
		elif(self.isNegative==True and otherNumber.isNegative==False):
			return -1
		else:
			return -1*self.compareMod(otherNumber)

	def valueAtSpecificPlace(self,n):
		if n>=self.length:
			return 0
		else:
			return self.numArray[n]

	def removeZeroes(self):
		while(self.length!=1 and self.numArray[0]==0):
			self.numArray.pop(0)
			self.length-=1
	def returnStringOutput(self):
		if(self.parityMaintainer==-1):
			s="-"
		else:
			s=""
		s=s+str(self.numArray[0])
		for i in range(1,self.length):
			s=s+str(self.numArray[i]).zfill(6)
		return s

@timing
def addBigNum(a,b):
	c=bigNum()
	maxLen=max(a.length,b.length)
	carry=0
	

	takeAlternative=False


	if(a.parityMaintainer==-1 and b.parityMaintainer==-1):
		takeAlternative=True
	elif(a.parityMaintainer==-1 and b.parityMaintainer==1 and a.compareMod(b)==1):
		takeAlternative=True
	elif(a.parityMaintainer==1 and b.parityMaintainer==-1 and b.compareMod(a)==1):
		takeAlternative=True


	if(takeAlternative==True):
		a.makeNegative()
		b.makeNegative()

	a.numArray.reverse()
	b.numArray.reverse()
	print("aaaaaaaa")
	print(a.numArray)
	print("bbbbbbbbb")
	print(b.numArray)

	for i in range(maxLen+1):
		d=(a.parityMaintainer*a.valueAtSpecificPlace(i)+b.parityMaintainer*b.valueAtSpecificPlace(i)+carry)

		c.numArray.append(d%base)
		# c.numArray.append(d%10)
		c.length+=1
		carry=d//base
		# carry=d//10
	if(takeAlternative==True):
		a.makeNegative()
		b.makeNegative()
		c.makeNegative()

	print("cccccccccccc")
	print(c.numArray)
	a.numArray.reverse()
	b.numArray.reverse()
	c.numArray.reverse()
	print("cccccrrrrrrrrrrrrr")
	print(c.numArray)
	c.removeZeroes()
	print(c.numArray)
	return(c)
def subBigNum(a,b):
	
	b.makeNegative()
	c= addBigNum(a,b)
	b.makeNegative()
	return c

def basicMulti(a,n):
	c=bigNum()
	if(n==10):
		a.numArray.append(0)
		a.length+=1
		return a
	elif(n==0):
		c=setInput(0)
		return c
	elif(n==1):
		return a
	else:
		a.numArray.reverse()

		for i in range(a.length+1):
			d=(a.valueAtSpecificPlace(i)*n+carry)

			c.numArray.append(d%base)
			c.length+=1
			carry=d//base

		a.numArray.reverse()
		c.numArray.reverse()
		c.removeZeroes()
		return(c)
def FFT(a,m,w):
	if(m==1):
		return a
	else:
		a_even=[]
		a_odd=[]
		for i in range(m):
			if(i%2==0):
				a_even.append(a[i])
				
			else:
				a_odd.append(a[i])
		#print("A:",end="")
		#print(a)
		#print("m:", end="")
		#print(m)
		#print(a_even)
		#print(a_odd)
		F_even=FFT(a_even,m//2,pow(w,2))
		F_odd=FFT(a_odd,m//2,pow(w,2))
		F=[0 for i in range(m)]
		x=1
		for i in range(m//2):
			#print(" the complex number being:",end="")
			#print(x)
			F[i]=F_even[i]+x*F_odd[i]
			F[i+(m//2)]=F_even[i]-x*F_odd[i]
			x*=w

		# print(F)
		#print("-------------------------")
		return F




@timing
def multiplyBigNum(c,d):
	a=bigNum()
	b=bigNum()
	a.setInput(c.returnStringOutput())
	b.setInput(d.returnStringOutput())
	maxi=max(len(a.numArray),len(b.numArray))
	powerr=math.ceil(math.log(maxi,2))
	FFTlen=pow(2,powerr)
	FFTlen*=2
	#print(FFTlen)
	a_array=[0 for i in range(FFTlen)]
	b_array=[0 for i in range(FFTlen)]
	a.numArray.reverse()
	b.numArray.reverse()
	for i in range(FFTlen):
		a_array[i]=a.valueAtSpecificPlace(i)
		b_array[i]=b.valueAtSpecificPlace(i)
	a.numArray.reverse()
	b.numArray.reverse()
	iota =0+1j
	w=math.cos(2*math.pi/FFTlen)+iota*math.sin(2*math.pi/FFTlen)

	aModified=FFT(a_array,FFTlen,w)
	bModified=FFT(b_array,FFTlen,w)
	# print(aModified)
	# print(bModified)
	c=[0 for i in range(FFTlen)]
	for i in range(FFTlen):
		c[i]=aModified[i]*bModified[i]

	cBackInPoly=FFT(c,FFTlen,pow(w,-1))
	for i in range(FFTlen):
		cBackInPoly[i]/=FFTlen
	carry=0
	cFinal=bigNum()
	# print(cBackInPoly)
	for i in range(FFTlen):
		if(cBackInPoly[i].real>0):
			x=round(cBackInPoly[i].real)+carry
		else:
			x=0+carry
			
		#print("x: ",end="")
		#print(x)
		cFinal.numArray.append(x%base)
		cFinal.length+=1
		carry=x//base
	# print(a.isNegative)
	# b.showOutput()
	# print(b.isNegative)
	# print(cFinal.numArray)
	if(a.isNegative==True and b.isNegative==True):
		cFinal.isNegative=False
	elif(a.isNegative==False and b.isNegative==False):
		cFinal.isNegative=False
	else:
		cFinal.isNegative=True
	if(cFinal.isNegative==True):
		cFinal.parityMaintainer=-1
	else:
		cFinal.parityMaintainer=1
	cFinal.numArray.reverse()
	cFinal.removeZeroes()
	# cFinal.showOutput()
	return cFinal

def divideByPowerOfTen(number,power):
	c=bigNum()
	if(power>=number.length):
		
		c.setInput(0)
		return c
	else:
		c=bigNum()
		c.isNegative=number.isNegative
		c.parityMaintainer=number.parityMaintainer
		for i in range((number.length)-power):
			c.numArray.append(number.numArray[i])
			c.length+=1
	# c.showOutput()
	return c
@timing
def divideBigNum(y1,y2):

	a=bigNum()
	b=bigNum()
	a.setInput(y1.returnStringOutput())
	b.setInput(y2.returnStringOutput())
	divisor=b
	# divisor.showOutput()
	starter=bigNum()
	
	
	d2=a
	p=d2.length-divisor.length
	starter.setInput(int(pow(10,p)))

	starter2=bigNum()
	starter2.setInput(2*int(pow(10,divisor.length+p)))
	for i in range(math.ceil(math.log(abs(p)+1,2))+10):
	# for i in range(10):
		# print(math.floor(i), end="::")
		# starter.showOutput()
		# print("\n")
		# print("Dxi: ",end="")
		x1=multiplyBigNum(divisor,starter)
		# print("Dxi: ",end="")
		# x1.showOutput()
		x2=subBigNum(starter2,x1)
		# print("2-Dxi: ",end="")
		# x2.showOutput()
		x3=multiplyBigNum(starter,x2)
		# print("x1*2-Dxi: ",end="")
		# x3.showOutput()
		starter=divideByPowerOfTen(x3,divisor.length+p)
		# print("(x1*2-Dxi)/10^l+p: ",end="")
		# starter.showOutput()
		print(1)
		# input()
	
	q=divideByPowerOfTen(multiplyBigNum(starter,d2),divisor.length+p)
	print(2)
	# print("q1: ",end="")
	# q.showOutput()
	# print("\nq2: ",end="")
	# print(divident//n)
	one=bigNum()
	one.setInput(1)

	fc=multiplyBigNum(addBigNum(q,one),divisor).compare(d2)
	print(3)
	counter=0
	while(fc==-1 or fc==0):
		q=addBigNum(q,one)
		print("im stuck here")
		fc=multiplyBigNum(addBigNum(q,one),divisor).compare(d2)
		counter+=1
	print("counterid ",counter)
	return (q,subBigNum(d2,multiplyBigNum(q,divisor)))

def generateRanmdom(bigNumber):
	arr=bigNumber.numArray
	if(bigNumber.length==0):
		c=bigNumber;
		return c
	else:
		# first element should be less than first element of bignumber
		c=bigNum()
		c.numArray.append(random.randint(0,arr[0]))
		c.length+=1
		i=1
		while(i<bigNumber.length):
			if(c.numArray[i-1]==arr[i-1]):

				c.numArray.append(random.randint(0,arr[i]))
				c.length+=1
			else:
				c.numArray.append(random.randint(0,9))
				c.length+=1
			i+=1
		c.removeZeroes()
		return c
def expmod(x,y,z):
	a=bigNum()
	n=bigNum()
	m=bigNum()
	a.setInput(x.returnStringOutput())
	n.setInput(y.returnStringOutput())
	m.setInput(z.returnStringOutput())
	zero=bigNum()
	one=bigNum()
	two=bigNum()
	two.setInput(2)
	one.setInput(1)
	zero.setInput(0)
	
	# while(n.compare(zero)!=0):
	# 	(div2,mod2)=divideBigNum(n,two)
	# 	if(mod2.compare(one)==0):
	# 		(tmp,p)=divideBigNum(multiplyBigNum(p,xseq),m)
	# 		p.showOutput()
	# 	xseq=multiplyBigNum(xseq,xseq)
	# 	print("yay n is ::",end="")
	# 	n.showOutput()
	# 	print("\n")
	# 	xseq.showOutput()

	# 	n=div2

	# return p
	if(n.compare(zero)==0):
		return one
	else:
		(div2,mod2)=divideBigNum(n,two)
		div2.showOutput()
		if(mod2.compare(one)==0):
			t=expmod(a,div2,z)
			(c,d)=divideBigNum(multiplyBigNum(t,t),z)
			t1=multiplyBigNum(a,d)
			(e,f)=divideBigNum(t1,z)
			f.showOutput()
			(temp,p)=divideBigNum(f,z)
			# p.showOutput()
			return  p
		else:
			t=expmod(a,div2,z)
			t1=multiplyBigNum(t,t)
			(c,d)=divideBigNum(t1,z)
			d.showOutput()
			(temp,p)=divideBigNum(d,z)
			# p.showOutput()
			return p


def Fermat(n):
	one=bigNum()
	one.setInput(1)
	# a=generateRanmdom(subBigNum(n,one))
	a=bigNum()
	a.setInput(200)
	# print("ok")
	# a.showOutput()
	# n.showOutput()
	return (expmod(a,n,n).compare(a)==0)

def prime(n,M):
	i,failed=0,False

	while((not failed) and (i<M) ):
		failed=not Fermat(n)
		# print(i)
		i+=1
	
	return (not failed)
@timing
def changeBase(n,base):
	difBase=[]
	zero=bigNum()
	zero.setInput(0)
	(q,r)=divideBigNum(n,b)
	while(r.compare(zero)!=0 or q.compare(zero)!=0):
		difBase.append(int(r.returnStringOutput()))
		print("r is")
		r.showOutput()
		(q,r)=divideBigNum(q,b)
	return difBase
@timing
def ad(a,b):
	return a+b
a=bigNum()
b=bigNum()
# a.setInput(558558849320833739867734104911100010767776210080294510110521111104630610771255884932083373986773410491110001076777621008029451011052111110463061077125588493208337398677341049111000107677762100802945101105211111046306107712849320833739867734104911100010767776210080294510110521111104630610771255855884932083373986773410491110001076777621008029451011052111110463061077125588493208337398677341049111000107677762100802945101105211111046306107712558849320833739867734104911100010767776210080294510110521111104630610771284932083373986773410491110001076777621008029451011052111110463061077125585588493208337398677341049111000107677762100802945101105211111046306107712558849320833739867734104911100010767776210080294510110521111104630610771255884932083373986773410491110001076777621008029451011052111110463061077128493208337398677341049111000107677762100802945101105211111046306107712558558849320833739867734104911100010767776210080294510110521111104630610771255884932083373986773410491110001076777621008029451011052111110463061771255884932083373986773410491110001076777621008029451011052111110463061077128493208337398677341049111000107677762100802945101105211111046306107712)
# b.setInput(66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666)
# (c,d)=divideBigNum(a,b)
# d.showOutput()
# print("Done")
a.getInput()
print(a.numArray)
b.getInput()
print(b.numArray)
c=multiplyBigNum(a,b)
c.showOutput()
s=input()
z=c.returnStringOutput()
for i in range((len(s))):
	if(not z[i]==s[i]):
		print(" ",end="")
	else:
		print(s[i],end="")
# print(sys.maxS2147483647ize)
# 
# print(a.length)
# b.getInput()
# # (c,d)=divideBigNum(a,b)
# d=multiplyBigNum(a,b)
# # print(changeBase(a,b))
# # addBigNum(a,b).showOutput()
# # print(ad(100000000000000110000000000000011000000000000001100000000000000110000000000000011000000000000001100000000000000110000000000000011000000000000001100000000000000110000000000000011000000000000001100000000000000110000000000000011000000000000001100000000000000110000000000000011000000000000001100000000000000110000000000000011000000000000001100000000000000110000000000000011000000000000001100000000000000110000000000000011000000000000001100000000000000110000000000000011000000000000001100000000000000110000000000000011000000000000001100000000000000110000000000000011000000000000001100000000000000110000000000000011000000000000001100000000000000110000000000000011000000000000001100000000000000110000000000000011000000000000001,100000000000000110000000000000011000000000000001100000000000000110000000000000011000000000000001100000000000000110000000000000011000000000000001100000000000000110000000000000011000000000000001100000000000000110000000000000011000000000000001100000000000000110000000000000011000000000000001100000000000000110000000000000011000000000000001100000000000000110000000000000011000000000000001100000000000000110000000000000011000000000000001100000000000000110000000000000011000000000000001100000000000000110000000000000011000000000000001100000000000000110000000000000011000000000000001100000000000000110000000000000011000000000000001100000000000000110000000000000011000000000000001100000000000000110000000000000011000000000000001))
# # c.showOutput()
# d.showOutput()
# print("Done")
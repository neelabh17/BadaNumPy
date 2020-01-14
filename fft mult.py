import cmath
import math
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
			for i in range(1,l):
				self.numArray.append(int(inp[i]))

		else:
			for i in range(l):
				self.numArray.append(int(inp[i]))
		self.length=len(self.numArray)

	def getInput(self):
		inp=input()
		l=len(inp)
		if(inp[0]=='-'):
			self.isNegative=True
			self.parityMaintainer=-1
			

			for i in range(1,l):
				self.numArray.append(int(inp[i]))

		else:
			for i in range(l):
				self.numArray.append(int(inp[i]))
		self.length=len(self.numArray)

	
	def showOutput(self):

		if(self.isNegative==True):
			print("-",end="")

		for i in range(self.length):
			print(self.numArray[i],end="")

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
		for i in range(self.length):
			s=s+str(self.numArray[i])
		return s
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

			c.numArray.append(d%10)
			c.length+=1
			carry=d//10

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





def multiplyBigNum(a,b):
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
	c=[0 for i in range(FFTlen)]
	for i in range(FFTlen):
		c[i]=aModified[i]*bModified[i]

	cBackInPoly=FFT(c,FFTlen,pow(w,-1))
	for i in range(FFTlen):
		cBackInPoly[i]/=FFTlen
	carry=0

	cFinal=bigNum()
	#print(cBackInPoly)
	for i in range(FFTlen):
		x=round(cBackInPoly[i].real)+carry
		#print("x: ",end="")
		#print(x)
		cFinal.numArray.append(x%10)
		cFinal.length+=1
		carry=x//10
	# print(a.isNegative)
	# b.showOutput()
	# print(b.isNegative)
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

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

	def setItTo(a):
		a=0#write the code
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

	for i in range(maxLen+1):
		d=(a.parityMaintainer*a.valueAtSpecificPlace(i)+b.parityMaintainer*b.valueAtSpecificPlace(i)+carry)

		c.numArray.append(d%10)
		c.length+=1
		carry=d//10
	if(takeAlternative==True):
		a.makeNegative()
		b.makeNegative()
		c.makeNegative()


	a.numArray.reverse()
	b.numArray.reverse()
	c.numArray.reverse()
	c.removeZeroes()
	return(c)
def subBigNum(a,b):
	c=b
	c.makeNegative()
	return addBigNum(a,c)

def basicMulti(a,n):
	c=bigNum()
	if(n==0):
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

def multiBigNum(a,b):
	



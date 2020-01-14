import random
def split(a):


	n=(len(a)//2)
	return a[0:n],a[n:]

def merge(a1,a2):
	if(len(a1)==0):
		return a2
	elif(len(a2)==0):
		return a1
	else:
		if(a1[0]>=a2[0]):
			
			return [a2[0]]+merge(a1,a2[1:])
		else:
			
			return [a1[0]]+merge(a1[1:],a2)
def mergeSort(a):

	if(len(a)==0):
		return a
	elif(len(a)==1):
		return a
	else:
		(a1,a2)=split(a)
		a1=mergeSort(a1)
		a2=mergeSort(a2)
		d=merge(a1,a2)
		
		return d

x=[]
n=int(input())
for i in range(n):
	x.append(random.randint(1,100))
d=(mergeSort(x))
print(x)
print(d)



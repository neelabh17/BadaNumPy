import random
import functools
import time
#########################
def timeit(func):
        @functools.wraps(func)
        def newfunc(*args, **kwargs):
                startTime = time.time()
                func(*args, **kwargs)
                elapsedTime = time.time() - startTime
                print('function [{}] finished in {} ms'.format(func.__name__, int(elapsedTime * 1000)))
        return newfunc
############################
def findPlace(x,a,left,right):
	
	i,j=left,right
	while(i<=j):
		if(a[i]<=x):
			i+=1
		else:
			a[i],a[j]=a[j],a[i]
			j-=1	
	p=j
	return p	


	
def qsort(a,left,right):
	if(left<=right):
		posi=findPlace(a[left],a,left,right)
		a[left],a[posi]=a[posi],a[left]
		qsort(a,left,posi-1)
		qsort(a,posi+1,right)
@timeit
def quicksort(a):
	
	if(len(a)== 1 or len(a)==0 ):
		return a
	else:
		qsort(a,0,len(a)-1)
		return a


	#Assert: a is sorted


x=[]
n=int(input())
for i in range(n):
	x.append(random.randint(1,100))
# print(x)
d=(quicksort(x))

# print(d)



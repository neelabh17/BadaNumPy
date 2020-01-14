
def insort(a,left,right):
	i=left

	while(i<=right):
		j=i
		p=j
		mini=a[j]
		print(a)
		print(a[j],j)
		while(j<=right):
			if(a[j]<=mini):
				p=j
				mini=a[j]
			j+=1
		
		print(p)
		a[i],a[p]=a[p],a[i]
		i+=1
	return a

print(insort([2,3,2,4,3,5,4,5,4,6,5],0,10))
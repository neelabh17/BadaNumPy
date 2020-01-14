def sieve(n):
	a=[i for i in range(n+1)]
	# print(a)
	i=2
	while(i*i<=n):
		j=2
		#Deleting elements
		while(i*j<=n):
			a[i*j]=0
			j=j+1

		#Find next value for i
		i=i+1

	while(a[i]==0 and i<=n):
		i+=1

	print(a)
n=input()
sieve(int(n))

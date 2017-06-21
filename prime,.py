n=int(input())
f=0
if n==2:
	print "it is prime"
for i in range(2,n):
	if n%i==0:
		f=1
		break
	if f==0:
		print"it is prime"
	else:
		print"it is not prime"

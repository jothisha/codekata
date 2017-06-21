a=int(input())
b=int(input())
while a<b:
	f=0
	for i in range(2,a):
		if a%i==0:
			f=1
			break
	if f==0:
		print a
	a=a+1

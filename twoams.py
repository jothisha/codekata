def ams(a):
	m=a
	result=0
	while a!=0:
		r=a%10
		result+=r*r*r
		q=a/10
		a=q
	if(result==m):
		return 1
	else:
		return 0
b=int(input())
c=int(input())
for i in range(b,c):
	if ams(i):
		print i

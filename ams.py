a=int(input())
m=a
result=0
while a!=0:
	r=a%10
	result+=r*r*r
	q=a/10
	a=q
if(result==m):
	print"amstrong number"
else:
	print"not amstrong number"

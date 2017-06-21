n=int(input())
k=n
q=0
while n!=0:
	r=n%10
	q=q*10+r
	n=n/10
if k==q:
	print"it is palindrome"
else:
	print"it is not palindrome"

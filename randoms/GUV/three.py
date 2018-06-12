a,b,c=map(int,input().split()) #get the things in same line
if a>b and a>c:
	print(a)
elif b>c:
	print(b)
else:
	print(c)
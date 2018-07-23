loop = int(input())
while loop>0:
	a=list(map(int,input().split()))
	b=sorted(a)
	print(b[1])
	loop-=1
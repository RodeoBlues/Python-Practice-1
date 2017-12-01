loop=int(input())
while loop>0:
	f1,f2 = map(int,input().split())
	print(f1%f2)
	loop-=1
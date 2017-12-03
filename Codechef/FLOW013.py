loop = int(input())
while loop > 0:
	a,b,c = map(int,input().split())
	if (a == 0 or b == 0 or c == 0) or (a+b+c != 180):
		print('NO')
	else:
		print("YES")
	loop-=1

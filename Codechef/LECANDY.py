for _ in range(int(input())):
	n,c = map(int,input().split())
	l = list(map(int,input().split()))
	if (sum(l) <= c):
		print('Yes')
	else:
		print('No')
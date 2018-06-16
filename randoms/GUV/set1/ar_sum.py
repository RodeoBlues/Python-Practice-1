def array_sum():
	n,total=map(int,input().split())
	e = list(map(int,input().split()))
	out=0
	while total>0:
		out += e[total-1]
		total-=1
	print(out)

array_sum()

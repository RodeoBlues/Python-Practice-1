n,total=map(int,input().split())
e = list(map(int,input().split()))
result = 0
while total > 0:
	result = result + e[total]
	total -= 1
print(result)
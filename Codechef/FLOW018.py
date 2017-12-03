loop = int(input())
while loop>0:
	in_val=int(input())
	fact=1
	for i in range(1,in_val+1):
		fact *= i
	print(fact)
	loop-=1
loop = int(input())
fact = 1
while loop>0:
	in_val = int(input())
	for i in range(1,in_val+1):
		fact = fact * i
	print(fact)
	fact = 1
	loop = loop-1
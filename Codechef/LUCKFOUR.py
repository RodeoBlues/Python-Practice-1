loop = int(input())
while loop>0:
	in_val = input()
	count = 0
	for i in in_val:
		int_i = int(i)
		if int_i == 4:
			count+=1
	print(count)  
	loop-=1
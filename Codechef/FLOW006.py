loop=int(input())
while loop>0:
	in_value=int(input())
	total=0
	while in_value>0:
		last=in_value//10
		rem_last=in_value%10
		total=rem_last+total
		in_value=last
	print(total)
	loop-=1
loop=int(input())
while loop>0:
	in_val=input()
	leni = len(in_val)
	while leni>0:
		print(in_val[leni-1],end='')
		leni-=1
	print()
	loop-=1
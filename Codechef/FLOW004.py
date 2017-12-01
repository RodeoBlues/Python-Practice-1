loop=int(input())
while loop>0:
	in_val=input()
	length=len(in_val)
	summ = int(in_val[0])+int(in_val[length-1])
	print(summ)
	loop-=1
'''This code may have bugs'''
loop = int(input())
while loop>0:
	n = int(input())
	rev = []
	while n>0:
		last = n%10
		rev.append(str(last))
		n=n//10
	print(''.join(rev))
	loop-=1
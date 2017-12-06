'''This code may have bugs'''
loop = int(input())
while loop>0:
	n = int(input())
	rev = 0
	while n>0:
		last = n%10
		rev=(rev*10)+last
		n=n//10
	print(rev)
	loop-=1
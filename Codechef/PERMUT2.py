#

'''
First get n as 5
[1,2,3,4,5]
[2,3,4,5,1]

'''

while True:
	n = int(input())
	perm = []
	if n == 0:
		break
	l = list(map(int,input().split()))
	for i in l:

		perm.append(i)

	print(l)
'''

Given a number N and an array of N integers, print the sorted array.
Input Size : 1 <= N <= 1000
Sample Testcase :
INPUT
3
2 1 3
OUTPUT
1 2 3

'''
loop = int(input())
a=[]
for _ in range(loop):
	i = int(input())
	a.append(i)

min_val = a[0]
for i in range(len(a)-1):
	if min_val < a[i]:
		print (min_val,a[i])
	else:
		min_val=a[i]
		print(min_val)
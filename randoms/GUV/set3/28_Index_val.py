'''

Given a number N and an array of N elements, print each element with its index.
Sample Testcase :
INPUT
3
2 1 3
OUTPUT
2 0
1 1
3 2 

'''
loop = int(input())
a=[]
for _ in range(0,loop):
	l = list(map(int,input().split()))
for i in range(len(a)-1):
	print(a[i],i)
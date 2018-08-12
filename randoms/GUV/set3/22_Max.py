'''
22 - Given a number N and an array of N integers, print the maximum element.
Input Size : 1 <= N <= 100000
Sample Testcase :
INPUT
3
1 2 3
OUTPUT
3 
'''

loop = int(input())
for i in range(loop):
	max = 0
	userInput = int(input())
	if userInput > max:
		max = userInput
print(max)


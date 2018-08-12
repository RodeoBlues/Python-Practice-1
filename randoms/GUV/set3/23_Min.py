'''

Given a number N and an array of N integers, print the minimum element.
Input Size : 1 <= N <= 100000
Sample Testcase :
INPUT
3
1 2 3
OUTPUT
1

'''

loop = int(input())
for _ in range(loop):
	userInput = int(input())
	min = userInput
	if min > userInput:
		min = userInput
print(min) 
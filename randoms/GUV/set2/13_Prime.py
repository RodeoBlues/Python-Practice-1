'''
Check whether a number is prime or not. Print yes if its a prime, no if it is not.
Input Size : N <= 1000
Sample Testcase :
INPUT
11
OUTPUT
yes 
'''
userInput = int(input())

def isPrime(userInput):
	if (userInput<=1):
		return True

	for i in range(2,userInput):
		if ((userInput % i)== 0):
			return False
	
		return False

if isPrime(userInput):
	print('yes')
else:
	print('no')

# def isPrime(n):
     
#     # Corner case
#     if (n <= 1):
#         return False
 
#     # Check from 2 to n-1
#     for i in range(2, n):
#         if (n % i == 0):
#             return False
 
#     return True
 
# # Driver Program 
# if isPrime(2):
#     print ("true")
# else:
#     print ("false")
i=int(input())
check=i
def isPalindrome(i):
	rev = 0
	while i > 0:
		rev = rev *10 + i%10 
		i = i//10

	if rev == check:
		print('yes')
	else:
		print('no')

#print(isPalindrome(i))
isPalindrome(i)
#Pesudo
#a=123
#b=a%10
#last_digit = 3
#a=a//10
#first_two = 12
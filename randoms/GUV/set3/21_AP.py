'''
Find the sum of an Arithmetic Progression till N terms given N,A,D.
Input Size : 1 <= N,A,D <= 100000
Sample Testcase :
INPUT
3 1 1
OUTPUT
6 

a = 3 (the first term)

d = 5 (the "common difference")

n is nth term

S = (n/2) × (2a + (n−1)d) 

'''

n,a,d = map(int,input().split())
S = 0
part_A = (n/2)
part_B = (2*a) + ((n-1)*d)
S = part_A*part_B
print(S)
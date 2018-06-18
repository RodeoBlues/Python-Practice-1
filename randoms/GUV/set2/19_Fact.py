# import unittest
i = int(input())
def factorial(i):
	if i == 0 or i == 1:
		return 1
	return i*factorial(i-1) #recursive

print(factorial(i))
# #Testcases
# class MyTest(unittest.TestCase):
#     def factorial(self):
#         self.assertEqual(factorial(1), 1)
#         self.assertEqual(factorial(6), 720)

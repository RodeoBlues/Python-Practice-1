a,b = map(int,input().split())
def evenBetweenIntervals(a,b):
	a+=1
	while a < b:
		if a%2 == 0:
			print(a,end=' ')
		a+=1

evenBetweenIntervals(a,b)

#1 10

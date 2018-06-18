a,b = map(int,input().split())
def oddBetweenIntervals(a,b):
	a+=1
	while a < b:
		if a%2 != 0:
			print(a,end=' ')
		a+=1

oddBetweenIntervals(a,b)

#1 10

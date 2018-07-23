loop = int(input())
in_list=[]
while loop>0:
	in_val = int(input())
	in_list.append(in_val)
	loop = loop-1
for i in sorted(in_list):
	print(i)

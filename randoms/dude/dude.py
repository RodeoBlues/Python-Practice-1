import os

#print(os.getcwd())

def dude():
	files = os.listdir()
	for file in files:
		print("Old file name" + file)
		print("New file name is" + str.strip(file,"0123456789"))
		os.rename(file,str.strip(file,"0123456789"))
	print("Files renamed sucessfully pls find out the MSG")

dude()
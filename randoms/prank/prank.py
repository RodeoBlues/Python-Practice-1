#!/bin/python
import os


def rename():
	#list files in the given dir
	dir_files = os.listdir("/home/vimal/Desktop/L/py/prank/prank")
	#print(dir_files)
	#Rename the fiels
	for file_name in dir_files:
		print("Old name of the file" + file_name)
		print("New name of the file" + str.strip(file_name,'1234567890'))
		os.rename(file_name,str.strip(file_name,'1234567890'))

rename()
import requests

def read_file():
	open_file = open("/home/dir/dir/text.txt")
	content_of_file = open_file.read()
	#print(content_of_file)
	open_file.close()
	check_profanity(content_of_file)

def check_profanity(file_content):
	dic = {'q' : file_content }
	URL = 'http://www.wdylike.appspot.com' #Entity to check the word or sentence is offensive or not
	r = requests.get(url= URL,params= dic)
	# print(r.text)
	if r.text == 'true':
		print("Offensive word found!")
	elif r.text == 'false':
		print("No offensive words!")
	else:
		print("Document scanned error")

read_file()

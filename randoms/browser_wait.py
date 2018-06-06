import webbrowser
import time

total_break = 3
break_count = 0

print("Started Time "+ time.ctime())
while break_count < total_break:
	time.sleep(5)
	print("Browser Opened")
	webbrowser.open("https://www.google.com")
	break_count = break_count + 1

print("Program Terminated")
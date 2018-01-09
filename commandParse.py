import os
import threading

plist = "list"
pbrowse = "browse"
psearch = "search"
popen = "open"
puser = "user"
pcompress = "compress"
pfeeling = "feeling"
pdir = "directory"
premove = "remove"
pdelete = "delete"
pcreate = "create"
pmake = "make"
pcal = "calendar"

def func_one(text):

	if pfeeling in text:
		os.system("espeak 'marvelous'")
		os.system("espeak 'fantastic'")

	if pdir in text:
		if pcreate in text or pmake in text:
			os.system("espeak 'creating directory'")
			mkdir = 'mkdir '
			arr = text.split()
			mkdir = mkdir+arr[2]
			os.system(mkdir)

		if premove in text or pdelete in text:
			os.system("espeak 'deleting directory'")	
			rmdir = 'rmdir '
			arr = text.split()
			rmdir = rmdir+arr[2]
			os.system(rmdir)


def func_two(text):

	if popen in text:
		os.system("espeak 'opening'")
		nautiluscmd = 'nautilus '
		if puser in text:
			userpath = nautiluscmd+'/home/boris'
			os.system(userpath)

	if plist in text:
		os.system("espeak 'listing'")
		os.system('ls')



def func_three(text):

	if 	pbrowse in text:
		os.system("espeak 'browsing'")
		os.system('python -m webbrowser -t "http://www.python.org"')

	if psearch in text:
		os.system("espeak 'searching for the file'")
		findcmd = 'find . -name "'
		arr = text.split()
		findcmd = findcmd+arr[1]+'*"'
		os.system(findcmd)		

def func_utilities(text):
	if pcal in text:
		cal = 'cal'
		os.system("espeak 'opening calendar'")
		os.system(cal)



def parse(text):
	t1 = threading.Thread(name='thread1', target=func_one, args=(text,))
	t2 = threading.Thread(name='thread2', target=func_two, args=(text,))
	t3 = threading.Thread(name='thread3', target=func_three, args=(text,))
	t4 = threading.Thread(name='thread4', target=func_utilities, args=(text,))

	t1.start()
	t2.start()
	t3.start()	
	t4.start()

	
	

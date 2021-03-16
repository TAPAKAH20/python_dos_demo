import subprocess

print('Trigger return code other than 1 and 0 in the subprocess')


proc = subprocess.Popen(["python3", "subproc.py"], stdin=subprocess.PIPE)
res = proc.communicate(input().encode('ASCII'))
poll = proc.poll()

while poll == 0 or poll == 1:
	print('Return code was', poll)
	proc = subprocess.Popen(["python3", "subproc.py"], stdin=subprocess.PIPE)
	res = proc.communicate(input().encode('ASCII'))
	poll = proc.poll()

print('Return code was', poll)
print("FLAG")
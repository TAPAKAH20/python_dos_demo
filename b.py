import subprocess

print('Trigger return code -6 in a subprocess')


proc = subprocess.Popen(["python3", "a.py"], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
res = proc.communicate(input().encode('ASCII'))
poll = proc.poll()

while poll != -6:
	print('Return code was', poll)
	proc = subprocess.Popen(["python3", "a.py"], stdin=subprocess.PIPE)
	res = proc.communicate(input().encode('ASCII'))
	poll = proc.poll()

print('Return code was', poll)
print("FLAG")
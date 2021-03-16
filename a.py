from ctypes import *

d = input()
try:
	d = float(d)
	a = c_double.from_param(d)

	print(a)
except Exception as e:
	print('Not a float')
	

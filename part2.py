# Part 2 of the Python Review lab.

def encode(x, y):
	if 1<y<250 and 500<x<1000:
		return(x*y)
	else:
		print("invalid input")
def prime (a):
	for i in range (2,a):
		if a % i ==0:
			return(False)
	return(True)

def decode(coded_message):
	for i in range(2,250):
		x= coded_message//i
		if 500<x<1000 and prime(x):
			return(x,i)
import random

mainfile = 'quotes.txt'
exclude = []

def file_length():
	with open(mainfile) as c:
		for i, l in enumerate(c):
			pass
	return i


def custom_random():
	while True:
		n = random.randint(0, file_length())
		if n in exclude:
			pass
		else:
			exclude.append(n)
			return n

def primary():
	for i in range(14):
		f = open(mainfile)
		quotes = f.readlines()
		f.close()
		print(str(i+1) + ". " + quotes[custom_random()].strip())
#		print(exclude)
#		print('')
#		print(file_length())


if __name__== '__main__':
	primary()


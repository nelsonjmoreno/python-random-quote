import random

#Defines primary quote file
mainfile = "quotes.txt"

#Obtains count of the number of quotes in quotes.txt
def file_length():
  with open(mainfile) as c:
    for i, l in enumerate(c):
      pass
  return i 

#Prints 2 random quotes
def primary():
  f = open(mainfile)
  quotes = f.readlines()
  f.close()
  n1 = random.randint(0, file_length())
  n2 = random.randint(0, file_length())
  if n2 == n1:
    next(n2)

  print(quotes[n1].strip())
  print(quotes[n2].strip())

if __name__== "__main__":
  primary()

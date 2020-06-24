import random

mainfile = "quotes.txt"

def file_length():
  with open(mainfile) as c:
    for i, l in enumerate(c):
      pass
  return i 

def primary():
  #print("Keep it logically awesome.")
  f = open(mainfile)
  quotes = f.readlines()
  f.close()
  n = random.randint(0, file_length())

  print(quotes[n])

if __name__== "__main__":
  primary()

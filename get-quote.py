import random

n = random.randint(0,13)

def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[n])


if __name__== "__main__":
  primary()

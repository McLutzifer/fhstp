
"""
Exercise 1:
    Console Input / Output

@author: Lukas Schumi (se201028)
"""

def isPrime(number):
  '''
  Funktion die untersucht, ob gegebener Input eine Primzahl ist. 
  '''
  prime = True
  for i in range(2, number):
    if number % i == 0:
      prime = False

  if prime == True:
    print (number, end=", ")


def checkInput(x):
  '''
  untersucht, ob Input ein Integer ist, oder zu einem gecastet werden kann
  '''
  while True:
    try:
      x = int(input())
    except ValueError:
      print("das ist keine Zahl. Bitte nochmal >> ")
    else:
      return x
      break

def main():
  startNumber = 1
  endNumber = 0

  print("Bitte zwei Zahlen eingeben.") 

  while startNumber > endNumber:
    print("Bitte erste Zahl eingeben >> ")
    startNumber = checkInput(startNumber)
    print("Bitte zweite Zahl eingeben >> ")
    endNumber = checkInput(endNumber)

    if startNumber > endNumber:
      print("Startnummer muss kleiner als Endnummer sein")


  print("Primzahlen zwischen {} und {} sind: ".format(startNumber, endNumber))
  for element in range(startNumber, endNumber+1):
    isPrime(element)


if __name__ == "__main__":
  main()

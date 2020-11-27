
"""
Exercise 3:
    Recursive calculation of the faculty

@author: Lukas Schumi (se201028)
"""

def faculty(n):
    '''
    Funktion nimmt Ganzzahl als input und ermittelt rekursiv die Fakultät

    '''
    if n == 1:
        return 1
    else:
        return n * faculty(n-1)


def main():

    while True:
        try:
            n = int(input("Bitte Number eingeben >> "))
            break    # bricht erst aus der Schleife, wenn ein int eingegeben wurde
        except ValueError:
            print("Bitte nur ganze zahlen eingeben!")

    print("Faktorielle von {} = {}".format(n, faculty(n)))
    
    # erstellt bzw updated ein txt File mit der Lösung, die oben in der print Funktion steht
    f = open("Exercise_Task_3.txt", "w")
    f.write("Faktorielle von {} = {}".format(n, faculty(n)))
    f.close()

if __name__ == "__main__":
  main()
  
  
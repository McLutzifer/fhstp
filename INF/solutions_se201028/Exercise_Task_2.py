
"""
Exercise 2:
    CommandLine Parameters 

@author: Lukas Schumi (se201028)
"""


def stringInput():
    string = input("Geben Sie eine einfache Gleichung ein, ein Bsp: 10 [+-x/] 2 >> ")
    while len(string.split(" ")) != 3:    #kontrolliert ob die eingegebene Gleichung aus drei Teilen besteht
       print("Die Eingabeform sollte wie folgt sein:\n<Zahl> <Operation> <Zahl>")
       string = input("Geben Sie eine Gleichung ein >>")

    string = string.replace(",", ".")
    val1, op, val2 = string.split(" ")

    return string, val1, op, val2


def checkInput(b, x, y):
    '''
    kontrolliert, ob die eingegebenen Werte numerisch sind
    '''
    try:
         x = float(x)
         y = float(y)
         return False
    except ValueError:
        print("Sie haben keine Zahlen eingegeben!")
        #print("Geben Sie eine einfache Gleichung ein, ein Bsp: 10 [+-x/] 2 >> ")
        #stringInput()
        return True


def method(string, op, val1, val2):
    error = False
    if op == "+":
        print ("Die Lösung für {} lautet:".format(string))
        print(val1 + val2)
    elif op == "-":
        print ("Die Lösung für {} lautet:".format(string))
        print(val1 - val2)
    elif op == "/":
        if val2 == 0:
            print("Division durch Null ist nicht erlaubt")
            error = True
        else:
            print ("Die Lösung für {} lautet:".format(string))
            print(val1 / val2)    
    elif op == "x" or op == "*":            
        print ("Die Lösung für {} lautet:".format(string))
        print(val1 * val2)            
    else:
        print("Geben Sie bitte eine gülte Rechenoperation ein\nMöglich sind <+>, <->, <*> und </>")
        error = True           
    return error


err = True
while err:
    x = True
    while x:
        # Schleife läuft bis Gleichung aus drei Teilen besteht und va1 und val2 Zahlen sind
        string, val1, op, val2 = stringInput()
        x = checkInput(x, val1, val2)
            
    val1 = float(val1)
    val2 = float(val2)
    
    err = method(string, op, val1, val2)



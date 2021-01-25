# Author: Lukas Schumi, se201028
"""
Uebungsblatt 3

Aufgabe 3
"""


class Wellnesscenter:

    def __init__(self, id_nr, name, balance, age):
        self.name = name
        self.balance = float(balance)
        self.id_nr = id_nr
        self.age = age
    
    def chargeCredit(self, amount):
        if amount < 5: 
            print("Mindestbetrag zum Aufladen: 5€")
        elif (self.balance + amount) > 200:
            print("Guthaben darf nicht mehr als 200€ betragen")
        else:
            self.balance += amount
            print("Sie haben {}€ aufgeladen! Aktuelles Guthaben: {}€".format(amount, self.balance))

    def bookService(self, extraService):
        """

        extra Service
        ----------
        'Service' wurde gestrichen, da sich der Preis nach dem Alter richtet
        Temporäres Guthaben eingerichtet, damit self.balance erst am Ende von bookService belastet wird
        Variable Tageskarte eingeführt, ohne Tageskarte kann man kein extraService dazubuchen

        """
        temp_balance = self.balance 
        Tageskarte = False
        
        if self.age >= 18:
            if temp_balance >= 25:
                temp_balance -= 25
                print("Tageskarte Erwachsene wurde aufgeladen.")
                Tageskarte = True
            else:
                print("Sie können sich diese Auswahl leider nicht leisten")
        elif self.age >= 12:
            if temp_balance >= 18:
                temp_balance -= 18
                print("Tageskarte Studierende wurde aufgeladen.")
                Tageskarte = True
            else:
                print("Sie können sich diese Auswahl leider nicht leisten")
        elif self.age < 12:
            if temp_balance >= 12:
                temp_balance -= 12
                print("Tageskarte Kinder wurde aufgeladen.")
                Tageskarte = True
            else:
                print("Sie können sich diese Auswahl leider nicht leisten")

        if Tageskarte == True:
            if extraService == 0:
                pass
            elif extraService == 1:
                if temp_balance >= 5:
                    temp_balance -= 5
                    print("Sauna wurde dazugebucht")
                else:
                    print("Zu wenig Guthaben")
            elif extraService == 2:
                if temp_balance >= 10:
                    temp_balance -= 10
                    print("Private SPA wurde dazugebucht")
                else:
                    print("Zu wenig Guthaben")
            else:
                print("Das ist kein Angebotener Service")
                print("Wählen Sie bitte zwischen '1' für Sauna, '2' für Private SPA, oder '0' für keinen extra Service")
                
            if temp_balance < 0:
                print("Sie können sich diese Auswahl leider nicht leisten")
            else:
                self.balance = temp_balance
                print("- aktueller Stand von {}: {}€".format(self.name, self.balance))

        
    def __str__(self):
        return f"Name: {self.name}, Verfügbares Guthaben: {self.balance}€"
    


def main():
    
    #Peter    
    p = Wellnesscenter(12, "Peter", 12, 32)
    print(p.balance)
    p.chargeCredit(4) 
    print(p.balance)
    p.bookService(2)
    print(p.balance)
    print("\n") # newline zur Übersicht

    #Laura
    l = Wellnesscenter(17, "Laura", 122, 12)
    l.bookService(2)
    print("\n")
    
    #Susanne
    s = Wellnesscenter(124, "Susanne", 150, 46)
    print(s)
    s.chargeCredit(42)
    s.bookService(0)
    print(s)
    print("\n")
    
    #Caroline
    c = Wellnesscenter(1, "Caroline", 0, 33)
    print(c)
    c.chargeCredit(7)
    c.bookService(2)
    print(c)
    print("\n")
    
    #Anton
    a = Wellnesscenter(42, "Anton", 199, 76)
    a.bookService(1)
    a.chargeCredit(10)
    print(a)
    print("\n")
    
    #Richard
    r = Wellnesscenter(64, "Richard", 199, 27)
    print(r)
    r.chargeCredit(100)
    print(r)
    r.bookService(7)
    
    print(r.bookService.__doc__)
if __name__ == '__main__':
    main()
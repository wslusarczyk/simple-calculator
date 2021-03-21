import functions

def userChoice():
    choice = int(input("Które działanie chcesz wykonać: \n"
                   "1) Dodawanie \n"
                   "2) Odejmowanie \n"
                   "3) Dzielenie \n"
                   "4) Mnożenie \n"
                   "5) Zakończ program \n"))
    return choice

def askUserForNumber():
    global numberOne, numberTwo
    numberOne = int(input("Podaj pierwszą liczbę "))
    numberTwo = int(input("Podaj drugą liczbę "))

choice = userChoice()

while choice != 5:
    if choice == 1:
        askUserForNumber()
        resultSum = functions.sum(numberOne, numberTwo)
        print("Wynik dodawania jest równy ", resultSum)
    elif choice == 2:
        askUserForNumber()
        resultSubtract = functions.subtract(numberOne, numberTwo)
        print("Wynik odejmowania jest równy", resultSubtract)
    elif choice == 3:
        askUserForNumber()
        while numberTwo ==0:
            print("Pamiętaj nie dziel przez 0!")
            askUserForNumber()
        resultDevsion = functions.divide(numberOne, numberTwo)
        print("Wynik dzielnia jest równy", resultDevsion)
    elif choice == 4:
        askUserForNumber()
        resultMultiply = functions.multiply(numberOne, numberTwo)
        print("Wynik mnożenia jest równy", resultMultiply)
    choice = userChoice()

print("Koniec programu")
# Pasos:
# definir las funciones que se necesitan: agregar, restar, multiplicar, dividir
# impromir opciones para el usuario
# pedir valores
# llamar a las funciones
# while loop hasta que el usuario quiera salir
def add(a, b):
    answer = a + b
    print("{} + {} = {}".format(str(a), str(b), str(answer)))

def sub(a, b):
    answer = a - b
    print("{} - {} = {}".format(str(a), str(b), str(answer)))

def mul(a, b):
    answer = a * b
    print("{} * {} = {}".format(str(a), str(b), str(answer)))

def div(a, b):
    answer = a / b
    print("{} / {} = {}".format(str(a), str(b), str(answer)))
def firstNumber():
    a = int(input("Enter first number: "))
    return a
def secondNumber():
    b = int(input("Enter second number: "))
    return b

while (True):
    print("""
    A. Addition
    B. Substraction
    C. Multiplication
    D. Division
    E. Exit
    """)
    choice = input("Choose an operation: ")
    choice = choice.lower()
    if choice == "a" or choice == "addition":
        add(firstNumber(), secondNumber())
    elif choice == "b" or choice == "substraction":
        sub(firstNumber(), secondNumber())
    elif choice == "c" or choice == "multiplication":
        mul(firstNumber(), secondNumber())
    elif choice == "d" or choice == "division":
        div(firstNumber(), secondNumber())
    elif choice == "e" or choice == "exit":
        print("You have exited the app")
        quit()
    else:
        print("Something goes wrong")
    



firstNumber = None
secondNumber = 0
operation = None
reset = True
result = 0
operationCalc = ["+", "-", "*", "/", "**"]
num = None

sum = 0

while True :
    if firstNumber == None :
        reset = True
        firstNumber = int(input ("Podaj pierwszą liczbę : "))
    else :
        reset = False
        num =  input ("Podaj działanie " + str(operationCalc) + " lub exit lub reset: ")
        if num == "exit" :
            break
        if num == "reset" :
            reset = True
            firstNumber = None
            continue
        if num == "+" :
            secondNumber = int (input("Podaj drugą liczbę : "))
            result = firstNumber + secondNumber
            firstNumber = result
            print(result)
            continue
        if num == "-" :
            secondNumber = int (input("Podaj drugą liczbę : "))
            result = firstNumber - secondNumber
            firstNumber = result
            print(result)
            continue
        if num == "*" :
            secondNumber = int (input("Podaj drugą liczbę : "))
            result = firstNumber * secondNumber
            firstNumber = result
            print(result)
            continue
        if num == "/" :
            secondNumber = int (input("Podaj drugą liczbę : "))
            result = firstNumber / secondNumber
            firstNumber = result
            print(result)
            continue
        if num == "**" :
            secondNumber = int (input("Podaj drugą liczbę : "))
            result = firstNumber ** secondNumber
            firstNumber = result
            print(result)
            continue



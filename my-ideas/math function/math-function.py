
file = open("math-function.txt","r")
mathFunction = file.read()
mathFunctionList = []

print(mathFunction)

x = input("Insert x:")
mathFunctionList = list(mathFunction)
for n,i in enumerate(mathFunctionList):
    if i == 'x':
        mathFunctionList[n] = str(x)

print(mathFunctionList)
index = 0
# Potencias
while index < len(mathFunctionList):
    if str(mathFunctionList[index]) == '^':
        mathFunctionList[index - 1] = str(int(mathFunctionList[index - 1])**int(mathFunctionList[index + 1]))
        del mathFunctionList[index]
        del mathFunctionList[index]
        index -= 1
    index += 1

index=0
#Multiplicacion y division
while index < len(mathFunctionList):

    if str(mathFunctionList[index]) == '.':
        mathFunctionList[index - 1] = str(int(mathFunctionList[index - 1]) * int(mathFunctionList[index + 1]))
        del mathFunctionList[index]
        del mathFunctionList[index]
        index -= 1

    elif str(mathFunctionList[index]) == '/':
        mathFunctionList[index - 1] = str(int(mathFunctionList[index - 1]) / int(mathFunctionList[index + 1]))
        del mathFunctionList[index]
        del mathFunctionList[index]
        index -= 1
    index+=1
index=0
#Suma y resta
while index < len(mathFunctionList):

    if str(mathFunctionList[index]) == '+':
        mathFunctionList[index - 1] = str(int(mathFunctionList[index - 1]) + int(mathFunctionList[index + 1]))
        del mathFunctionList[index]
        del mathFunctionList[index]
        index -= 1

    elif str(mathFunctionList[index]) == '-':
        mathFunctionList[index - 1] = str(int(mathFunctionList[index - 1]) - int(mathFunctionList[index + 1]))
        del mathFunctionList[index]
        del mathFunctionList[index]
        index -= 1
    index += 1
print("The result is: "+str(mathFunctionList[0]))




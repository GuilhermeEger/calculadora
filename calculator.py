#Calculadora simples para iniciar em Python.

firstNumber = 0
secondNumber = 0
result = 0
operator = ''
runMode = ''

firstNumber = int(input('Digite o primeiro número para o cálculo: '))
operator = input('Digite a operação desejada: ')
secondNumber = int(input('Digite o segundo número para o cálculo: '))

if operator == '+':
    result = firstNumber + secondNumber
elif operator == '-':
    result = firstNumber - secondNumber
elif operator == '/':
    result = firstNumber / secondNumber
elif operator == '*':
    result = firstNumber * secondNumber

print(result)





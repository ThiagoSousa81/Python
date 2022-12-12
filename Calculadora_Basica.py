#Calculadora Básica
srm = 0
while srm == 0:
        
    comand = str(input('Deseja qual operação(+, -, *, /)?\n'))
    result = 0
    if comand == '+':
        a = int(input('Primeiro valor: '))
        b = int(input('Segundo valor: '))
        result = a + b
        print("Resultado: ")
    elif comand == '-':
        a = int(input('Primeiro valor: '))
        b = int(input('Segundo valor: '))
        result = a - b
        print("Resultado: ")
    elif comand == '*':
        a = int(input('Primeiro valor: '))
        b = int(input('Segundo valor: '))
        result = a * b
        print("Resultado: ")
    elif comand == '/':
        a = int(input('Primeiro valor: '))
        b = int(input('Segundo valor: '))
        result = a / b
        print("Resultado: ")
    else:
        print('Não entendi o que você quiz dizer...')
    print(result)
    

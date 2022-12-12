#Método do valor de Delta
def delta(a, b, c):
    return (b ^ 2 - 4 * a * c)
rest = 0
while rest == 0:
    print('∆ = b²-4*a*c')
    a = int(input('Valor de a: '))
    b = int(input('Valor de b: '))
    c = int(input('Valor de c: '))
    print(delta(a, b, c))

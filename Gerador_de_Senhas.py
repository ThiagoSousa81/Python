import string, random
while True:
    size = int(input('Digite o tamanho: '))
    chars = string.ascii_uppercase + string.digits
    rnd = random.SystemRandom()
    print(''.join(rnd.choice(chars) for i in range(size)))


           

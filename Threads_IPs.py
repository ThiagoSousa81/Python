from threading import Thread

def carro(Piloto, speed):
    traget = 0
    while traget <= 100:
        traget += speed
        #time.sleep(5)
        print('\nPiloto: {} KM: {}'.format(Piloto, traget))


t_car1 = Thread(target=carro, args = ['Adam', 4.5])
t_car2 = Thread(target=carro, args = ['Leonard', 5])

t_car1.start()
t_car2.start()

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Socket pronto!')
host = 'localhost'
porta = 5432
mensagem = ' OII '

s.bind((host, porta))

while 1:
    dados, end = s.recvfrom(4096)
    
    if dados:
        print("Servidor Enviando msg...")
        s.sendto(dados + (mensagem.encode()), end)
        



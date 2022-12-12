import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Cliente Socket Criado com Sucesso!!!')
host = 'localhost'
porta = 5433
msg = 'Heloo Server!'
try:
    print('Cliente: ' + msg)
    s.sendto(msg.encode(), (host, 5432))
    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print('Servidor: ' + dados)
finally:
    s.close()
    

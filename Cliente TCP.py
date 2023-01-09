import socket
import sys
def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("Conexão falhou! \n" + e)
    finally:
        print("Socket criado com sucesso!")
        Host = "localhost"
        Porta = 5443
    try:
        s.connect((Host, int(Porta)))
        print("Conetado")
        s.shutdown(2)
    except socket.error as e:
        print(e)
main()
        
        
    


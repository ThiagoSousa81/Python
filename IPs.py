import ipaddress

ip = '0.0.0.0'

endereco = ipaddress.ip_address(ip)

#for i in range(5000):
endereco = endereco + 4294967295
print(endereco)

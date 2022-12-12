import hashlib
text = input('Digite o texto: ')
resultado = hashlib.md5(text.encode("ansi"))
print(resultado.hexdigest())

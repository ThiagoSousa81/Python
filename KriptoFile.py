import ctypes
#https://cleitonbueno.com/python-usando-bibliotecas-do-linux-com-ctypes/
atributo_ocultar = 0x02
retorno = ctypes.windll.kernel32.SetFileAttributesW('File1.py', atributo_ocultar)
if retorno:
    print('Arquivo ocultado')
else:
    print('Arquivo não oculto')

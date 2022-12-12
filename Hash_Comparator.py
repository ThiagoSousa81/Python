import hashlib
while True:
    text = input('Entre com o texto para hashear: ')
    hash1 = hashlib.new('MD5')
#    hash1.update(str(text))
    hash1 = hash1.hexdigest()
    print(hash1)
    

import phonenumbers
from phonenumbers import geocoder
while True:
    phone =  input('Digite número no formato: +551140028922 \n')
    phone_number = phonenumbers.parse(phone)
    print(geocoder.description_for_number(phone_number, 'pt'))



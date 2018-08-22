import base64
import os
import sys
import time

from cryptography.fernet import Fernet
def generate_master_key():
    my_key_file = "./mykey.key"
    if os.path.exists(my_key_file):
        with open(my_key_file, 'rb') as myfile:
            master_key = myfile.read()
    else:
        print("No se encontro una llave, se generara una nueva. Presiona cualquier tecla para continuar...")
        basura = input()
        master_key = Fernet.generate_key()
        with open(my_key_file, 'wb') as myfile:
            myfile.write(master_key)
    return master_key
    del master_key

data_enc = sys.argv[1]
key = generate_master_key()
cipher_suite = Fernet(key)
def encrypt(s):
    return cipher_suite.encrypt(base64.encodebytes(s.encode('utf-8')))
def decrypt(token):
    return base64.decodebytes(cipher_suite.decrypt(token))
	
in_selec = input('Para cifrar presiona 1 para desencriptar presiona 2')
if in_selec == '1':
    #input('Archivo a cifrar: ')
    with open(data_enc,'r') as g:
        s = g.read()
    with open(data_enc+'.enc','wb') as g:
        g.write(encrypt(s))

elif in_selec == '2':
    try:
        #data_enc = input('Archivo a descifrar: ')
        with open(data_enc,'rb') as g:
            data = decrypt(g.read())
        with open(data_enc[0:-4],'wb') as f:
            f.write(data)
        print(data)
        time.sleep(5.5)
    except:
        print("Error al desencriptar. LLave no valida")

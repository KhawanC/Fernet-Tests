import sys

from os import write
from cryptography.fernet import Fernet #Criptografia usada na minha aplicação
from teste1 import codes #mudar teste{} para a variável do seu arquivo //// Caso não haja valor para importação, comente esse linha

sys.path.append('.') #

def criarChave(): #função para gerar uma chave única
    chave = Fernet.generate_key()
    with open('secret.key', 'wb') as key_file:
        key_file.write(chave)

def carr_chave(): #função para ler a chave
    return open('secret.key', 'rb').read()

chave = carr_chave()

f1 = Fernet(chave)
f2 = Fernet(codes.chave)

var = int(input('''Você quer: 
[1] encriptar sua mensagem 
[2] decriptar sua mensagem

'''))

if var == 1: 
    message = sys.argv[1].encode() #segundo argumento da linha do terminal será a mensagem
    with open(sys.argv[2]+'.py', 'w') as encypted: #terceiro argumento será o nome da viriável, recomendo: (nome_genéricoX + .py)
        criarChave()
        messCifrada = f1.encrypt(message)
        encypted.write('class codes:'
        '\n    mensagem = ' + str(messCifrada) +'\n    chave = '+str(chave)) #Será criada uma classe para que os valores dos objetos sejam acessados posteriormente

if var == 2: 
   mess_data = codes.mensagem
   key = codes.chave
   decrypted_data = f2.decrypt(mess_data)    
   print(decrypted_data)
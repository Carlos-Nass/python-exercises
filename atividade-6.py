import random
import string

def gerar_senha(tamanho=12):
    
    letras_lower = string.ascii_lowercase
    letras_upper = string.ascii_uppercase
    digitos = string.digits
    simbolos = string.punctuation


    todos_caracteres = letras_lower + letras_upper + digitos + simbolos


    senha = ''.join(random.sample(todos_caracteres, tamanho))
    return senha

nova_senha = gerar_senha()
print(nova_senha)
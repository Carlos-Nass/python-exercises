import random

while True:
    
    num = random.randint(1, 9)
    
    chance = input("Adivinhe o número entre 1 e 9 (ou digite 'sair' para sair): ")
    
    if chance == "sair":
        break
        
    chance = int(chance)
    
    if chance < num:
        print("Tentativa < que o número!")
    elif chance > num:
        print("Tentativa > que o número!")
    else:
        print("Você acertou o número!")
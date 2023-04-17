
palavra = input("Digite uma palavra: ")

palavra = palavra.replace(" ", "").lower()

if palavra == palavra[::-1]:
    print("É um palíndromo :D")
else:
    print("Não é um palíndromo :C")
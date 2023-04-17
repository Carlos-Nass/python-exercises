nome_arq = "names.txt"
cont_names = {}

with open(nome_arq, "r") as arq:
    for linha in arq:
        nome = linha.strip()
        if nome in cont_names:
            cont_names[nome] += 1
        else:
            cont_names[nome] = 1

for nome, cont in cont_names.items():
    print(nome + ": " + str(cont))
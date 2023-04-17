def remove_dupli(lista):
    nova_lista = []
    for elemento in lista:
        if elemento not in nova_lista:
            nova_lista.append(elemento)
    return nova_lista

lista_original = [1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 8, 9, 9, 9]
nova_lista = remove_dupli(lista_original)
print(nova_lista)
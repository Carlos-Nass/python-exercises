
continuar = True

while continuar:
    jogador1 = input("Jogador 1, escolha pedra, papel ou tesoura: ").lower()
    jogador2 = input("Jogador 2, escolha pedra, papel ou tesoura: ").lower()

    if jogador1 == jogador2:
        vencedor = None
    elif jogador1 == "pedra" and jogador2 == "tesoura":
        vencedor = "jogador 1"
    elif jogador1 == "tesoura" and jogador2 == "papel":
        vencedor = "jogador 1"
    elif jogador1 == "papel" and jogador2 == "pedra":
        vencedor = "jogador 1"
    else:
        vencedor = "jogador 2"

    if vencedor is None:
        print("Empate!")
    else:
        print(f"{vencedor} venceu!")

    resposta = input("Quer jogar novamente? (s ou n): ")
    while resposta not in ["sim", "s", "n", "não"]:
        resposta = input("Resposta inválida. Quer jogar novamente? (s ou n): ")
    if resposta == "n":
        continuar = False
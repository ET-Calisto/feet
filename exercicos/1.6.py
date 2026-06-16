# 6 - Jogo do Pedra, Papel, Tesoura. Solicite as escolhas do jogador 1 e do jogador 2
# (“pedra”, “papel” ou “tesoura”). Use condicionais para determinar quem ganhou:
# • Pedra ganha de tesoura, tesoura ganha de papel, papel ganha de pedra.
# • Exiba uma mensagem como “Jogador 1 venceu!” ou “Empate!”.

import random


opcoes = ["pedra", "papel", "tesoura"]


print("--- Jogo Pedra, Papel e Tesoura ---")
jogador = input("Escolha pedra, papel ou tesoura: ").lower()
computador = random.choice(opcoes)


print(f"O computador escolheu: {computador}")


if jogador not in opcoes:
    print("Jogada inválida! Tente novamente.")
elif jogador == computador:
    print("Empate!")
elif (jogador == "pedra" and computador == "tesoura") or \
     (jogador == "papel" and computador == "pedra") or \
     (jogador == "tesoura" and computador == "papel"):
    print("Você venceu!")
else:
    print("Você perdeu!")




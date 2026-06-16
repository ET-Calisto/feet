# 4 – Solicite ao usuário um superpoder entre três opções: “força”, “velocidade” ou “voo”.
# Use estruturas de decisão para exibir uma frase que diga qual super-herói você seria com
# base na escolha:
# • Se escolher “força”: exiba “Você seria o Hulk!”;
# • Se escolher “velocidade”: exiba “Você seria o Flash!”;
# • Se escolher “voo”: exiba “Você seria o Flash!”.


superpoder = int(input("escolha um superpoder: 1.força, 2.velocidade ou 3.voo"))
if superpoder ==1:
    print("Você seria o Hulk!")
elif superpoder == 2:
    print("Você seria o Flash!")
elif superpoder == 3:
    print("Você seria o Flash!")
else:
    print("Talvez um neuronio seria mais util pra vc que um superpoder")

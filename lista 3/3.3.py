# 3 – Faça um programa que funcionará como um cadastro de códigos de produtos de uma
# loja de roupas. O cadastro deve ser realizado em uma lista com até 10 códigos. Inicialize
# os elementos da lista com -1, este valor indicará que o elemento está vago para o
# cadastro. Seu programa deve ter um menu com uma opção para cadastrar um novo
# código (apenas um por vez) e para listar os todos códigos cadastrados (não devem ser
# listados códigos não cadastrados). Deve-se também informar se houve sucesso ou falha
# na hora de cadastrar um novo código e também não deve ser possível cadastrar um
# produto com o código -1. No momento do cadastro, não deve ser informado o valor do
# índice, esse deve ser “calculado” automaticamente. Veja como deve ser criado o menu:
# Menu
# ----
# 1 – Cadastrar
# 2 – Listar todos
# 0 – Sair
c=0
import os
os.system('cls'if os.name=="nt" else "clear")
print("Cadastro de códigos de produtos de uma loja de roupas")
cadastro_de_codigos_de_produtos = [-1]*10
resposta_usuario=1
while resposta_usuario!=0:
    resposta_usuario = int(input(""" Menu
 ----
 1 – Cadastrar
 2 – Listar todos
 0 – Sair
     """))
    if resposta_usuario==1:
        if c<=10:
            print("cadastre um novo codigo")
            sla=int(input("Escreva o codigo"))
            cadastro_de_codigos_de_produtos[c]=sla
            c=c+1
        else:
            print("Não é possivel cadastrar novo codigo :(")
    if resposta_usuario==2:
        print("Lista codigos de produtos")
        print(cadastro_de_codigos_de_produtos)
    if resposta_usuario!=0 and resposta_usuario!=1 and resposta_usuario!=2:
        print("Resposta inexperada :(")
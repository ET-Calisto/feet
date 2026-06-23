# 3 – Faça um programa que exiba na tela a contagem iniciando no número 1 e indo até um
# número informado pelo usuário. Considere que a contagem pode ser até um número
# positivo ou até um número negativo.
n = int(input("escreva um numero"))
c=1
#numero positivo
if n>0:
    while c<n:
        print(c)
        c=c+1
else:
#numero negativo
    while c>n:
        print(c)
        c=c-1
# 4 – Implemente um algoritmo que exiba na tela os números pares de 0 até um número
# digitado pelo usuário. Dica: você pode utilizar o operador módulo (%) ou contar de 2 em 2
n2=int(input("digite um numero"))
n1=0
if n2>0:
    while n1<n2:
        n1=n1+2
        print(n1)
else:
    while n1>n2:
        n1=n1-2
        print(n1)

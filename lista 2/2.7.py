# 7 – Implemente um programa para calcular sua média final em uma determinada unidade
# curricular. O programa deve solicitar ao usuário a quantidade de notas, o valor para cada
# uma das notas e exibir, ao final, a média aritmética simples e informar se o(a) estudante
# está Aprovado ou Reprovado. Considere que a média mínima para a aprovação é 6.
n1=int(input("digite sua nota"))
n2=int(input("digite sua nota"))
n3=int(input("digite sua nota"))

ma=n1+n2+n3/3

if ma<6:
    print("reprovado")
else:
    print("Você foi aprovado! Parabens!")
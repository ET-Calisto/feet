# 2 – Crie um programa que leia 4 notas de um(a) determinado(a) estudante. Após a leitura
# de todas notas, exiba a média aritmética simples e a situação final (aprovado(a) ou
# reprovado(a))
aluno =[""]*4
i=0
while i<4:
    sla=int(input("qual a nota?"))
    aluno[i]=sla
    i=i+1

media=sum(aluno)/4
print(media)
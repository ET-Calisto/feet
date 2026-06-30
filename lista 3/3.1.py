# 1 - Implemente um programa com um cadastro de idades de 6 alunos utilizando lista. O
# programa deve solicitar as idades dos 6 alunos. Após informar todas as idades, deve-se
# apresentar apenas as idades que forem maiores ou iguais a 16.
cadastrodeidades = [""]*6
i=0
while i<6:
    sla=int(input("quantos anos o aluno tem?"))
    cadastrodeidades[i]=sla
    i=i+1

i=0
while i<6:
    if cadastrodeidades[i]>=16:
        print(cadastrodeidades[i])
    i=i+1

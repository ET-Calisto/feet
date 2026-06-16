# 7 - Qual é o seu Signo? Solicite o dia e o mês de nascimento do usuário. Com base nesses valores, use condicionais para determinar o signo.
print("Escreva em algorismos")
d = int(input("Qual dia você nasceu? "))
m = int(input("Qual mês você nasceu? "))

if m == 1 and d <=19 or m ==12 and d >= 22:
    print("Você é de capricornio!")
    # Capricórnio: 22 de dezembro a 19 de janeiro
elif m ==1 and d >=21 or m == 2 and d >= 1 and d <=18:
    print("Você é de Aquario!")
    # Aquário: 20 de janeiro a 18 de fevereiro
elif m ==2 and d >= 19 or m ==3 and d <=20:
    print("Gluup glup glup gluuuup!")
    # Peixes: 19 de fevereiro a 20 de março
elif m==3 and d>=21 or m==4 and d<=19:
    print("Você é de Áries!")
    # Áries: 21 de março a 19 de abril
elif m==4 and d>=20 or m==5 and d<=20:
    print("Você é de Touro!") 
    # Touro: 20 de abril a 20 de maio
elif m==5 and d>=21 or m==6 and d<=20:
    print("Você é de Gêmeos!") 
    # Gêmeos: 21 de maio a 20 de junho
elif m==6 and d>=21 or m==7 and d<=22:
    print("Você é de Câncer!") 
    # Câncer: 21 de junho a 22 de julho
elif m==7 and d>=23 or m==8 and d<=22:
    print("Você é de Câncer!") 
    # Leão: 23 de julho a 22 de agosto
elif m==8 and d>=23 or m==9 and d<=22:
    print("Você é de Virgem!") 
    # Virgem: 23 de agosto a 22 de setembro
elif m==9 and d>=23 or m==10 and d<=22:
    print("Você é de Libra!") 
    # Libra: 23 de setembro a 22 de outubro
elif m==10 and d>=23 or m==11 and d<=21:
    print("Você é de Escorpião!") 
    # Escorpião: 23 de outubro a 21 de novembro
elif m==11 and d>=22 or m==12 and d<=21:
    print("Você é de iiirrrrí!") 
    # Sagitário: 22 de novembro a 21 de dezembro

else:
    print("ERROR")
#1  Solicite o valor total de uma compra. Se o valor for maior ou igual a 100, exiba "Você
#ganhou um cupom de desconto!". Caso contrário, exiba "Continue comprando para
#ganhar um cupom de desconto!".


valortotal = int(input("Escreva o valor total da compra: "))
if valortotal >= 100:
    print("Você recebeu cupom de desconto!")
else:
    print("Continue comprando para ganhar um cupom de desconto!")
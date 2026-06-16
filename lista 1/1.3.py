# 3 – Construa um algoritmo que solicite o nome de usuário e a senha. Se o nome de
# usuário for igual a "admin" e a senha for igual a "12345", exiba "Login bem-sucedido".
# Caso contrário, exiba "Nome de usuário ou senha incorretos".


senhaverdadeiraultrasecreta = 12345
usuarioverdadeiroultrasecreto = "admin"
nomedeusuario = input("Insira nome de usuario: ")
senha = int(input("Insira senha"))
if nomedeusuario == usuarioverdadeiroultrasecreto and senha == senhaverdadeiraultrasecreta:
    print("Login bem-sucedido!")
else:
    print("Nome de usuário ou senha incorretos")
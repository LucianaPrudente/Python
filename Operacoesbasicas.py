"""a= 5
print(a)
print("O valor é:", a)
print("O valor é:%i" %a)
print("O valor é:" + str(a))

b= 7.5
print("Concatenando Decimal:",b )
print("Concatenando Decimal: %.3f", b)
print("Concatenando Decimal:" + str(b) )

c= "Me diga algo bom"
print("Concatenando String:", c)
print("Concatenando String: %s" %c)
print("Concatenando String:" + str(c))
"""

print ("Programa 2")

login = input ("Login: ")
senha = str(input ("Senha: "))

print("O usuário informado foi: %s e a senha informada foi: %s" %(login,senha))
senha_cadastrada = "sim"

if(senha=="sim"):
    print("Você digitou SIM")
else:
    if(senha=="nao"):
        print("Você digitou NÃO")
    else:
        print("A senha inserida não possui nenhum registro de cadastro.")

"""
if (senha == senha_cadastrada):
    print("O segredo é: I love you too!")
else:
     senha = input ("Senha inválida! Insira novamente: ")   
elif (senha!= "0"):
    print("Sorry! Try again")
"""

"""
print(10+10)
print("soma composta", 1+(1+1))
print(10-5)
print(10/6)
print("Divisão por arredondamento do inteiro", 10//6)
print("div de 3 e 2: ", 3%2)
print("div de 4 e 2: ", 4%2)
print("div de um float:", 7%3.1)
"""

"""
num1 = float(input("num1: "))
num2 = float(input("num2: "))

divisao = num1/num2

print(num1, "dividido por", num2, "é", divisao)

resto = num1%num2

print("o resto de", num1, "por", num2, "é", resto )
"""

"""
print("A raiz quadrada de 81 é:", 81**(1/2))
a=5
b=5
c=1
print(a==b)
print(a==c)
print(a==b) or (a!=b)
print(a!=b) and (a!=c)
print(a==b) and (a!=c)
"""


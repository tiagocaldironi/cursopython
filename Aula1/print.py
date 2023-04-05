'''
Comentários com várias linhas
data
autor
objetivo

'''

#imprimir:
# O Tiago tem 34 anos e mora em Hortolandia

nome = str(input("Digite o nome: "))
idade = int(input("Digite a idade: "))
cidade = str(input("Digite a cidade: "))

if nome[-1] in('a','e'):
    genero='A'
else:
    genero="O"



saida = f'{genero} {nome.capitalize()} tem {idade} anos e mora em {cidade}'

print(saida)

mensagem = 'eu Adoro Comida Caseira'

print(mensagem.capitalize().replace("adoro","não curto").upper().lower().capitalize().replace("não curto","adoro"))


for numero in range(1,200):
    print(numero)

for numero in range(1,300,2):
    print(numero)

for numero in range(1,300):
    if numero%2==0:
        print(numero)



compra_comfirmada = True
mensagem_compra = "A compra no valor de 20,90 foi efetuada"
email= "tiago.caldironi@gmail.com"
tentativas_envio = 3


for tentativa in range(1,tentativas_envio):
    if compra_comfirmada:
        print(f'Destinatário: {email}')
        print(mensagem_compra.capitalize())
        break
    elif compra_comfirmada == False:
        print("A Compra não foi confirmada")
    else:
        print("Falha no envio")



tabuada = 11

for t in range(1,tabuada):
    for n in range(1,tabuada):
        print( f' {t} x {n} = ' + str(n*t)  )



manchete = "Fantastico"
output = ''

for texto in (manchete):
        output = output + texto + ' '

print(output.upper())



colunas = 7
linhas = 7
simbolo ='@'

for c in range(1,colunas):
    for l in range(1,linhas):
        print(simbolo,end='')
    print()   



def soma():
    numero1 = 10
    numero2 = 20
    calculo = numero1 + numero2
    print(f'O valor do calculo resulta em {calculo}')


soma()

def soma_return():
    numero2 = 10
    numero3 = 40
    calculo = numero2 + numero3
    return calculo

print('O resultado do calculo com retorno é:' + str(soma_return()))



def soma_numeros(*numeros):
    soma = 0
    for i in numeros:
        soma = soma + i
    return soma

x = soma_numeros(1,2,3,5,8,13)

print(str(x))


def fcarro(**dados):
    return dados

print(fcarro(Marca='Hyunday',cor='Branco',motor='1.0'))
print(fcarro(Marca='Fiat',cor='Azul'))



import math

print(math.factorial(56))



cidades = ['São Paulo','Salvador','Curitiba']

cidades.append('Manaus')
cidades.append('Florianópolis')

cidades.sort()

print(cidades)



cores =['azul','amarelo','vermelho','roxo']
sair = 0

def verifica_estoque(cor,estoque):
    if cor in estoque:
        return 'sim'
    else:
        return 'não'
    

while sair == 0:
    cor = input('Digite a cor que deseja: ')
    print(verifica_estoque(cor.lower(),cores))
    sair = int(input('Para sair digite 1: '))


aluno = {'nome': 'Tiago','idade':16,'sexo':'M','Nacionalidade':'Brasileira'}

print(aluno['nome'],aluno['Nacionalidade'])

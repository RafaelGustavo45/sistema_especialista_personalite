from opcoes import selecao
from tecnicas import validar
from tecnicas import soma_resposta

#importando
print("sistema especialista de teste de personalidade \n")
print("arquivo leia-me nos arquivos 'leia_me.pdf'")
print("selecione uma das opções \n")
print("2- teste de qual minion voce é \n")
print("3- teste de voce seria um bom lider? \n")
print("4- teste voce é uma pessoa dramatica? \n")
print("5- teste voce é popular")

#print(soma_resposta(["a","b","c"],[10,20,30],"b")) ok

escolha = int(input("digite: "))

selecao(escolha)
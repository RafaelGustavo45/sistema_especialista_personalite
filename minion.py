def teste2():
  print("teste de qual minion voce é ")
  print("link: https://www.youtube.com/watch?v=Hx7UIsZpp2c")
  soma = 0
  from tecnicas import validar
  from tecnicas import soma_resposta
  valores_permitidos = ["a", "b", "c", "d", "e"]
  i = False
  while i == False:
    print("1- escolha um objeto")
    print("A) bazuka")
    print("B) ukelele")
    print("C) rolo de papel higienico")
    print("D) tacos de golfe")
    print("E) ursinho de pelucia")
    res = str(input("selecione: "))
    res = res.lower()
    i = validar(valores_permitidos, res)
    if i == True:
      soma += soma_resposta(valores_permitidos, [0, 20, 40, 10, 30], res)
    else:
      print("fora do escopo, repetindo")
  #if escolha == "a":
  #  soma += 0
  #elif escolha == "b":
  #  soma += 20
  #elif escolha == "c":
  #  soma += 40
  #elif escolha == "d":
  #  soma += 10
  #elif escolha == "e":
  #  soma += 30
  i = False
  while i == False:
    print(
      "2- qual é a atividade que voce mais gosta de fazer com amigos / familia"
    )
    print("A) sair")
    print("B) partir para nos aventurar")
    print("C) jogar jogos/videogame")
    print("D) fazer compras")
    print("E) praticar esportes")
    res = str(input("selecione: "))
    res = res.lower()
    i = validar(valores_permitidos, res)
    if i == True:
      soma += soma_resposta(valores_permitidos, [20, 40, 0, 30, 10], res)
    else:
      print("fora do escopo, repetindo")

    #if escolha == "a":
    #soma += 20
  #elif escolha == "b":
  #  soma += 40
  #elif escolha == "c":
  #  soma += 0
  #elif escolha == "d":
  #  soma += 30
  #elif escolha == "e":
  #  soma += 10
  i = False
  while i == False:
    print("3- o objetivo da sua vida é ser")
    print("A) honrado")
    print("B) feliz")
    print("C) inteligente")
    print("D) famoso")
    print("E) amado")
    res = str(input("selecione: "))
    res = res.lower()
    i = validar(valores_permitidos, res)
    if i == True:
      soma += soma_resposta(valores_permitidos, [10, 30, 0, 20, 40], res)
    else:
      print("fora do escopo, repetindo")

  #continuar daqui
  #if escolha == "a":
  #  soma += 10
  #elif escolha == "b":
  #  soma += 30
  #elif escolha == "c":
  #  soma += 0
  #elif escolha == "d":
  #  soma += 20
  #elif escolha == "e":
  #  soma += 40
  i = False
  while i == False:
    print("4- escolha um estilo de cabelo")
    print("A) chuquinha no meio do cabelo")
    print("B) dividido no meio")
    print("C) nenhum deles")
    print("D) arrepiado")
    print("E) careca")
    escolha = str(input("selecione: "))
    escolha = escolha.lower()
    i = validar(valores_permitidos, res)
    if i == True:
      soma += soma_resposta(valores_permitidos, [10, 0, 20, 40, 30], res)
    else:
      print("fora do escopo, repetindo")
  #if escolha == "a":
  #  soma += 10
  #elif escolha == "b":
  #  soma += 0
  #elif escolha == "c":
  #  soma += 20
  #elif escolha == "d":
  #  soma += 40
  #elif escolha == "e":
  #  soma += 30
  i = False
  while i == False:
    print("5- oque voce mais odeia")
    print("A) regras ")
    print("B) esperar")
    print("C) ser zuado / me sentir desonrado")
    print("D) bullying")
    print("E) estudar")
    escolha = str(input("selecione: "))
    escolha = escolha.lower()
    i = validar(valores_permitidos, res)
    if i == True:
      soma += soma_resposta(valores_permitidos, [20, 0, 10, 40, 30], res)
    else:
      print("fora do escopo, repetindo")
  #if escolha == "a":
  #  soma += 20
  #elif escolha == "b":
  #  soma += 0
  #elif escolha == "c":
  #  soma += 10
  #elif escolha == "d":
  #  soma += 40
  #elif escolha == "e":
  #  soma += 30
  i = False
  while i == False:
    print("6- escolha sua comida favorita")
    print("A) qualquer fast food ")
    print("B) sorvete")
    print("C) banana")
    print("D) doces")
    print("E) gelatina")
    escolha = str(input("selecione: "))
    escolha = escolha.lower()
    i = validar(valores_permitidos, res)
    if i == True:
      soma += soma_resposta(valores_permitidos, [30, 10, 0, 40, 20], res)
    else:
      print("fora do escopo, repetindo")
    #if escolha == "a":
    #  soma += 30
  #elif escolha == "b":
  #  soma += 10
  #elif escolha == "c":
  #  soma += 0
  #elif escolha == "d":
  #  soma += 40
  #elif escolha == "e":
  #  soma += 20
  i = False
  while i == False:
    print("7- como voce se descreveria em uma palavra")
    print("A) carinhoso")
    print("B) brincalhão")
    print("C) animado")
    print("D) mandão")
    print("E) infantil")
    escolha = str(input("selecione: "))
    escolha = escolha.lower()
    i = validar(valores_permitidos, res)
    if i == True:
      soma += soma_resposta(valores_permitidos, [0, 20, 40, 10, 30], res)
    else:
      print("fora do escopo, repetindo")
  #if escolha == "a":
  #  soma += 0
  #elif escolha == "b":
  #  soma += 20
  #elif escolha == "c":
  #  soma += 40
  #elif escolha == "d":
  #  soma += 10
  #elif escolha == "e":
  #  soma += 30
  i = False
  while i == False:
    print(
      "8- se voce fosse um minion, oque voce faria para se libertar do gru")
    print("A) iria conversar com todos para buscar ideias")
    print("B) bolaria um plano infalivel para isso")
    print("C) descobriria a forma certa de chegar a liberdade")
    print("D) faria algo tao louco que ele nunca esperaria")
    print("E) amaria a revolução sendo um lider minion")
    escolha = str(input("selecione: "))
    escolha = escolha.lower()
    i = validar(valores_permitidos, res)
    if i == True:
      soma += soma_resposta(valores_permitidos, [40, 0, 10, 30, 20], res)
    else:
      print("fora do escopo, repetindo")
  #if escolha == "a":
  #  soma += 40
  #elif escolha == "b":
  #  soma += 0
  #elif escolha == "c":
  #  soma += 10
  #elif escolha == "d":
  #  soma += 30
  #elif escolha == "e":
  #  soma += 20
  i = False
  while i == False:
    print("9- alguem gritou com voce do nada, oque voce faz?")
    print("A) mostro para ele que é inapropriado e sigo a vida")
    print("B) respondo levantando a voz, quem mandou?")
    print("C) tento ignorar, não se discute com irracionalidade")
    print("D) depende da situação, mas vou sair por cima")
    print("E) tento entender o porque a pessoa estava brava")
    escolha = str(input("selecione: "))
    escolha = escolha.lower()
    i = validar(valores_permitidos, res)
    if i == True:
      soma += soma_resposta(valores_permitidos, [10, 30, 0, 20, 40], res)
    else:
      print("fora do escopo, repetindo")
  #if escolha == "a":
  #  soma += 10
  #elif escolha == "b":
  #  soma += 30
  #elif escolha == "c":
  #  soma += 0
  #elif escolha == "d":
  #  soma += 20
  #elif escolha == "e":
  #  soma += 40
  i = False
  while i == False:
    print("10- escolha uma frase")
    print("A) não seja muito legal, vão se aproveitar de voce")
    print("B) coragem é como um musculo, cresce com o uso")
    print("C) se não gosta de como as coisas estão, mude-as")
    print("D) errado é errado, mesmo que todo mundo faça isso")
    print("E) faça que respeitem sua inteligencia")
    escolha = str(input("selecione: "))
    escolha = escolha.lower()
    i = validar(valores_permitidos, res)
    if i == True:
      soma += soma_resposta(valores_permitidos, [40, 30, 20, 10, 0], res)
    else:
      print("fora do escopo, repetindo")
  #if escolha == "a":
  #  soma += 40
  #elif escolha == "b":
  #  soma += 30
  #elif escolha == "c":
  #  soma += 20
  #elif escolha == "d":
  #  soma += 10
  #elif escolha == "e":
  #  soma += 0

  print("calculando o resultado")

  if (soma >= 0 and soma <= 70):
    print("voce é o minion dave \n")
    print(
      "voce tirou dave, o minion. Seus traços de personalidade são os seguintes: gentil, carinhoso, engraçado, animado, fiel, aventureiro e amoroso"
    )
    #colocar descrição de cada um
  elif (soma > 70 and soma <= 160):
    print("voce é o minion kevin \n")
    print(
      "voce ritou kevil, o minion, seus traços de personalidade são: calmo, lider, casual, ativo, mandão, carinhoso, compreensivo, e um tanto serio"
    )
  elif (soma > 160 and soma <= 230):
    print("voce é o minion stuart \n")
    print(
      "voce tirou stuart, o minion. Seus traços de personalidade são brincalhão, especial, honesto, atraente, sincero, tranquilo, diferente, original, incessante!"
    )
  elif (soma > 230 and soma <= 320):
    print("voce é o minion bob \n")
    print(
      "voce tirou o bob, o minion. Seus traços de personalidade são: adoravel, otimista, danadinho, infantil, sortudo, unico, e um tanto imaturo"
    )
  else:
    print("voce é o minion jerry \n")
    print(
      "voce tirou Jerry, o minion. Seus traços de personalidade sao: sensivel, assustado, animado, confuso, carinhoso e artistico"
    )

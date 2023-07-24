def teste4():
  print("teste de dramatico ")
  print("\n")
  from tecnicas import validar
  from tecnicas import soma_resposta
  valores_permitidos = ["a", "b", "c"]
  soma = 0
  i = False
  while i == False:
    print("link: https://www.youtube.com/watch?v=gCEp-xeLxfc")
    print("1-voce já chorou alguma vez no trabalho/escola?")
    print("A) nao")
    print("B) quase ocorreu")
    print("C) sim")
    res = str(input())
    res = res.lower()
    i = validar(valores_permitidos, res)
    if i == True:
      soma += soma_resposta(valores_permitidos, [0, 10, 20], res)
    else:
      print("fora do escopo, repetindo")
    #if i == True:
    #  if res == "a":
    #    soma += 0
    #  elif res == "b":
    #    soma += 10
    #  elif res == "c":
    #    soma += 20
    #else:
    #  print("fora do escopo, repetindo")

  i = False
  while i == False:
    print("2-voce já foi para o hospital para descobrir que não tinha nada?")
    print("A) sim")
    print("B) não")
    print("C) não lembro")
    res = str(input())
    res = res.lower()
    i = validar(valores_permitidos, res)
    if i == True:
      soma += soma_resposta(valores_permitidos, [20, 0, 10], res)
    else:
      print("fora do escopo, repetindo")
    #if i == True:
    #  if res == "a":
    #    soma += 20
    #  elif res == "b":
    #    soma += 0
    #  elif res == "c":
    #    soma += 10
    #else:
    #  print("fora do escopo, repetindo")

  i = False
  while i == False:
    print(
      "3-seu celular toca 1h da manhã, oque voce acha ser o objetivo da ligação?"
    )
    print("A) alguem precisa da minha ajuda")
    print("B) alguem morreu")
    print("C) sei lá")
    res = str(input())
    res = res.lower()
    i = validar(valores_permitidos, res)
    if i == True:
      soma += soma_resposta(valores_permitidos, [10, 20, 0], res)
    else:
      print("fora do escopo, repetindo")
    #if i == True:
    #if res == "a":
    #  soma += 10
    #elif res == "b":
    #  soma += 20
    #elif res == "c":
    #  soma += 0

  i = False
  while i == False:
    print(
      "4-você ve um calombo estranho atras do seu braço, oque voce acha que é?"
    )
    print("A) sei lá, marco uma consulta no médico")
    print("B) vou morrer de cancer")
    print("C) assumo algo ruim que precisa ser investigado")

    res = str(input())
    res = res.lower()
    i = validar(valores_permitidos, res)
    if i == True:
      soma += soma_resposta(valores_permitidos, [0, 20, 10], res)
    else:
      print("fora do escopo, repetindo")
    #if i == True:
    #  if res == "a":
    #    soma += 0
    #  elif res == "b":
    #    soma += 20
    #  elif res == "c":
    #    soma += 10
    #else:
    #  print("fora do escopo, repetindo")

  i = False
  while i == False:
    print(
      "5- seu amor esqueceu da data de seu aniversario, você o acusa de não o amar mais?"
    )
    print("A) não tenho certeza, talvez")
    print("B) não, provavelmente só esqueceu")
    print("C) Claro, como esquecer meu aniversario!?")

    res = str(input())
    res = res.lower()
    i = validar(valores_permitidos, res)
    if i == True:
      soma += soma_resposta(valores_permitidos, [10, 0, 20], res)
    else:
      print("fora do escopo, repetindo")
    #if i == True:
    #  if res == "a":
    #    soma += 10
    #  elif res == "b":
    #    soma += 0
    #  elif res == "c":
    #    soma += 20
    #else:
    #  print("repetindo, fora do escopo")

  i = False
  while i == False:
    print("6- voce está saindo com alguem por um tempo, e ele(a) não avança?")
    print("A) imagina que deve ser gay/lesbica, e termico com ele(a)")
    print("B) imagino que esta se guardando para o momento certo")
    print("C) pergunto na cara se me acha atraente ou não?")

    res = str(input())
    res = res.lower()
    i = validar(valores_permitidos, res)
    if i == True:
      soma += soma_resposta(valores_permitidos, [20, 0, 10], res)
    else:
      print("fora do escopo, repetindo")
    #if i == True:
    #  if res == "a":
    #    soma += 20
    #  elif res == "b":
    #    soma += 0
    #  elif res == "c":
    #    soma += 10
    #else:
    #  print("fora do escopo, repetindo")

  i = False
  while i == False:
    print("7- voce vê seu namorado(a) na rua com alguem do sexo oposto, voce:")
    print("A) passo por eles e dou um oi")
    print("B) na hora sigo minha vida, confronto depois")
    print("C) confronto na hora")

    res = str(input())
    res = res.lower()
    i = validar(valores_permitidos, res)
    if i == True:
      soma += soma_resposta(valores_permitidos, [0, 10, 20], res)
    else:
      print("fora do escopo, repetindo")
    #if i == True:
    #  if res == "a":
    #    soma += 0
    #  elif res == "b":
    #    soma += 10
    #  elif res == "c":
    #    soma += 20
    #else:
    #  print("fora do escopo, repetindo")

  i = False
  while i == False:
    print(
      "8- voce já gritou com um atendente por ter um voo/onibus cancelado?")
    print("A) sim")
    print("B) nao")
    print("C) não gritar, mas tivemos 'um papo'")

    res = str(input())
    res = res.lower()
    i = validar(valores_permitidos, res)
    if i == True:
      soma += soma_resposta(valores_permitidos, [20, 0, 10], res)
    else:
      print("fora do escopo, repetindo")
    #if i == True:
    #  if res == "a":
    #    soma += 20
    #  elif res == "b":
    #    soma += 0
    #  elif res == "c":
    #    soma += 10
    #else:
    #  print("fora do escopo, repetindo")

  i = False
  while i == False:
    print("9- voce já esperneou em uma consulta medica?")
    print("A) sim")
    print("B) nao")
    print("C) não lembro/quase")
    res = str(input())
    res = res.lower()
    i = validar(valores_permitidos, res)
    if i == True:
      soma += soma_resposta(valores_permitidos, [20, 0, 10], res)
    else:
      print("fora do escopo, repetindo")
    #if i == True:
    #  if res == "a":
    #    soma += 20
    #  elif res == "b":
    #    soma += 0
    #  elif res == "c":
    #    soma += 10
    #else:
    #  print("fora do escopo, repetindo")
  i = False
  while i == False:
    print("10- voce consegue chorar na hora que quiser?")
    print("A) sim")
    print("B) as vezes")
    print("C) não")

    res = str(input())
    res = res.lower()
    if i == True:
      soma += soma_resposta(valores_permitidos, [20, 10, 20], res)
    else:
      print("fora do escopo, repetindo")
  #if res == "a":
  #  soma += 20
  #elif res == "b":
  #  soma += 10
  #elif res == "c":
  #  soma += 0

  print("encerrado, avaliando")

  if soma <= 60:
    print("zero drama \n")
    print(
      "parabens, voce não é um drama queen, voce é totalmente pé no chão, mais tranquilo e sabe levar a vida com a atitude correta, que bom, continue assim, com certeza voce mantem os conflitos apenas no nivel necessario na sua vida"
    )
    #colocar descrição de cada um
  elif (soma > 60 and soma <= 140):
    print("drama medio \n")
    print(
      "voce é meio misto, algumas vezes voce age como uma drama queen. Acontece que é normal. Mas voce definitivamente não é um drama queen total, tudo na vida é sobre equilibrio, e voce tem conseguido manter o seu, lembre-se que existem sempre diversas formas de resolver conflitos, e ser dramatico quase nunca é a melhor"
    )
  else:
    print("bem dramatico \n")
    print(
      "parece que voce é um drama queen de primeira, na maioria do tempo voce faz tempestade em copo de agua, seria bom voce tentar, mesmo que uma unica vez, levar a vida de uma forma mais desapegada e não se preocupar tanto, e assim voce vai se sentir melhor melhor doque voce imaginava evitando alguns conflitos"
    )

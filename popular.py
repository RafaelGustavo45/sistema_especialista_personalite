def teste5():
  print("teste voce é popular ")
  print("link: https://www.youtube.com/watch?v=3RwRB_UZkU0")
  soma = 0
  from tecnicas import validar
  from tecnicas import soma_resposta
  valores_permitidos = ["a", "b", "c", "d"]
  #print(soma)
  #max: 40 min: 10 ok ambos
  print("1- de 0 a 100, voce se preocupa com sua aparencia?")
  q = float(input("quantos %:"))
  g = q / 3.225
  soma += 10
  #print(soma)
  soma += g
  #print(soma)
  #print(soma)
  print("2- voce faz parte de alguma equipe esportiva?(s/n)")
  res = str(input())
  res = res.lower()
  if res == "s":
    #print(soma)
    print("de 0 a 100, o quanto voce participa?")
    q = float(input("quantos %:"))
    g = q / 3.225
    soma += 10
    #print(soma)
    soma += g
    #print(soma)
  else:
    soma += 10
    #print(soma)
  i = False
  while i == False:
    print("3- como é o seu circulo de amigos?")
    print("A) Amigos?, mmmmm")
    print("B) bem grande, mas eu não confio em ninguem")
    print("C) grupo pequeno, mas bem proximo")
    print("D) grande, mas poucos são intimos")

    res = str(input("opcao: "))
    res = res.lower()
    i = validar(valores_permitidos, res)
    if i == True:
      soma += soma_resposta(valores_permitidos, [10, 20, 30, 40], res)
    else:
      print("fora do escopo, repetindo")
  #if res == "a":
  #  soma += 10
  #elif res == "b":
  #  soma += 20
  #elif res == "c":
  #  soma += 30
  #elif res == "d":
  #  soma += 40
  i = False
  while i == False:
    print("4- oque voce faz no tempo livre?")
    print("A) fico na internet ou jogando")
    print("B) namoro/saio com alguem")
    print("C) pratico esportes")
    print("D) saio com os amigos")

    res = str(input("opcao: "))
    res = res.lower()
    i = validar(valores_permitidos, res)
    if i == True:
      soma += soma_resposta(valores_permitidos, [10, 20, 40, 30], res)
    else:
      print("fora do escopo, repetindo")

  #if res == "a":
  #  soma += 10
  #elif res == "b":
  #  soma += 20
  #elif res == "c":
  #  soma += 40
  #elif res == "d":
  #  soma += 30
  #print(soma)
  print("5- as pessoas costumam elogiar suas habilidades artisticas? (s/n)")
  res = str(input())
  res = res.lower()
  if res == "s":
    #print(soma)
    print("de 0 a 100, o quanto ocorre o elogio?")
    q = float(input("quantos %:"))
    g = q / 3.225
    soma += 10
    soma += g
    #print(soma)
  else:
    soma += 10
    #print(soma)

  i = False
  while i == False:
    print("6- as pessoas costumam elogiar sua inteligencia?")
    print("A) hummm. nunca")
    print("B) bastante, denovo")
    print("C) as vezes")
    print("D) até que bastante")
    res = str(input("opcao: "))
    res = res.lower()
    i = validar(valores_permitidos, res)
    if i == True:
      soma += soma_resposta(valores_permitidos, [10, 40, 20, 30], res)
    else:
      print("fora do escopo, repetindo")

  #if res == "a":
  #  soma += 10
  #elif res == "b":
  #  soma += 40
  #elif res == "c":
  #  soma += 20
  #elif res == "d":
  # soma += 30
  i = False
  while i == False:
    print("7- as pessoas te zoam/provocam")
    print("A) elas não querem mexer comigo")
    print("B) as vezes")
    print("C) sou uma sombra")
    print("D) todo o tempo, e eu dou o troco")

    res = str(input("opcao: "))
    res = res.lower()
    i = validar(valores_permitidos, res)
    if i == True:
      soma += soma_resposta(valores_permitidos, [30, 20, 10, 40], res)
    else:
      print("fora do escopo, repetindo")

  #if res == "a":
  #  soma += 30
  #elif res == "b":
  #  soma += 20
  #elif res == "c":
  #  soma += 10
  #elif res == "d":
  #  soma += 40
  i = False
  while i == False:
    print("8- as pessoas costumam te dar aquelas olhadas ou secadas?")
    print("A)recebo alguma secadas, fico de saco cheio")
    print("B) Aiiii")
    print("C) normalmente eu dou a secada")
    print("D) uma vez ou outra")
    res = str(input("opcao: "))
    res = res.lower()
    i = validar(valores_permitidos, res)
    if i == True:
      soma += soma_resposta(valores_permitidos, [40, 10, 20, 30], res)
    else:
      print("fora do escopo, repetindo")

  #if res == "a":
  #  soma += 40
  #elif res == "b":
  #  soma += 10
  #elif res == "c":
  #  soma += 20
  #elif res == "d":
  #  soma += 30
  i = False
  while i == False:
    print("9- qual tipo de aplauso voce costuma receber por suas conquistas?")
    print("A) poucos, mas estão ali")
    print("B) muito assobio, e gente gritando meu nome")
    print("C) grandes aplausos e poucos assobios")
    print("D) normal... Hmmmm")

    res = str(input("opcao: "))
    res = res.lower()
    i = validar(valores_permitidos, res)
    if i == True:
      soma += soma_resposta(valores_permitidos, [10, 40, 20, 30], res)
    else:
      print("fora do escopo, repetindo")

  #if res == "a":
  #  soma += 10
  #elif res == "b":
  #  soma += 40
  #elif res == "c":
  #  soma += 20
  #elif res == "d":
  #  soma += 30
  i = False
  while i == False:
    print("10- voce acha se alguem popular? ")
    print("A) talvez, um pouco")
    print("B) sim")
    print("C) Hummmm, não muito")
    print("D) não, eu não sou famoso")

    res = str(input("opcao: "))
    res = res.lower()
    i = validar(valores_permitidos, res)
    if i == True:
      soma += soma_resposta(valores_permitidos, [20, 30, 10, 40], res)
    else:
      print("fora do escopo, repetindo")
  #if res == "a":
  #  soma += 20
  #elif res == "b":
  #  soma += 30
  #elif res == "c":
  #  soma += 10
  #elif res == "d":
  #  soma += 40

  print("\n analisando \n")

  if soma <= 150:
    print("voce não é popular \n")
    print(
      "voce parece ser alguem muito quieto, e gosta de passar tempo sozinho. Isso não é ruim. Mas voce pode trabalhar em algumas coisas, saia mais e socialize mais com as pessoas!"
    )

  elif soma > 150 and soma <= 250:
    print("voce é alguem na media \n")
    print(
      "voce não é alguem popular nem impopular, saia e se abra mais com as pessoas, e escolha suas palavras com mais cuidado"
    )
  elif soma > 250 and soma < 350:
    print("voce está em um bom lugar \n")
    print(
      "voce é uma pessoa muito gentil e legal que é bem ativo, voce é popular mas não é alguem que está sendo seguido e observado a todo instante, curta sua vida com liberdade"
    )
  else:
    print("voce é famoso \n")
    print(
      "as pessoas conhecem o seu nome ou seu rosto. Voce precisa ser cuidadoso, quanto mais amigos voce faz, mais inimigos e haters começam a aparecer do bueiro, se orgulhe mesmo assim e siga a vida"
    )

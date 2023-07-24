def selecao(o):
  #importando

  from minion import teste2
  from drama import teste4
  from lider import teste3
  from popular import teste5

  if o == 2:
    teste2()
  elif o == 3:
    teste3()
  elif o == 4:
    teste4()
  elif o == 5:
    teste5()
  else:
    print("fora do escopo de selecao: ", o)

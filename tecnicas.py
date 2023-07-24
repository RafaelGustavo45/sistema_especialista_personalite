def validar(permitidos, valor_inserido):
  if valor_inserido in permitidos:
    return True
  else:
    return False


def soma_resposta(opcoes, somatorio, letra):
  if len(somatorio) != len(opcoes):
    print("erro: listas de somatorio e opcoes diferem")
  else:
    i = 0
    while i < len(opcoes):
      if opcoes[i] == letra:
        qual = opcoes[i]
        break
      else:
        pass
        i += 1

    sele = ord(qual) - 97
    return somatorio[sele]

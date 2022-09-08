def contarLetras(lista):
  letras = {}
  for i in lista:
    if i not in letras.keys():
      letras[i] = 1
    else:
      letras[i] = letras[i] + 1
      
  return letras
   
print(contarLetras('icfhccuuugguguigcicu'))
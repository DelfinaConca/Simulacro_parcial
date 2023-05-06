def trasladar(una_lista, otra_lista, elemento):
  otra_lista.append(elemento)
  una_lista.remove(elemento)

lista = [2,5,8]
listita = []
trasladar(listita, lista, 2)

# B) -Error: ValueError

def trasladar(una_lista, otra_lista, elemento):
    try:
      una_lista.remove(elemento)
      otra_lista.append(elemento)
    except ValueError:
        print ("El elemento que se quiere eliminar no está en la lista")

lista = [2,5,8]
listita = []
trasladar(listita, lista, 2)

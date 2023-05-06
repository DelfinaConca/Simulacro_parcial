import re
#a)
string = "XabaaaYjXbabbbbaaYqXffeeY"
def entre_X_e_Y(string):
    patron = "X(.*?ab.*?)Y"                 #.*? todo lo que haya: le decimos que si entr X e Y hay algun ab me devuelva todo lo que haya entre esas letras SI es que hay algun ab, sino no me devuelve nada
    return re.findall(patron,string)        # ? le decimos que traiga los matches internos, por eso no puede devolver una X
                                            #.*? es para que nos devuelva TODO lo que esta antes del ab y TODO lo que esta despues
print(entre_X_e_Y(string))

#o

# def entre_X_Y(string):
#     patron = "X[^XY]*ab[^XY]*Y"                       #cuando ya negas algo, por default lo que no negas, lo toma
#     return re.findall(patron,string)
# print(entre_X_Y(string))

#b)
# string = "aabocaggaaactazu4lggaasagag24gra1ndecta"
# def funcionesDeExpresiones_regulares(string):
#     return re.findall("ag([^\d]*)cta",string)

# print(funcionesDeExpresiones_regulares(string))

#V O F:
# 1. FALSO: Las palabras se escriben todas en minusc separadas por _ , No hace falta poner "funcion" en el nombre de la funcion y sus nombres tienen que representar lo que hacen, y falta en parametro entre(). 
# 2. 3. FALSO: Ninguna de esas. Devuelve Atribute Error porque findall tenia solo una l
# 4. VERDADERO: con la funcion arreglada devuelve eso
# 5. FALSO: Sabemos por la consigna que no tiene que devolver num, entoonces ya descartamos esa opcion


#"ag(\d.*?)cta" en este patron le estamos diciendo que haya un valor numerico siguiendo de caulquier cosa todo eso entre ag y cta
# hay que ponerle el ^ \d asi dice cualquier cosa menos el valor digital, sacarle el . porque se contradice ya que es cualquier cosa y el ? 
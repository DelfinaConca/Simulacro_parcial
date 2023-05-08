import os, glob , re

def filtrar (archivo): 
    lista_txt = glob.glob("*.txt")

    with open(archivo, "a") as arch:         #solo lo abrimos "a"
        for archivo in lista_txt:
            with open (archivo,"r") as archivo_secreto:      # leemos "r"
                texto = archivo_secreto.read()
                lista = re.findall("[\w]+[-_\.]*[\w]*+@gmail.com",texto)
                for email in lista:
                    arch.write(email+"\n")             # el .write solo escribe strings
filtrar("base_de_datos.txt")
# en el ej reemplazar donde dice archivo por "base de datos"

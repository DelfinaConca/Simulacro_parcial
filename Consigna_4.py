#ENUNCIADO 
#come bolitas: gana de puntos el dobrle de la cant de bolitas
#come fantasma: rosa 8, verde 6,naranja 4, rojo 2
#velocidad: (puntos + 2)/100
#perder vida: contar -1 baja cant de vidas, resetea puntos. Si se queda sin vidas "fin del juego"

#a)
class PacMan:
    def __innit__(self):   #no tiene parametros, porque son datos iniciales fijos
        self.puntos = 0
        self.vidas = 3 

    def comer_bolitas(self, bolitas):
        self.puntos += (bolitas * 2)        
        
    def velocidad(self):
        return 2 + self.puntos /100        
    
    def perderVida(self):
        self.puntos = 0
        self.vidas -= 1
    
        if self.vidas == 0:
            print("GAME OVER")
#1era opcion   
#     def comer_fantasma(self,fantasma):
#         if fantasma == "rosa":
#             self.puntos +=8 
#         elif fantasma == "verde":
#             self.puntos +=6
#         elif fantasma == "naranja":
#             self.puntos +=4
#         elif fantasma == "rojo":
#             self.puntos +=2
# #2da opcion
    def comer_fantasma(self,fantasma,color):
        self.puntos+= fantasma.puntos_color(color)

#2da opcion
class Fantasma:
    def __innit__(self):
        self.fantasmas = {"rosa": 8, "verde": 6,"naranja": 4, "rojo": 2}
    
    
    def puntos_color(self,color):
        return self.fantasmas(color)


#1era opcion
# pacman = PacMan() #como no tiene parametros, no le tengo que pasar argumentos
# print(pacman.puntos)
# pacman.comer_bolitas(10)
# print(pacman.puntos)
# pacman.comer_fantasma("verde")
# print(pacman.puntos)

#2da opcion
pacman = PacMan()
fantasma = Fantasma()

print(pacman.puntos)
# pacman.comer_bolitas(10)
# print(pacman.puntos)
# pacman.comer_fantasma("verde")
# print(pacman.puntos)

#b)
class PacManMejorado(PacMan):
    def vida_extra(self):
        if self.puntos >= 200:
            self.vidas +=1
            self.puntos -+ 200
        else:
            print ("Faltan", 200 - self.puntos, "puntos para ganar una vida extra")
        
    def velocidad(self):
        return 3 + self.puntos / 100


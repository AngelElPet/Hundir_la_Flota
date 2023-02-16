import numpy as np
import random as rd


class Tablero:
    tablero_amigo = np.full((10,10),'X')
    tablero_enemigo = np.full((10,10),' ')
    barcos1 = 4
    barcos2 = 3
    barcos3 = 2
    barcos4 = 1
    barcos_vivos = 0
    sitios_atacados = []
    lista_barcos = []#lista de tuplas con las posiciones de las celdas que aun tienen un barco vivo
    puntos_ataque = []
    def __init__(self) -> None:
        pass
    def restart (self):
        self.tablero_amigo = np.full((10,10),'X')
        self.tablero_enemigo = np.full((10,10),' ')
        self.barcos1 = 4
        self.barcos2 = 3
        self.barcos3 = 2
        self.barcos4 = 1
        self.barcos_vivos = 0
        self.lista_barcos =[]
        self.sitios_atacados = []
        self.puntos_ataque = []
     
    def sin_blancos(self):
        self.puntos_ataque = []
    def blancos (self,c):
        x = c[0]
        y = c[1]
        
        print ('He hentrado')
        print (type(str(self.tablero_amigo[(x+1,y)]))== type('a') and not((x+1,y) in self.sitios_atacados))
        print(self.sitios_atacados)
        print(c)
        print(not(c in self.sitios_atacados))
    
        try:
            if type(str(self.tablero_amigo[(x+1,y)]))== type('a') and not((x+1,y)in self.sitios_atacados) :
                self.puntos_ataque.append((x+1,y))
        except IndexError:
            pass
        try:
            if type(str(self.tablero_amigo[(x-1,y)]))== type('a') and not((x-1,y)in self.sitios_atacados):
                self.puntos_ataque.append((x-1,y))
        except IndexError:
            pass
        try:
            if type(str(self.tablero_amigo[(x,y-1)]))== type('a')and not((x,y-1)in self.sitios_atacados):
                self.puntos_ataque.append((x,y-1))
        except IndexError:
            pass
        try:
            if type(str(self.tablero_amigo[(x,y+1)]))== type('a') and not((x,y+1) in self.sitios_atacados):
                self.puntos_ataque.append((x,y+1))
        except IndexError:
            pass
    def posicion_aleatoria_facil(self):
        while self.barcos1 >0:
            x = rd.randint(0,9)
            y = rd.randint(0,9)
            if self.tablero_amigo[x,y] == 'X':
                self.tablero_amigo[x,y] ='1'
                self.barcos1 -= 1
                self.barcos_vivos +=1
                self.lista_barcos.append((x,y))
        while self.barcos2 >0:
            
            x = rd.randint(0,9)
            y = rd.randint(0,8)
            if self.tablero_amigo[x,y] == 'X' and self.tablero_amigo[x,y+1] == 'X':
                self.tablero_amigo[x,y] ='2'
                self.tablero_amigo[x,y+1] ='2'
                self.barcos2 -= 1
                self.barcos_vivos +=1
                self.lista_barcos.extend(((x,y),(x,y+1)))
        while self.barcos3>0:
            x = rd.randint(0,9)
            y = rd.randint(0,7)
            if self.tablero_amigo[x,y] == 'X' and self.tablero_amigo[x,y+1] == 'X' and self.tablero_amigo[x,y+2] == 'X':
                self.tablero_amigo[x,y] ='3'
                self.tablero_amigo[x,y+1] ='3'
                self.tablero_amigo[x,y+2] ='3'
                self.barcos3 -= 1
                self.barcos_vivos +=1
                self.lista_barcos.extend(((x,y),(x,y+1),(x,y+2)))
        while self.barcos4>0:
            
            x = rd.randint(0,9)
            y = rd.randint(0,6)
            if self.tablero_amigo[x,y] == 'X' and self.tablero_amigo[x,y+1] == 'X' and self.tablero_amigo[x,y+2] == 'X'and self.tablero_amigo[x,y+3] == 'X':
                self.tablero_amigo[x,y] ='4'
                self.tablero_amigo[x,y+1] ='4'
                self.tablero_amigo[x,y+2] ='4'
                self.tablero_amigo[x,y+3] = '4'
                self.barcos4-= 1
                self.barcos_vivos +=1
                self.lista_barcos.extend(((x,y),(x,y+1),(x,y+2),(x,y+3)))
    def posicion_aleatoria_dif(self):
        
        while self.barcos1 >0:
            x = rd.randint(0,9)
            y = rd.randint(0,9)
            if self.tablero_amigo[x,y] == 'X':
                self.tablero_amigo[x,y] ='1'
                self.barcos1 -= 1
                self.barcos_vivos +=1
                self.lista_barcos.append((x,y))
        
        while self.barcos2 >0:
            y1 = np.random.randint(0,4, size=(1,1))
            x1 = y1
            if x1 == 0: #Se posiciona el barco hacia la derecha
                x = rd.randint(0,9)
                y = rd.randint(0,8)
                if self.tablero_amigo[x,y] == 'X' and self.tablero_amigo[x,y+1] == 'X':
                    self.tablero_amigo[x,y] ='2'
                    self.tablero_amigo[x,y+1] ='2'
                    self.barcos2 -= 1
                    self.barcos_vivos +=1
                    self.lista_barcos.extend(((x,y),(x,y+1)))
            if x1 == 1: #Se posiciona el barco hacia la izquierda
                x = rd.randint(0,9)
                y = rd.randint(1,9)
                if self.tablero_amigo[x,y] == 'X' and self.tablero_amigo[x,y-1] == 'X':
                    self.tablero_amigo[x,y] ='2'
                    self.tablero_amigo[x,y-1] ='2'
                    self.barcos2 -= 1
                    self.barcos_vivos +=1
                    self.lista_barcos.extend(((x,y),(x,y-1)))
            if x1 == 2: #Se posiciona el barco hacia arriba
                x = rd.randint(1,9)
                y = rd.randint(0,9)
                if self.tablero_amigo[x,y] == 'X' and self.tablero_amigo[x-1,y] == 'X':
                    self.tablero_amigo[x,y] ='2'
                    self.tablero_amigo[x-1,y] ='2'
                    self.barcos2 -= 1
                    self.barcos_vivos +=1
                    self.lista_barcos.extend(((x,y),(x-1,y)))
            if x1 == 3: #Se posiciona el barco hacia abajo
                x = rd.randint(0,8)
                y = rd.randint(0,9)
                if self.tablero_amigo[x,y] == 'X' and self.tablero_amigo[x+1,y] == 'X':
                    self.tablero_amigo[x,y] ='2'
                    self.tablero_amigo[x+1,y] ='2'
                    self.barcos2 -= 1
                    self.barcos_vivos +=1
                    self.lista_barcos.extend(((x,y),(x+1,y)))
        while self.barcos3>0:
            y1 = np.random.randint(0,6, size=(1,1))
            x1 = y1
            if x1 == 0: #Se posiciona el barco hacia la derecha
                x = rd.randint(0,9)
                y = rd.randint(0,7)
                if self.tablero_amigo[x,y] == 'X' and self.tablero_amigo[x,y+1] == 'X' and self.tablero_amigo[x,y+2] == 'X':
                    self.tablero_amigo[x,y] ='3'
                    self.tablero_amigo[x,y+1] ='3'
                    self.tablero_amigo[x,y+2] ='3'
                    self.barcos3 -= 1
                    self.barcos_vivos +=1
                    self.lista_barcos.extend(((x,y),(x,y+1),(x,y+2)))
            if x1 == 1: #Se posiciona el barco hacia la izquierda
                x = rd.randint(0,9)
                y = rd.randint(2,9)
                if self.tablero_amigo[x,y] == 'X' and self.tablero_amigo[x,y-1] == 'X' and self.tablero_amigo[x,y-2] == 'X':
                    self.tablero_amigo[x,y] ='3'
                    self.tablero_amigo[x,y-1] ='3'
                    self.tablero_amigo[x,y-2] ='3'
                    self.barcos3 -= 1
                    self.barcos_vivos +=1
                    self.lista_barcos.extend(((x,y),(x,y-1),(x,y-2)))
            if x1 == 2: #Se posiciona el barco hacia arriba
                x = rd.randint(2,9)
                y = rd.randint(0,9)
                if self.tablero_amigo[x,y] == 'X' and self.tablero_amigo[x-1,y] == 'X' and self.tablero_amigo[x-2,y] == 'X':
                    self.tablero_amigo[x,y] ='3'
                    self.tablero_amigo[x-1,y] ='3'
                    self.tablero_amigo[x-2,y] ='3'
                    self.barcos3 -= 1
                    self.barcos_vivos +=1
                    self.lista_barcos.extend(((x,y),(x-1,y),(x-2,y)))
            if x1 == 3: #Se posiciona el barco hacia abajo
                x = rd.randint(0,7)
                y = rd.randint(0,9)
                if self.tablero_amigo[x,y] == 'X' and self.tablero_amigo[x+1,y] == 'X' and self.tablero_amigo[x+2,y] == 'X':
                    self.tablero_amigo[x,y] ='3'
                    self.tablero_amigo[x+1,y] ='3'
                    self.tablero_amigo[x+2,y] ='3'
                    self.barcos3 -= 1
                    self.barcos_vivos +=1
                    self.lista_barcos.extend(((x,y),(x+1,y),(x+2,y)))
            if x1 == 4: #Se posiciona el barco hacia la derecha e izquierda siendo (a[0,0],a[0,1]) el centro del barco
                x = rd.randint(0,9)
                y = rd.randint(1,8)
                if self.tablero_amigo[x,y] == 'X' and self.tablero_amigo[x,y+1] == 'X' and self.tablero_amigo[x,y-1] == 'X':
                    self.tablero_amigo[x,y] ='3'
                    self.tablero_amigo[x,y+1] ='3'
                    self.tablero_amigo[x,y-1] ='3'
                    self.barcos3 -= 1
                    self.barcos_vivos +=1
                    self.lista_barcos.extend(((x,y),(x,y-1),(x,y+1)))
            if x1 == 5: #Se posiciona el barco hacia arriba y abajo siendo (a[0,0],a[0,1]) el centro del barco
                x = rd.randint(1,8)
                y = rd.randint(0,9)
                if self.tablero_amigo[x,y] == 'X' and self.tablero_amigo[x-1,y] == 'X' and self.tablero_amigo[x+1,y] == 'X':
                    self.tablero_amigo[x,y] ='3'
                    self.tablero_amigo[x-1,y] ='3'
                    self.tablero_amigo[x+1,y] ='3'
                    self.barcos3 -= 1
                    self.barcos_vivos +=1
                    self.lista_barcos.extend(((x,y),(x-1,y),(x+1,y)))
        while self.barcos4>0:
            y1 = np.random.randint(0,6, size=(1,1))
            x1= y1
            if x1 == 0: #Se posiciona el barco hacia la derecha
                x = rd.randint(0,9)
                y = rd.randint(0,6)
                if self.tablero_amigo[x,y] == 'X' and self.tablero_amigo[x,y+1] == 'X' and self.tablero_amigo[x,y+2] == 'X'and self.tablero_amigo[x,y+3] == 'X':
                    self.tablero_amigo[x,y] ='4'
                    self.tablero_amigo[x,y+1] ='4'
                    self.tablero_amigo[x,y+2] ='4'
                    self.tablero_amigo[x,y+3] = '4'
                    self.barcos4-= 1
                    self.barcos_vivos +=1
                    self.lista_barcos.extend(((x,y),(x,y+1),(x,y+2),(x,y+3)))
            if x1 == 1: #Se posiciona el barco hacia la izquierda
                x = rd.randint(0,9)
                y = rd.randint(3,9)
                if self.tablero_amigo[x,y] == 'X' and self.tablero_amigo[x,y-1] == 'X' and self.tablero_amigo[x,y-2] == 'X'and self.tablero_amigo[x,y-3] == 'X':
                    self.tablero_amigo[x,y] ='4'
                    self.tablero_amigo[x,y-1] ='4'
                    self.tablero_amigo[x,y-2] ='4'
                    self.tablero_amigo[x,y-3] = '4'
                    self.barcos4-= 1
                    self.barcos_vivos +=1
                    self.lista_barcos.extend(((x,y),(x,y-1),(x,y-2),(x,y-3)))
            if x1 == 2: #Se posiciona el barco hacia arriba
                x = rd.randint(3,9)
                y = rd.randint(0,9)
                if self.tablero_amigo[x,y] == 'X' and self.tablero_amigo[x-1,y] == 'X' and self.tablero_amigo[x-2,y] == 'X'and self.tablero_amigo[x-3,y] == 'X':
                    self.tablero_amigo[x,y] ='4'
                    self.tablero_amigo[x-1,y] ='4'
                    self.tablero_amigo[x-2,y] ='4'
                    self.tablero_amigo[x-3,y] = '4'
                    self.barcos4-= 1
                    self.barcos_vivos +=1
                    self.lista_barcos.extend(((x,y),(x-1,y),(x-2,y),(x-3,y)))
            if x1 == 3: #Se posiciona el barco hacia abajo
                x = rd.randint(0,6)
                y = rd.randint(0,9)
                if self.tablero_amigo[x,y] == 'X' and self.tablero_amigo[x+1,y] == 'X' and self.tablero_amigo[x+2,y] == 'X'and self.tablero_amigo[x+3,y] == 'X':
                    self.tablero_amigo[x,y] ='4'
                    self.tablero_amigo[x+1,y] ='4'
                    self.tablero_amigo[x+2,y] ='4'
                    self.tablero_amigo[x+3,y] = '4'
                    self.barcos4-= 1
                    self.barcos_vivos +=1
                    self.lista_barcos.extend(((x,y),(x+1,y),(x+2,y),(x+3,y)))
            if x1 == 4: #Se posiciona el barco hacia la derecha+2 e izquierda siendo (a[0,0],a[0,1]) el centro del barco
                
                x = rd.randint(0,9)
                y = rd.randint(1,7)
                if self.tablero_amigo[x,y] == 'X' and self.tablero_amigo[x,y+1] == 'X' and self.tablero_amigo[x,y+2] == 'X'and self.tablero_amigo[x,y-1] == 'X':
                    self.tablero_amigo[x,y] ='4'
                    self.tablero_amigo[x,y-1] ='4'
                    self.tablero_amigo[x,y+1] ='4'
                    self.tablero_amigo[x,y+2]= '4'
                    self.barcos4-= 1
                    self.barcos_vivos +=1
                    self.lista_barcos.extend(((x,y),(x,y-1),(x,y+1),(x,y+2)))
            if x1 == 5: #Se posiciona el barco hacia arriba y abajo+2 siendo (a[0,0],a[0,1]) el centro del barco
                x = rd.randint(1,7)
                y = rd.randint(0,9)
                if self.tablero_amigo[x,y] == 'X' and self.tablero_amigo[x+1,y] == 'X' and self.tablero_amigo[x+2,y] == 'X'and self.tablero_amigo[x-1,y] == 'X':
                    self.tablero_amigo[x,y] ='4'
                    self.tablero_amigo[x-1,y] ='4'
                    self.tablero_amigo[x+1,y] ='4'
                    self.tablero_amigo[x+2,y]= '4'
                    self.barcos4-= 1
                    self.barcos_vivos +=1
                    self.lista_barcos.extend(((x,y),(x+1,y),(x+2,y),(x-1,y)))

    def posicion_aleatoria_dif2(self):
        self.posicion_aleatoria_dif()
        for x in range(10):
            for y in range(10):
                if self.tablero_amigo[x,y] != 'X':
                    self.tablero_amigo[x,y] = 'O'
    
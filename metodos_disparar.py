from clase_tablero import*
import numpy as np
import random as rd

def disparar_persona(a,b,c): # c va a ser la tupla disparo
    if b.tablero_amigo[c[0],c[1]] != 'X':
        a.tablero_enemigo[c[0],c[1]] = b.tablero_amigo[c[0],c[1]]
        print ('Campo de batalla de la persona', a.tablero_enemigo, sep = '\n')
        print('Sigues disparando')
        return [True,c]
    else:
        a.tablero_enemigo[c[0],c[1]] = b.tablero_amigo[c[0],c[1]]
        print ('Campo de batalla de la persona', a.tablero_enemigo, sep = '\n')
        print('Has fallado, conque pierdes tu posición de ataque')
        return [False,(None,)]
    
def disparar_maquina (a,b,c): # c va a ser la tupla disparo
    if b.tablero_amigo[c[0],c[1]] != 'X':
        a.tablero_enemigo[c[0],c[1]] = b.tablero_amigo[c[0],c[1]]
        print ('Campo de batalla de la máquina', a.tablero_enemigo, sep = '\n')
        print('Sigues disparando')
        return [True,c]
    else:
        a.tablero_enemigo[c[0],c[1]] = b.tablero_amigo[c[0],c[1]]
        print ('Campo de batalla de la máquina', a.tablero_enemigo, sep = '\n')
        print('Has fallado, conque pierdes tu posición de ataque')
        return [False,(None,None)]
    
def disparo_aleatorio_dif(a,b): #donde a es la máquina, b es el jugador y c es un disparo de proximidad
    if len(a.puntos_ataque)!=0:
        disparo = a.puntos_ataque[0]
        a.puntos_ataque.remove(a.puntos_ataque[0])
        a.sitios_atacados.append(disparo)
        d= disparar_maquina(a,b,disparo)
        if b.tablero_amigo[d[1][0],d[1][1]] != '1' and d[1]!= (None,None):
            print('HE ACERTADO')
            print(d[1])
            a.blancos(d[1])
        return d
    else:
        disparo_x = rd.randint(0,9)
        disparo_y = rd.randint(0,9)
        disparo = (disparo_x,disparo_y)
        if disparo in a.sitios_atacados:
            disparo_aleatorio_dif(a,b)
        else:
            a.sitios_atacados.append(disparo)
    
    d = disparar_maquina(a,b,disparo)
    if d[0]:
        if b.tablero_amigo[d[1][0],d[1][1]] != '1':
            print('HE ACERTADO')
            print(d[1])
            a.blancos(d[1])
    return d

def disparo_no_aleatorio(a,b):
    
        disparo_x = int(input('Introduce la coordenada x (un numero entre el 1 y el 10)'))-1
        disparo_y = int(input('Introduce la coordenada y (un numero entre el 1 y el 10)'))-1
        disparo = (disparo_x,disparo_y)
    
        while (ord(str(disparo_x))<48 and ord(str(disparo_x))>57) or (ord(str(disparo_y))<48 and ord(str(disparo_y))>57):
            print('Las coordenadas introducidas no son validas. Por favor, vuelve a introducir valores entre el 1 y el 10 ')
            disparo_x = int(input('Introduce la coordenada x (un numero entre el 1 y el 10)'))
            disparo_y = int(input('Introduce la coordenada y (un numero entre el 1 y el 10)'))
            disparo = (disparo_x,disparo_y)
        
        if disparo in a.sitios_atacados:
            return [False, (None,)]
        else:
            a.sitios_atacados.append(disparo)
                
        return disparar_persona(a,b,disparo)

def disparo_aleatorio_facil(a,b): #donde a es el objeto Tablero del que ataca y b el objeto Tablero del que defiende
    
    
    disparo_x = rd.randint(0,9)
    disparo_y = rd.randint(0,9)
    disparo = (disparo_x,disparo_y)
    if disparo in a.sitios_atacados:
        disparo_aleatorio_facil(a,b)
    else:
        a.sitios_atacados.append(disparo)
    
    return disparar_maquina(a,b,disparo)

def seguir_jugando():
    a = int(input('Introduce 0 para salir del juego. Introduce 1 para seguir jugando'))
    if a == 0:
        return True
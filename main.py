import numpy as np
import random as rd
from clase_tablero import*
from metodos_disparar import*

g ='''
                    ___                                     ___                    ___           ___                       ___   
     _____         /  /\          ___                      /  /\                  /  /\         /__/\        ___          /  /\  
    /  /::\       /  /::\        /  /\                    /  /:/_                /  /:/_        \  \:\      /  /\        /  /::\ 
   /  /:/\:\     /  /:/\:\      /  /:/    ___     ___    /  /:/ /\              /  /:/ /\        \__\:\    /  /:/       /  /:/\:\\ 
  /  /:/~/::\   /  /:/~/::\    /  /:/    /__/\   /  /\  /  /:/ /:/_            /  /:/ /::\   ___ /  /::\  /__/::\      /  /:/~/:/
 /__/:/ /:/\:| /__/:/ /:/\:\  /  /::\    \  \:\ /  /:/ /__/:/ /:/ /\          /__/:/ /:/\:\ /__/\  /:/\:\ \__\/\:\__  /__/:/ /:/ 
 \  \:\/:/~/:/ \  \:\/:/__\/ /__/:/\:\    \  \:\  /:/  \  \:\/:/ /:/          \  \:\/:/~/:/ \  \:\/:/__\/    \  \:\/\ \  \:\/:/  
  \  \::/ /:/   \  \::/      \__\/  \:\    \  \:\/:/    \  \::/ /:/            \  \::/ /:/   \  \::/          \__\::/  \  \::/   
   \  \:\/:/     \  \:\           \  \:\    \  \::/      \  \:\/:/              \__\/ /:/     \  \:\          /__/:/    \  \:\   
    \  \::/       \  \:\           \__\/     \__\/        \  \::/                 /__/:/       \  \:\         \__\/      \  \:\  
     \__\/         \__\/                                   \__\/                  \__\/         \__\/                     \__\/

'''
g1 ='''
Bienvenido al Batle ship donde te enfrentarás a la máquina más inteligente. A ver si eres capaz de ganarle. Lo primero de todo
es introducir el nivel de dificultad:\n
    Nivel de dificultad facil introduce 1
    Nivel de dificultad medio introduce 2
    Nivel de dificultad difícil introduce 3
    Nivel de dificultad extremo introduce 4\n'''
print(g)
print()
print(g1)

f = int(input('Introduce el nivel de dificultad que quieres: '))

if f == 1:
    Maquina = Tablero()
    Persona = Tablero()
    Maquina.restart()
    Maquina.posicion_aleatoria_facil()
    Persona.restart()
    Persona.posicion_aleatoria_dif2()
    c1 = Maquina.lista_barcos.copy()
    c2 = Persona.lista_barcos.copy()

    while len(c1)>0 or len(c2)>0:
        e = seguir_jugando()
        if e:
            break
        d1 = [True,(None,)]
        d2 = [True,(None,)]
        while d1[0]:
            d1 = disparo_no_aleatorio(Persona,Maquina)
            try:
                c1.remove(d1[1])
            except ValueError:
                pass
            print('Te quedan ', len(c1), ' de aciertos para poder ganar')
            if d1[0]==False:
                break
            if len(c1) == 0:
                break
    
        if len(c1) ==0:
            break    
        while d2[0]:
            d2= disparo_aleatorio_facil(Maquina,Persona)
            try:
                c2.remove(d2[1])  
            except ValueError:
                pass
            print('Le quedan ',len(c2), ' de aciertos a la máquina para ganarte')
        
            if d2[0]==False:
                break
            if len(c2) == 0:
                break
        if len(c2) == 0:
            break

    

if f == 2:
    Maquina = Tablero()
    Persona = Tablero()
    Maquina.restart()
    Maquina.posicion_aleatoria_dif()
    Persona.restart()
    Persona.posicion_aleatoria_dif2()
    c1 = Maquina.lista_barcos.copy()
    c2 = Persona.lista_barcos.copy()

    while len(c1)>0 or len(c2)>0:
        e = seguir_jugando()
        if e:
            break
        d1 = [True,(None,)]
        d2 = [True,(None,)]
        while d1[0]:
            d1 = disparo_no_aleatorio(Persona,Maquina)
            try:
                c1.remove(d1[1])
            except ValueError:
                pass
            print('Te quedan ', len(c1), ' de aciertos para poder ganar')
            if d1[0]==False:
                break
            if len(c1) == 0:
                break
    
        if len(c1) ==0:
            break    
        while d2[0]:
            d2= disparo_aleatorio_dif(Maquina,Persona)
            try:
                c2.remove(d2[1])  
            except ValueError:
                pass
            print('Le quedan ',len(c2), ' de aciertos a la máquina para ganarte')
        
            if d2[0]==False:
                break
            if len(c2) == 0:
                break
        if len(c2) == 0:
            break

    

if f == 3:
    Maquina = Tablero()
    Persona = Tablero()
    Maquina.restart()
    Maquina.posicion_aleatoria_dif2()
    Persona.restart()
    Persona.posicion_aleatoria_dif2()
    c1 = Maquina.lista_barcos.copy()
    c2 = Persona.lista_barcos.copy()

    while len(c1)>0 or len(c2)>0:
        e = seguir_jugando()
        if e:
            break
        d1 = [True,(None,)]
        d2 = [True,(None,)]
        while d1[0]:
            d1 = disparo_no_aleatorio(Persona,Maquina)
            try:
                c1.remove(d1[1])
            except ValueError:
                pass
            print('Te quedan ', len(c1), ' de aciertos para poder ganar')
            if d1[0]==False:
                break
            if len(c1) == 0:
                break
    
        if len(c1) ==0:
            break    
        while d2[0]:
            d2= disparo_aleatorio_dif(Maquina,Persona)
            try:
                c2.remove(d2[1])  
            except ValueError:
                pass
            print('Le quedan ',len(c2), ' de aciertos a la máquina para ganarte')
        
            if d2[0]==False:
                break
            if len(c2) == 0:
                break
        if len(c2) == 0:
            break

    

if f == 4:
    Maquina = Tablero()
    Persona = Tablero()
    Maquina.restart()
    Maquina.posicion_aleatoria_dif2()
    Persona.restart()
    Persona.posicion_aleatoria_dif()
    c1 = Maquina.lista_barcos.copy()
    c2 = Persona.lista_barcos.copy()

    while len(c1)>0 or len(c2)>0:
        e = seguir_jugando()
        if e:
            break
        d1 = [True,(None,)]
        d2 = [True,(None,)]
        while d1[0]:
            d1 = disparo_no_aleatorio(Persona,Maquina)
            try:
                c1.remove(d1[1])
            except ValueError:
                pass
            print('Te quedan ', len(c1), ' de aciertos para poder ganar')
            if d1[0]==False:
                break
            if len(c1) == 0:
                break
    
        if len(c1) ==0:
            break    
        while d2[0]:
            d2= disparo_aleatorio_dif(Maquina,Persona)
            try:
                c2.remove(d2[1])  
            except ValueError:
                pass
            print('Le quedan ',len(c2), ' de aciertos a la máquina para ganarte')
        
            if d2[0]==False:
                break
            if len(c2) == 0:
                break
        if len(c2) == 0:
            break



a ='''
                                                                                         
                                                                                         
                                    ___                                                  
             ,--,                 ,--.'|_                          ,--,                  
           ,--.'|                 |  | :,'     ,---.     __  ,-. ,--.'|                  
     .---. |  |,                  :  : ' :    '   ,'\  ,' ,'/ /| |  |,                   
   /.  ./| `--'_        ,---.   .;__,'  /    /   /   | '  | |' | `--'_        ,--.--.    
 .-' . ' | ,' ,'|      /     \  |  |   |    .   ; ,. : |  |   ,' ,' ,'|      /       \   
/___/ \: | '  | |     /    / '  :__,'| :    '   | |: : '  :  /   '  | |     .--.  .-. |  
.   \  ' . |  | :    .    ' /     '  : |__  '   | .; : |  | '    |  | :      \__\/: . .  
 \   \   ' '  : |__  '   ; :__    |  | '.'| |   :    | ;  : |    '  : |__    ," .--.; |  
  \   \    |  | '.'| '   | '.'|   ;  :    ;  \   \  /  |  , ;    |  | '.'|  /  /  ,.  |  
   \   \ | ;  :    ; |   :    :   |  ,   /    `----'    ---'     ;  :    ; ;  :   .'   \ 
    '---"  |  ,   /   \   \  /     ---`-'                        |  ,   /  |  ,     .-. / 
            ---`-'     `----'                                     ---`-'    `--`---'    




'''
b = ''' 
          _____                    _____                    _____                    _____                   _______               _____                    _____          
         /\    \                  /\    \                  /\    \                  /\    \                 /::\    \             /\    \                  /\    \         
        /::\    \                /::\    \                /::\    \                /::\    \               /::::\    \           /::\    \                /::\    \        
       /::::\    \              /::::\    \              /::::\    \              /::::\    \             /::::::\    \          \:::\    \              /::::\    \       
      /::::::\    \            /::::::\    \            /::::::\    \            /::::::\    \           /::::::::\    \          \:::\    \            /::::::\    \      
     /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \         /:::/~~\:::\    \          \:::\    \          /:::/\:::\    \     
    /:::/  \:::\    \        /:::/__\:::\    \        /:::/__\:::\    \        /:::/__\:::\    \       /:::/    \:::\    \          \:::\    \        /:::/__\:::\    \    
   /:::/    \:::\    \      /::::\   \:::\    \      /::::\   \:::\    \      /::::\   \:::\    \     /:::/    / \:::\    \         /::::\    \      /::::\   \:::\    \   
  /:::/    / \:::\    \    /::::::\   \:::\    \    /::::::\   \:::\    \    /::::::\   \:::\    \   /:::/____/   \:::\____\       /::::::\    \    /::::::\   \:::\    \  
 /:::/    /   \:::\ ___\  /:::/\:::\   \:::\    \  /:::/\:::\   \:::\____\  /:::/\:::\   \:::\____\ |:::|    |     |:::|    |     /:::/\:::\    \  /:::/\:::\   \:::\    \ 
/:::/____/     \:::|    |/:::/__\:::\   \:::\____\/:::/  \:::\   \:::|    |/:::/  \:::\   \:::|    ||:::|____|     |:::|    |    /:::/  \:::\____\/:::/  \:::\   \:::\____\\
\:::\    \     /:::|____|\:::\   \:::\   \::/    /\::/   |::::\  /:::|____|\::/   |::::\  /:::|____| \:::\    \   /:::/    /    /:::/    \::/    /\::/    \:::\  /:::/    /
 \:::\    \   /:::/    /  \:::\   \:::\   \/____/  \/____|:::::\/:::/    /  \/____|:::::\/:::/    /   \:::\    \ /:::/    /    /:::/    / \/____/  \/____/ \:::\/:::/    / 
  \:::\    \ /:::/    /    \:::\   \:::\    \            |:::::::::/    /         |:::::::::/    /     \:::\    /:::/    /    /:::/    /                    \::::::/    /  
   \:::\    /:::/    /      \:::\   \:::\____\           |::|\::::/    /          |::|\::::/    /       \:::\__/:::/    /    /:::/    /                      \::::/    /   
    \:::\  /:::/    /        \:::\   \::/    /           |::| \::/____/           |::| \::/____/         \::::::::/    /     \::/    /                       /:::/    /    
     \:::\/:::/    /          \:::\   \/____/            |::|  ~|                 |::|  ~|                \::::::/    /       \/____/                       /:::/    /     
      \::::::/    /            \:::\    \                |::|   |                 |::|   |                 \::::/    /                                     /:::/    /      
       \::::/    /              \:::\____\               \::|   |                 \::|   |                  \::/____/                                     /:::/    /       
        \::/____/                \::/    /                \:|   |                  \:|   |                   ~~                                           \::/    /        
         ~~                       \/____/                  \|___|                   \|___|                                                                 \/____/         
                                                                                                                                                                           
'''




if len(c1) == 0:
    print(a)
else:
    print(b)
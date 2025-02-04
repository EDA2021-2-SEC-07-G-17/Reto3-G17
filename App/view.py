﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
import time 
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Inicializar catalogo")
    print("2- Cargar informacion")
    print("3- Contar los avistamientos en una ciudad->Req 1")
    print("4- Contar los avistamientos por duracion->Req 2-Sebastián Casanova")
    print("5- Contar avistamientos por Hora/Minutos del día->Req 3-Jaime Alfonso")
    print("6- Contar los avistamientos en un rango de fechas->Req 4")
    print("7- Contar los avistamientos de una Zona Geográfica->Req 5")
    print("8- Visualizar los avistamientos de una zona geográfica->Bono")

catalogo = None
ufofile = 'UFOS-utf8-small.csv'

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    
    if int(inputs[0]) == 1:
        print("Inicializando catalogo...")
        catalogo = controller.iniciar_catalogo()


    elif int(inputs[0]) == 2:
        print("Cargando información de los archivos ....")
        controller.loadData(catalogo, ufofile)
        print("El total de avistamientos cargados son: "+str(lt.size(catalogo["lista_ufos"])))
        i = 1
        l = lt.newList("ARRAY_LIST")
        lst = catalogo['lista_ufos']
        print("Los primeros cinco avistamientos: ")
        while i <= 5:
            ufo = lt.getElement(lst, i)
            print("\nDatatime: " + str(ufo["datetime"]) + "\nCiudad: " + ufo["city"] + "\nPaís: " + ufo["country"]
                    + "\nDuración (segundos): " + str(ufo["duration (seconds)"]) + "\nForma del objeto: " + ufo["shape"])
            uf = lt.lastElement(lst)
            lt.removeLast(lst)
            lt.addFirst(l, uf)
            i += 1
        
        print("Los últimos cinco avistamientos: ")
        for u in lt.iterator(l):
            print("\nDatatime: " + str(u["datetime"]) + "\nCiudad: " + u["city"] + "\nPaís: " + u["country"]
                    + "\nDuración (segundos): " + str(u["duration (seconds)"]) + "\nForma del objeto: " + u["shape"])

    
    elif int(inputs[0]) == 3:
        
        ciudad = input("Escriba la ciudad de la cual quiera saber los avistamientos registrados: ")
        tiempo_inicio=time.process_time()

        total, contador, listado = controller.avistamientos_ciudad(catalogo, ciudad)

        print("\n")
        print("El total de ciudades que tienen avistamientos de UFOS es: "+str(total))
        print("\n")
        print("El total de avistamientos en "+str(ciudad)+" es: "+str(contador))

        i = 1
        lst = lt.newList("ARRAY_LIST")
        print("\n")
        print("Los primeros 3 avistamientos en la ciudad son: ")
        while i <= 3:
            ufo = lt.getElement(listado, i)
            print("\nDatatime: " + str(ufo["datetime"]) + "\nCiudad: " + ufo["city"] + "\nEstado: " + ufo["state"] 
                + "\nPaís: " + ufo["country"] + "\nDuración (segundos): " + str(ufo["duration (seconds)"]) 
                + "\nForma del objeto: " + ufo["shape"] )
            ultimo = lt.lastElement(listado)
            lt.removeLast(listado)
            lt.addFirst(lst, ultimo)
            i+=1
        print("\n")
        print("Los ultimos 3 avistamientos en la ciudad son: ")
        for h in lt.iterator(lst):
            print("\nDatatime: " + str(h["datetime"]) + "\nCiudad: " + h["city"] + "\nEstado: " + h["state"] 
                + "\nPaís: " + h["country"] + "\nDuración (segundos): " + str(h["duration (seconds)"]) 
                + "\nForma del objeto: " + h["shape"] )
        tiempo_fin=time.process_time()
        TimeMseg=(tiempo_fin-tiempo_inicio)*1000
        print (TimeMseg)        
    
    elif int(inputs[0]) == 4:
        lim1 = input("Escriba el limite inferior en segundos: ")
        lim2 = input("Escriba el limite superior en segundos: ")
        maximo, contador, listado = controller.avistamientos_duracion(catalogo,lim1,lim2)
        tiempo_inicio=time.process_time()

        avistamientos = lt.size(listado)
        tamaño = lt.size(listado)

        print("\n")
        print("El avistamiento mas largo duró: "+str(maximo)+" seg y ocurrió: "+str(contador)+" vez/veces")
        print("\n")
        print("Hay "+str(tamaño)+" avistamientos entre "+str(lim1)+" y "+str(lim2))
        
        i = 1
        lst = lt.newList("ARRAY_LIST")
        print("\n")
        print("Los primeros 3 avistamientos en el rango son: ")
        while i <= 3:
            ufo = lt.getElement(listado, i)
            print("\nDatatime: " + str(ufo["datetime"]) + "\nCiudad: " + ufo["city"] + "\nEstado: " + ufo["state"] 
                + "\nPaís: " + ufo["country"] + "\nDuración (segundos): " + str(ufo["duration (seconds)"]) 
                + "\nForma del objeto: " + ufo["shape"] )
            ultimo = lt.lastElement(listado)
            lt.removeLast(listado)
            lt.addFirst(lst, ultimo)
            i+=1
        print("\n")
        print("Los ultimos 3 avistamientos en el rango: ")
        for h in lt.iterator(lst):
            print("\nDatatime: " + str(h["datetime"]) + "\nCiudad: " + h["city"] + "\nEstado: " + h["state"] 
                + "\nPaís: " + h["country"] + "\nDuración (segundos): " + str(h["duration (seconds)"]) 
                + "\nForma del objeto: " + h["shape"] )
        tiempo_fin=time.process_time()
        TimeMseg=(tiempo_fin-tiempo_inicio)*1000
        print (TimeMseg)        

    elif int(inputs[0]) == 7:
        lat_min = input("Escriba el limite minimo de la latitud: ")
        lat_max = input("Escriba el limite maximo de la latitud: ")
        long_min = input("Escriba el limite minimo de la longitud: ")
        long_max = input("Escriba el limite maximo de la longitud: ")
        tiempo_inicio=time.process_time()

        contador, listado = controller.avistamientos_zona(catalogo, round(float(lat_min),2), round(float(lat_max),2), round(float(long_min),2), round(float(long_max),2))

        print("\n")
        print("En el rango especificado hay "+str(contador)+" avistamientos")
        print("\n")

        lst = lt.newList("ARRAY_LIST")
        
        if int(contador) >= 10:
            i = 1
            print("Los primeros 5 avistamientos en el rango son: ")
            while i <= 5:
                ufo = lt.getElement(listado, i)
                print("\nDatatime: " + str(ufo["datetime"]) + "\nCiudad: " + ufo["city"] + "\nEstado: " + ufo["state"] 
                    + "\nPaís: " + ufo["country"] + "\nForma del objeto: " + ufo["shape"] 
                    + "\nDuración (segundos): " + str(ufo["duration (seconds)"]) + "\nLatitud " + ufo["latitude"] 
                    + "\nLongitud " + ufo["longitude"])
                ultimo = lt.lastElement(listado)
                lt.removeLast(listado)
                lt.addFirst(lst, ultimo)
                i+=1
            print("\n")
            print("Los ultimos 5 avistamientos en el rango: ")
            for h in lt.iterator(lst):
                print("\nDatatime: " + str(h["datetime"]) + "\nCiudad: " + h["city"] + "\nEstado: " + h["state"] 
                    + "\nPaís: " + h["country"] + "\nForma del objeto: " + h["shape"] 
                    + "\nDuración (segundos): " + str(h["duration (seconds)"]) + "\nLatitud " + h["latitude"] 
                    + "\nLongitud " + h["longitude"])
            
        elif int(contador) == 1:
            ufo = lt.getElement(listado,1)
            print("\nDatatime: " + str(ufo["datetime"]) + "\nCiudad: " + ufo["city"] + "\nEstado: " + ufo["state"] 
                    + "\nPaís: " + ufo["country"] + "\nForma del objeto: " + ufo["shape"] 
                    + "\nDuración (segundos): " + str(ufo["duration (seconds)"]) + "\nLatitud " + ufo["latitude"] 
                    + "\nLongitud " + ufo["longitude"])
        
        elif int(contador) < 10 and int(contador) != 1:
            j=1
            mitad = int(contador/2)
            print("Los primeros "+ str(mitad) +" avistamientos en el rango son: ")  
            while j <= mitad:
                ufo = lt.getElement(listado, j)
                print("\nDatatime: " + str(ufo["datetime"]) + "\nCiudad: " + ufo["city"] + "\nEstado: " + ufo["state"] 
                    + "\nPaís: " + ufo["country"] + "\nForma del objeto: " + ufo["shape"] 
                    + "\nDuración (segundos): " + str(ufo["duration (seconds)"]) + "\nLatitud " + ufo["latitude"] 
                    + "\nLongitud " + ufo["longitude"])
                ultimo = lt.lastElement(listado)
                lt.removeLast(listado)
                lt.addFirst(lst, ultimo)
                j+=1

            print("\n")
            print("Los ultimos "+ str(mitad) +" avistamientos en el rango son: ")
            for n in lt.iterator(lst):
                print("\nDatatime: " + str(n["datetime"]) + "\nCiudad: " + n["city"] + "\nEstado: " + n["state"] 
                    + "\nPaís: " + n["country"] + "\nForma del objeto: " + n["shape"] 
                    + "\nDuración (segundos): " + str(n["duration (seconds)"]) + "\nLatitud " + n["latitude"] 
                    + "\nLongitud " + n["longitude"])
        tiempo_fin=time.process_time()
        TimeMseg=(tiempo_fin-tiempo_inicio)*1000
        print (TimeMseg)

    elif int(inputs[0]) == 6:
        lim = input("Escriba el limite inferior en formato (AAAA-MM-DD): ")
        lim2 = input("Escriba el limite superior formato (AAAA-MM-DD): ")
        lim3=lim2+"24:60:01"
        tiempo_inicio=time.process_time()
        maximo, contador, listado = controller.avistamientos_Fecha(catalogo,lim,lim3)

        avistamientos = lt.size(listado)
        tamaño = lt.size(listado)

        print("\n")
        print("El avistamiento que ocurrio mas tarde fue a las: "+str(maximo)+" y ocurrió: "+str(contador)+" vez/veces")
        print("\n")
        print("Hay "+str(tamaño)+" avistamientos entre "+str(lim)+" y "+str(lim2))
        
        i = 1
        lst = lt.newList("ARRAY_LIST")
        print("\n")
        print("Los primeros 3 avistamientos en el rango son: ")
        while i <= 3:
            ufo = lt.getElement(listado, i)
            print("\nDatatime: " + str(ufo["datetime"]) + "\nCiudad: " + ufo["city"] + "\nEstado: " + ufo["state"] 
                + "\nPaís: " + ufo["country"] + "\nDuración (segundos): " + str(ufo["duration (seconds)"]) 
                + "\nForma del objeto: " + ufo["shape"] )
            ultimo = lt.lastElement(listado)
            lt.removeLast(listado)
            lt.addFirst(lst, ultimo)
            i+=1
        print("\n")
        print("Los ultimos 3 avistamientos en el rango: ")
        for h in lt.iterator(lst):
            print("\nDatatime: " + str(h["datetime"]) + "\nCiudad: " + h["city"] + "\nEstado: " + h["state"] 
                + "\nPaís: " + h["country"] + "\nDuración (segundos): " + str(h["duration (seconds)"]) 
                + "\nForma del objeto: " + h["shape"] )
        tiempo_fin=time.process_time()
        TimeMseg=(tiempo_fin-tiempo_inicio)*1000
        print (TimeMseg)        
    elif int(inputs[0]) == 5:
        lim = input("Escriba el limite inferior en formato (horas:minutos): ")
        lim2 = input("Escriba el limite superior formato (horas:minutos): ")
        lim3=lim2+":01"
        tiempo_inicio=time.process_time()
        maximo, contador, listado = controller.avistamientos_Hora(catalogo,lim,lim3)

        avistamientos = lt.size(listado)
        tamaño = lt.size(listado)

        print("\n")
        print("El avistamiento que ocurrio mas tarde fue a las: "+str(maximo)+" y ocurrió: "+str(contador)+" vez/veces")
        print("\n")
        print("Hay "+str(tamaño)+" avistamientos entre las "+str(lim)+" y las"+str(lim2))
        
        i = 1
        lst = lt.newList("ARRAY_LIST")
        print("\n")
        print("Los primeros 3 avistamientos en el rango son: ")
        while i <= 3:
            ufo = lt.getElement(listado, i)
            print("\nDatatime: " + str(ufo["datetime"]) + "\nCiudad: " + ufo["city"] + "\nEstado: " + ufo["state"] 
                + "\nPaís: " + ufo["country"] + "\nDuración (segundos): " + str(ufo["duration (seconds)"]) 
                + "\nForma del objeto: " + ufo["shape"] )
            ultimo = lt.lastElement(listado)
            lt.removeLast(listado)
            lt.addFirst(lst, ultimo)
            i+=1
        print("\n")
        print("Los ultimos 3 avistamientos en el rango: ")
        for h in lt.iterator(lst):
            print("\nDatatime: " + str(h["datetime"]) + "\nCiudad: " + h["city"] + "\nEstado: " + h["state"] 
                + "\nPaís: " + h["country"] + "\nDuración (segundos): " + str(h["duration (seconds)"]) 
                + "\nForma del objeto: " + h["shape"] )  
        tiempo_fin=time.process_time()
        TimeMseg=(tiempo_fin-tiempo_inicio)*1000
        print (TimeMseg)        

    else:
        sys.exit(0)       
sys.exit(0)

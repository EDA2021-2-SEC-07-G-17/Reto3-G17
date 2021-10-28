"""
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
    print("4- Contar los avistamientos por duracion->Req 2")
    print("5- Contar avistamientos por Hora/Minutos del día->Req 3")
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


    else:
        sys.exit(0)
sys.exit(0)

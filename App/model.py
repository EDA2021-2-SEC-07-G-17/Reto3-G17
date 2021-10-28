"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as mg
import datetime
from time import strptime
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def init_catalog():
    catalog = {
        "ufos":None,
        "lista_ufos":None
    }

    catalog["ufos"] = om.newMap(omaptype="RBT",comparefunction=compareDates)
    catalog["lista_ufos"] = lt.newList(datastructure="SINGLE_LINKED")

    return catalog

# Funciones para agregar informacion al catalogo
def ufo_lista(catalog, ufo):
    lt.addLast(catalog["lista_ufos"],ufo)

def addufo(catalog, ufo):
    fecha_ufo = ufo["datetime"]
    existencia = om.get(catalog["ufos"],fecha_ufo)
    if existencia is None:
        lista_ufos = lt.newList(datastructure="SINGLE_LINKED", cmpfunction=compareDates)
        lt.addLast(lista_ufos,ufo)
        om.put(catalog["ufos"],fecha_ufo,lista_ufos)
    else:
        lista = me.getValue(existencia)
        lt.addLast(lista,ufo)
        om.put(catalog["ufos"],fecha_ufo,lista)



# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

def compareDates(date1, date2):
    """
    Compara dos fechas
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1

def comparara_fechas(ufo1, ufo2):
    date1 = ufo1['datetime']
    date2 = ufo2['datetime']
    date1 = strptime(date1, '%Y-%m-%d %H:%M:%S')
    date2 = strptime(date2, '%Y-%m-%d %H:%M:%S')
    return date1 < date2

# Funciones de ordenamiento

def ordenar_fechas(lst):
    mg.sort(lst, comparara_fechas)
    return lst

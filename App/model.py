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


from os import _AddedDllDirectory
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
        "lista_ufos":None,
        "duration":None,
        "hora/minuto":None,
        "ciudades":None,
        "fecha":None
    }

    catalog["ufos"] = om.newMap(omaptype="RBT",comparefunction=compareDates)
    catalog["lista_ufos"] = lt.newList(datastructure="SINGLE_LINKED")
    catalog["duration"] = om.newMap(omaptype="RBT",comparefunction=comparar_duraciones)
    catalog["ciudades"] = om.newMap(omaptype="RBT")
    catalog["hora/minuto"] = om.newMap(omaptype="RBT")
    catalog["fecha"] = om.newMap(omaptype="RBT")

    return catalog

# Funciones para agregar informacion al catalogo
def ufo_lista(catalog, ufo):
    lt.addLast(catalog["lista_ufos"], ufo)
    addDuration(catalog, ufo)
    addCity(catalog, ufo)
    addHora(catalog, ufo)
    addFecha(catalog, ufo)

def addufo(catalog, ufo):
    fecha_ufo = ufo["datetime"]
    existencia = om.get(catalog["ufos"],fecha_ufo)
    if existencia is None:
        lista_ufos = lt.newList(datastructure="SINGLE_LINKED")
        lt.addLast(lista_ufos,ufo)
        om.put(catalog["ufos"],fecha_ufo,lista_ufos)
    else:
        lista = me.getValue(existencia)
        lt.addLast(lista,ufo)
        om.put(catalog["ufos"],fecha_ufo,lista)

def addDuration(catalog, ufo):
    mapa = catalog["duration"]
    duracion = ufo["duration (seconds)"]

    existencia = om.get(mapa,duracion)

    if existencia is None:
        bucket = lt.newList(datastructure="SINGLE_LINKED",cmpfunction=comparar_duraciones)
        lt.addLast(bucket, ufo)
        om.put(mapa, duracion, bucket)
    else:
        bucket_e = me.getValue(existencia)
        lt.addLast(bucket_e, ufo)
        ordenar_ciudades_alfabeticamente(bucket_e)
        om.put(mapa, duracion, bucket_e)
    
    return mapa
def addHora(catalog, ufo):
    mapa = catalog["hora/minuto"]
    fecha = (ufo["datetime"].split())[1]

    existencia = om.get(mapa,fecha)

    if existencia is None:
        bucket = lt.newList(datastructure="SINGLE_LINKED",cmpfunction=comparar_hora)
        lt.addLast(bucket, ufo)
        om.put(mapa, fecha, bucket)
    else:
        bucket_e = me.getValue(existencia)
        lt.addLast(bucket_e, ufo)
        ordenar_fechas(bucket_e)
        om.put(mapa, fecha, bucket_e)
    
    return mapa 
def addFecha(catalog, ufo):
    mapa = catalog["fecha"]
    fecha = ufo["datetime"].split()[0]

    existencia = om.get(mapa,fecha)

    if existencia is None:
        bucket = lt.newList(datastructure="SINGLE_LINKED",cmpfunction=comparar_hora)
        lt.addLast(bucket, ufo)
        om.put(mapa, fecha, bucket)
    else:
        bucket_e = me.getValue(existencia)
        lt.addLast(bucket_e, ufo)
        ordenar_fechas(bucket_e)
        om.put(mapa, fecha, bucket_e)
    
    return mapa        

def addCity(catalog, ufo):
    mapa = catalog["ciudades"]
    ciudad = ufo["city"]

    existencia = om.get(mapa,ciudad)

    if existencia is None:
        bucket = lt.newList(datastructure="SINGLE_LINKED",cmpfunction=comparar_ciudades)
        lt.addLast(bucket, ufo)
        om.put(mapa, ciudad, bucket)
    else:
        bucket_e = me.getValue(existencia)
        lt.addLast(bucket_e, ufo)
        ordenar_fechas(bucket_e)
        om.put(mapa, ciudad, bucket_e)
    
    return mapa


# Funciones para creacion de datos

# Funciones de consulta

def avistamientos_ciudad(catalog, ciudad):
    mapa = catalog["ciudades"]

    ciudades = om.keySet(mapa)
    total = lt.size(ciudades)
    ciu = om.get(mapa,ciudad)
    avistamientos = me.getValue(ciu)
    contador = lt.size(avistamientos)
    
    return total, contador, avistamientos

def avistamientos_duracion(catalog, lim1, lim2):
    mapa = catalog["duration"]
    maximo = om.maxKey(mapa)
    tupla_maximo = om.get(mapa, maximo)
    bucket_maximo = me.getValue(tupla_maximo)
    
    contador = lt.size(bucket_maximo)

    lista_rango = om.keys(mapa, float(lim1), float(lim2))

    lista_final = lt.newList(datastructure="SINGLE_LINKED", cmpfunction=comparar_duraciones)

    for key in lt.iterator(lista_rango):
        ufo = om.get(mapa, key)
        bucket = me.getValue(ufo)
        
        for e in lt.iterator(bucket):
            lt.addLast(lista_final, e)

    return maximo, contador, lista_final
def avistamientos_Hora(catalog, lim1, lim2):
    mapa = catalog["hora/minuto"]
    maximo = om.maxKey(mapa)
    tupla_maximo = om.get(mapa, maximo)
    bucket_maximo = me.getValue(tupla_maximo)
    
    contador = lt.size(bucket_maximo)

    lista_rango = om.keys(mapa, lim1,lim2)

    lista_final = lt.newList(datastructure="SINGLE_LINKED", cmpfunction=comparar_hora)

    for key in lt.iterator(lista_rango):
        ufo = om.get(mapa, key)
        bucket = me.getValue(ufo)
        
        for e in lt.iterator(bucket):
            lt.addLast(lista_final, e)

    return maximo, contador, lista_final
def avistamientos_Fecha(catalog, lim1, lim2):
    mapa = catalog["fecha"]
    maximo = om.minKey(mapa)
    tupla_maximo = om.get(mapa, maximo)
    bucket_maximo = me.getValue(tupla_maximo)
    
    contador = lt.size(bucket_maximo)

    lista_rango = om.keys(mapa, lim1,lim2)

    lista_final = lt.newList(datastructure="SINGLE_LINKED", cmpfunction=comparar_hora)

    for key in lt.iterator(lista_rango):
        ufo = om.get(mapa, key)
        bucket = me.getValue(ufo)
        
        for e in lt.iterator(bucket):
            lt.addLast(lista_final, e)

    return maximo, contador, lista_final



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

def comparar_duraciones(d1, d2):
    if (float(d1) == float(d2)):
        return 0
    elif (float(d1) > float(d2)):
        return 1
    else:
        return -1

def comparar_ciudades(ciu1, ciu2):
    ciudad1 = ciu1["city"]
    ciudad2 = ciu2["city"]
    lista = [str(ciudad1),str(ciudad2)]
    orden = ordenar_alfabeticamente(lista)

    if str(ciudad1) == orden[0]:
        return True
    else:
        return False
def comparar_hora(d1, d2):
    if (d1 == d2):
        return 0
    elif (d1[1] > d2[1]):
        return 1
    else:
        return -1        

# Funciones de ordenamiento

def ordenar_fechas(lst):
    mg.sort(lst, comparara_fechas)
    return lst

def ordenar_ciudades_alfabeticamente(lst):
    mg.sort(lst, comparar_ciudades)
    return lst
    

# Funciones de apoyo

def ordenar_alfabeticamente(lista):
    lista.sort()
    return lista

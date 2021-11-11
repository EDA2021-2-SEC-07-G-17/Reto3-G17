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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def iniciar_catalogo():
    catalogo = model.init_catalog()
    return catalogo

# Funciones para la carga de datos
def loadData(catalogo, ufosfile):

    ufofile = cf.data_dir + ufosfile
    input_file = csv.DictReader(open(ufofile, encoding="utf-8"),
                                delimiter=",")
    for ufo in input_file:
        model.addufo(catalogo, ufo)
        model.ufo_lista(catalogo, ufo)
        
    model.ordenar_fechas(catalogo['lista_ufos'])
    return catalogo

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

def avistamientos_ciudad(catalogo, ciudad):
    total, contador, avistamientos = model.avistamientos_ciudad(catalogo, ciudad)
    return total, contador, avistamientos

def avistamientos_duracion(catalogo, lim1, lim2):
    maximo, contador, listado = model.avistamientos_duracion(catalogo,lim1,lim2)
    return maximo, contador, listado

def avistamientos_zona(catalogo, lat_min, lat_max, long_min, long_max):
    contador, listado = model.avistamientos_zona_geografica(catalogo, lat_min, lat_max, long_min, long_max)
    return contador, listado

def avistamientos_Hora(catalogo, lim1, lim2):
    maximo, contador, listado = model.avistamientos_Hora(catalogo,lim1,lim2)
    return maximo, contador, listado 
    
def avistamientos_Fecha(catalogo, lim1, lim2):
    maximo, contador, listado = model.avistamientos_Fecha(catalogo,lim1,lim2)
    return maximo, contador, listado        

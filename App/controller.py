﻿"""
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
import time
import tracemalloc
def initCatalog(tipo):
    catalog=model.newCatalog(tipo)
    return catalog

    

# Funciones para la carga de datos
def loadData(catalog):
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()

    start_time = getTime()
    start_memory = getMemory()


    loadVideos(catalog)
    loadCategories(catalog)
    
    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)
    return delta_time,delta_memory

def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def getMemory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def deltaMemory(start_memory, stop_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory

def loadVideos(catalog):
    
    file_name=cf.data_dir + "videos-large.csv"
    input_file=csv.DictReader(open(file_name,encoding="utf-8"))
    i=0
    for video in input_file:
        i+=1
        model.addVideo(catalog,video)
        model.addCategory_videos(catalog,video)
        model.addCountry(catalog,video)
    print("Cantidad de videos cargados: ", i)

    

def loadCategories(catalog):
    file_name=cf.data_dir + "category-id.csv"
    input_file=csv.DictReader(open(file_name,encoding="utf-8"),delimiter="\t")
    i=0
    for categoria in input_file:
        model.addCategory(catalog, categoria)
        i+=1
    print("Cantidad de categorias cargadas: ",i)
# Funciones de ordenamiento

def videosLikesCategory(catalog, category):
    return model.videosLikesCategory(catalog,category)

def requerimiento1(catalog,country,category):
    return model.requerimiento1(catalog,country,category)
def requerimiento2(catalog,country):
    return model.requerimiento2(catalog,country)
def requerimientos3(catalog,nombres):
    return model.requerimiento3(catalog,nombres)    
def requerimiento4(country,tag,catalog):
    return model.requerimiento4(country,tag,catalog)


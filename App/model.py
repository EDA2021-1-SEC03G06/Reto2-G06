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
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import insertionsort as si
from DISClib.Algorithms.Sorting import quicksort as qs
from DISClib.Algorithms.Sorting import mergesort as ms
import time
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
# Construccion de modelos
def newCatalog(tipo):
    catalog={ "videos" : None,
               "Category" : None,
               "Category-videos":None}

    catalog["videos"] = lt.newList(tipo)
    
    catalog["category"]=lt.newList(tipo)
    catalog["category-videos"]=mp.newMap(100,maptype='PROBING',loadfactor=0.5)

    return catalog


# Funciones para agregar informacion al catalogo

def addVideo(catalog,video):
    lt.addLast(catalog["videos"],video)

def addCategory(catalog,category):
    category["name"]=category["name"].strip()
    lt.addLast(catalog["category"],category)
    
def addCategory_videos(catalog,video):
    categories=catalog["category-videos"]
    category=int(video["category_id"])

    flag=mp.contains(categories,category)
    if flag:
        couple=mp.get(categories,category)
        lista=me.getValue(couple)
    else:
        lista=lt.newList(datastructure='ARRAY_LIST')
        mp.put(categories,category,lista)
        
    lt.addLast(lista,video)

# Funciones para creacion de datos

def newCategory(id,name):
    diccionario={ "id": id,"name":name}
    return diccionario

# Funciones de consulta


def getCategoryNumber(nombre,catalog):
    categorias=catalog["category"]
    size=lt.size(categorias)
    
    for i in range(1,size+1):
        elemento=lt.getElement(categorias,i)
        if elemento["name"]==nombre:
            print(elemento["id"])
            return int(elemento["id"])

# Funciones utilizadas para comparar elementos dentro de una lista
def cmpVideosByViewsDescendant(video1,video2):
   return int(video1["views"])< int(video2["views"])

def cmpVideosByvViewsAscendant(video1,video2):
    return int(video1["views"])>int(video2["views"])

def cmpVideosByCountry(pais,video):
    return str(video["country"])==str(pais)
def cmpVideosByCategory(numero,video):
    return int(video["category_id"])==int(numero)
def cmpVideosById(video1,video2):
    return video1["video_id"]<video2["video_id"]

def cmpVideosByTag(tag,video):
    return tag in video["tags"]   
def cmpByCategory(category1,category2):
    return int(category1)>int(category2)
def cmpVideosByLikes(video1,video2):
    return int(video1["likes"])>int(video2["likes"])
def cmpVideosByTitle(video1,video2):
    return video1["title"]<video2["title"]

# Funciones de ordenamiento
def selectionSort(lista,numero):
    numero=int(numero)
    start_time = time.process_time()
    if numero==1:
        se.sort(lista, cmpVideosByvViewsAscendant)
        stop_time = time.process_time()
    elif numero==2:
        se.sort(lista,cmpVideosByViewsDescendant)
        stop_time = time.process_time()
    elif numero==3:
        se.sort(lista,cmpVideosById)
        stop_time = time.process_time()
    else:
        se.sort(lista,cmpVideosByLikes)
        stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return lista,elapsed_time_mseg

def insertionSort(lista,numero):
    numero=int(numero)
    start_time = time.process_time()
    if numero==1:
        si.sort(lista, cmpVideosByvViewsAscendant)
        stop_time = time.process_time()
    elif numero==2:
        si.sort(lista,cmpVideosByViewsDescendant)
        stop_time = time.process_time()
    elif numero==3:
        si.sort(lista,cmpVideosById)
        stop_time = time.process_time()
    else:
        si.sort(lista,cmpVideosByLikes)
        stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return lista,elapsed_time_mseg

def shellSort(lista,numero):
    numero=int(numero)
    start_time = time.process_time()
    if numero==1:
        sa.sort(lista, cmpVideosByvViewsAscendant)
        stop_time = time.process_time()
    elif numero==2:
        sa.sort(lista,cmpVideosByViewsDescendant)
        stop_time = time.process_time()
    elif numero==3:
        sa.sort(lista,cmpVideosByViewsDescendant)
        stop_time = time.process_time()
    else:
        sa.sort(lista,cmpVideosByLikes)
        stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return lista,elapsed_time_mseg

def mergeSort(lista,numero):
    numero=int(numero)
    start_time = time.process_time()
    if numero==1:
        ms.sort(lista, cmpVideosByvViewsAscendant)
        stop_time = time.process_time()
    elif numero==2:
        ms.sort(lista,cmpVideosByViewsDescendant)
        stop_time = time.process_time()
    elif numero==3:
        ms.sort(lista,cmpVideosById)
        stop_time = time.process_time()
    elif numero==5:
        ms.sort(lista,cmpVideosByTitle)
        stop_time=time.process_time()
    else:
        ms.sort(lista,cmpVideosByLikes)
        stop_time = time.process_time()
        
        
    elapsed_time_mseg = (stop_time - start_time)*1000
    return lista,elapsed_time_mseg


def quickSort(lista,numero):
    numero=int(numero)
    start_time = time.process_time()
    if numero==1:
        qs.sort(lista, cmpVideosByvViewsAscendant)
        stop_time = time.process_time()
    elif numero==2:
        qs.sort(lista,cmpVideosByViewsDescendant)
        stop_time = time.process_time()
    elif numero==3:
        qs.sort(lista,cmpVideosById)
        stop_time = time.process_time()
    else:
        qs.sort(lista,cmpVideosByLikes)
        stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return lista,elapsed_time_mseg

def videosLikesCategory(catalog,category):

    number=getCategoryNumber(category,catalog)
    videos=catalog["category-videos"]
    couple=mp.get(videos,number)
    lista=me.getValue(couple)

    ordenada=mergeSort(lista,4)[0]
    
    return ordenada


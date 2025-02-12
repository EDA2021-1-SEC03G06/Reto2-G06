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
from DISClib.DataStructures import listiterator as li
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
    
    catalog["category"]=mp.newMap(200,maptype='CHAINING',loadfactor=1.0)
    catalog["category-videos"]=mp.newMap(200,maptype='CHAINING',loadfactor=1.0)
    catalog["countries"]=mp.newMap(200,maptype='CHAINING',loadfactor=1.0)

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
        mp.put(catalog["category-videos"],category,lista)
        
    lt.addLast(lista,video)
def addCountry(catalog,video):
    countries=catalog["countries"]
    country=video["country"].lower()

    flag=mp.contains(countries,country)
    if flag:
        couple=mp.get(countries,country)
        lista=me.getValue(couple)
    else:
        lista=lt.newList(datastructure='ARRAY_LIST')
        mp.put(catalog["countries"],country,lista)
    lt.addLast(lista,video)
# Funciones para creacion de datos

def newCategory(id,name):
    name=name.lower()
    diccionario={ "id": id,"name":name}
    return diccionario

# Funciones de consulta


def getCategoryNumber(nombre,catalog):
    categorias=catalog["category"]
    size=lt.size(categorias)
    iterador=li.newIterator(categorias)
    bandera=True
    numero=0
    while li.hasNext(iterador) and bandera:
        elemento=li.next(iterador)
        if elemento["name"].lower()==nombre.lower():
            print(elemento["id"])
            bandera=False
            numero=elemento["id"]
    return numero

# Funciones utilizadas para comparar elementos dentro de una lista
def cmpVideosByViewsDescendant(video1,video2):
   return int(video1["views"])< int(video2["views"])

def cmpVideosByvViewsAscendant(video1,video2):
    return int(video1["views"])>int(video2["views"])

def cmpVideosByCountry(pais,video):
    return str(video["country"].lower())==str(pais.lower())
def cmpVideosByCategory(numero,video):
    return int(video["category_id"])==int(numero)
def cmpVideosById(video1,video2):
    return video1["video_id"]<video2["video_id"]

def cmpVideosByTag(tag,video):
    return tag.lower() in video["tags"].lower()   
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
    return lista

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
    return lista

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
    return lista

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
    return lista


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
    return lista

def videosLikesCategory(catalog,category):
    
    start_time = time.process_time()

    number=getCategoryNumber(category,catalog)
    videos=catalog["category-videos"]
    couple=mp.get(videos,number)
    lista=me.getValue(couple)

    ordenada=mergeSort(lista,4)[0]
    
    return ordenada

def requerimiento1(catalog,country,category):
    start_time = time.process_time()
    country=country.lower()

    countries=catalog["countries"]
    couple=mp.get(countries,country)
    lista=me.getValue(couple)
    size=lt.size(lista)

    number=getCategoryNumber(category,catalog)
    contador=1
    iterador=li.newIterator(lista)
    i=1
    
    while li.hasNext(iterador):
        video=li.next(iterador)
        if cmpVideosByCategory(number,video):
            lt.exchange(lista,i,contador)
            contador+=1
        i+=1
        
    lista_total=lt.subList(lista,1,contador)
    size=lt.size(lista_total)
    ordenada=mergeSort(lista_total,1)    

    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000

    return ordenada,elapsed_time_mseg

def requerimiento2(catalog,country):
    country=country.lower()
    start_time = time.process_time()
    countries=catalog["countries"]
    couple=mp.get(countries,country)
    lista=me.getValue(couple)

    lista_ordenada=mergeSort(lista,3)

    mayor=lt.getElement(lista_ordenada,1)
    cantidad_mayor=0
    size=lt.size(lista_ordenada)
    print(size)
    iterador=li.newIterator(lista_ordenada)

    cantidad=0
    comparador=mayor
    
    while li.hasNext(iterador):
        video=li.next(iterador)
        if video["video_id"]==comparador["video_id"]:
            cantidad+=1
        else:
            if cantidad>cantidad_mayor:
                mayor=comparador
                cantidad_mayor=cantidad
            cantidad=1
            comparador=video
        
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return mayor,cantidad_mayor,elapsed_time_mseg

def requerimiento3(catalog,nombres):
        
    start_time = time.process_time()
    nombre = nombres.lower()
    number= getCategoryNumber(nombre,catalog)
    categoria=catalog["category-videos"]
    couple =mp.get(categoria,number)
    lista= me.getValue(couple)
    
    lista_ordenada=mergeSort(lista,3)

    mayor=lt.getElement(lista_ordenada,1)
    cantidad_mayor=0
    size=lt.size(lista_ordenada)
    print(size)
    iterador=li.newIterator(lista_ordenada)

    cantidad=0
    comparador=mayor
    
    while li.hasNext(iterador):
        video=li.next(iterador)
        if video["video_id"]==comparador["video_id"]:
            cantidad+=1
        else:
            if cantidad>cantidad_mayor:
                mayor=comparador
                cantidad_mayor=cantidad
            cantidad=1
            comparador=video
        
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return mayor,cantidad_mayor,elapsed_time_mseg


def requerimiento4(country,tag,catalog):
    start_time = time.process_time()
    country=country.lower()
    countries=catalog["countries"]
    couple=mp.get(countries,country)
    lista=me.getValue(couple)

    nueva_lista=lt.newList("ARRAY_LIST")
    iterador=li.newIterator(lista)
    size=lt.size(lista)
    print(size)
    while li.hasNext(iterador):
        video=li.next(iterador)
        if cmpVideosByTag(tag,video):
            lt.addLast(nueva_lista,video)
    print(lt.size(nueva_lista))
    nueva_lista=mergeSort(nueva_lista,4)
    nueva_lista=mergeSort(nueva_lista,3)
    

    lista_ordenada=lt.newList("ARRAY_LIST")
    video=lt.getElement(nueva_lista,1)
    lt.addLast(lista_ordenada,video)

    segundo_iterador=li.newIterator(nueva_lista)
    while li.hasNext(segundo_iterador):
        video=li.next(segundo_iterador)
        comparador=lt.lastElement(lista_ordenada)
        if comparador["title"]!=video["title"]:
            lt.addLast(lista_ordenada,video)
    
    lista_ordenada=mergeSort(lista_ordenada,4)

    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000

    return lista_ordenada,elapsed_time_mseg
    
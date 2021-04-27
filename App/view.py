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
    print("0- Seleccionar tipo de datos")
    print("1- Cargar información en el catálogo")
    print("2-  Encontrar videos con menos vistas")
    print("3-  requerimiento1")
    print("4- requerimiento2")
    print("5- requerimiento3")
    print("6- requerimiento4 ")


catalog = None
reducido= None
"""
Menu principal
"""
def mostrarOrdenamientos():
    print("Seleccione el tipo de ordenamiento iterativo:")
    print("1- selection Sort")
    print("2- Insertion Sort")
    print("3- Shell Sort")
    print("4- quick sort")
    print("5- merge sort")




tipoDato=""
sys.setrecursionlimit(1000*10)
while True:
    printMenu()
    
    inputs = int(input('Seleccione una opción para continuar '))
    if inputs==0:

        x=int(input("Presione 1 para seleccionar arreglos, o 2 para seleccionar listas encadenadas "))
        if x==1:
            tipoDato="ARRAY_LIST"
            print("Array lists")
        elif x==2:
            tipoDato="SINGLE_LINKED"
            print("Single linked")
    elif inputs == 1:
        print("Cargando información de los archivos .... ")
        catalog=controller.initCatalog(tipoDato)
        print(tipoDato)
        deltas=controller.loadData(catalog)
        print("Los datos se han demorado en cargar " ,deltas[0]," Ms")
        print("Al cargar los datos se han ocupado ",deltas[1]," Kb")
       

    elif inputs == 2:
        numero=int(input(("Indique tamaño de la muestra ")))
        tag=input("Indique el tag ")
        lista=controller.videosLikesCategory(catalog,tag)
        for i in range(1,numero):
            video=lt.getElement(lista,i)
            print("titulo: ",video["title"]," id: ",video["category_id"]," likes: ",video["likes"])
    elif inputs==3:
        tamano=int(input("Ingrese la cantidad de videos en el ranking "))
        pais=input("Ingrese el nombre del pais ")
        
        categoria=input("Ingrese la categoria que desea buscar ")
        
        print("cargando...")

        lista=controller.requerimiento1(catalog,pais,categoria)
        
        for i in range(1,tamano+1):
            x=lt.getElement(lista[0],i)
            print(i ," : ","Titulo: ", x["title"]," dia tendencia: ",x["trending_date"]," canal:  ",x["channel_title"]," fecha_publicación:  ",x["publish_time"]," vistas: ",x["views"]," likes:  ",x["likes"]," dislikes: ",x["dislikes"]," pais: ", x["country"]," categoria: ", x["category_id"] )
        print("el algoritmo se demora: ",lista[1]," ms") 
    elif inputs==4:
        pais=input("Ingrese el nombre del pais  ")
        print("cargando...")
        
        video_dias=controller.requerimiento2(catalog,pais)
        video=video_dias[0]
        print("Titulo: ", video["title"] ," Canal: ", video["channel_title"]," Pais: ", video["country"]," dias: ",video_dias[1])
        print("El algoritmo se demora :" , video_dias[2] ," ms")
    elif inputs==5:
        nombres=input("Ingrese la categoria del video  ")
        print ("Cargando...")   
       
        video_cates=controller.requerimientos3(catalog,nombres)
        video=video_cates[0] 
        print(video["title"]," ",video["channel_title"], " ",  video["category_id"]," ",video_cates[1])
        print("el algoritmo se demora :", video_cates[2],"ms")
    elif inputs==6:
        pais=input("Ingrese el nombre del pais ")
        
        numero=int(input("Ingrese la cantidad de videos "))
        tag=input("Ingrese el tag ")
        print("cargando")
        videos=controller.requerimiento4(pais,tag,catalog)
        size=lt.size(videos[0])
        if numero>size:
            numero=size
        for i in range(1,numero+1):
            video=lt.getElement(videos[0],i)
            print(i, " Titulo: ",video["title"]," Canal: ",video["channel_title"]," Fecha Publicación: ",video["publish_time"]," Likes: ",video["likes"]," Pais: ",video["country"])
        print("Tiempo de ejecución: ", videos[1])


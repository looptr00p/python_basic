#Escriba un programa en python que guarde en un archivo de texto una serie de palabras o frases.
#Luego lea el archivo y cada línea de texto del mismo debe ser almacenada en una lista.
#Finalmente, visualice los elementos guardados en la lista. Utilice funciones (def) para cada
#proceso o tarea a realizar.



def crear_archivo():
    #creando y escribiendo en el archivo
    archivo = open('mi_archivo.txt', 'w')
    for k in range(5):
        data = input("Ingrese una palabra o frase: ")
        archivo.write(data+"\n")
    archivo.close()

def leer_archivo_guardar_en_lista():
    global frases
    #Leyendo el archivo
    archivo = open('mi_archivo.txt', 'r')
    for linea in archivo:
        frases.append(linea)
    archivo.close()   

def imprimir_lista():
    for k in frases:
        print(k)
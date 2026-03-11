# FUNDAMENTOS DE PROGRAMACIÓN PARA INGENIERÍA
# FUNDAMENTOS DE COMPUTACIÓN Y PROGRAMACIÓN
# SECCIÓN DEL CURSO: 10145-0-C-1.
# PROFESOR DE TEORÍA: Carlos Vera Escobar.
# PROFESOR DE LABORATORIO: Natalia Snahueza Ruiz.
#
# AUTOR
# NOMBRE: Krishna Carrasco Cueto.
# RUN: 22.022.403-1.
# CARRERA: Bachillerato con mención Ingeniería Civil Informatica.

#Funciones
#Defino una función propia llamada buscar_palabras
def buscar_palabras(frase):
    lista_ini = frase.split() #necesito separar la listas por los espacios y ocupo .split (apuntes listas)
    resultado = []

    for palabr in lista_ini:
        if len(palabr) > 5: #use len para poder contar las letras (apunte strings) 
            letra_sola = True
            for caracter in palabr:
                if not caracter.isalpha(): #ocupo .isalpha para poder ver si el caracter es una letra (apunte strings) 
                    letra_sola = False

            if letra_sola:
                resultado.append(palabr) #ocupe .append el cual agrega un elemento al final de la lista (apunte listas)
                
    return resultado #para dar a termino a la funcion que cree , se debe utilizar return (apunte funciones propias)

#Defino la segunda funcion propia contar
def contar(lista):
    contador_palabr = 0
    vocales ="aeiouáéíóúÁÉÍÓÚAEIOU"
    #debo hacer un contador para que pueda contar las vocales(lab del sabado)
    for palabr in lista:
        numero_vocals = 0
        num_consonantes = 0

        for letra in palabr:
            if letra in vocales:
                numero_vocals += 1
            else:
                num_consonantes += 1

        if num_consonantes > numero_vocals: #criterio de tener más consonantes que vocales 
            contador_palabr += 1
            
    return contador_palabr #para dar a termino a la funcion que cree , se debe utilizar return (apunte funciones propias)

#Defino la funcion propia de seleccionar_respuesta
def seleccionar_respuesta(respuesta, numero):
    list_respues = respuesta.split("/") #use .split para poder poner el separador (apuntes listas) 
    cant_elemen = len(list_respues) #use len para poder contar las letras (apunte strings)

    indic_final = numero % cant_elemen #para poder manejar el comportamiento del contador si el numero es mayor o largo, lo que hace es reiniciar el conteo 

    return list_respues[indic_final] #para dar a termino a la funcion que cree , se debe utilizar return (apunte funciones propias)


                    
            

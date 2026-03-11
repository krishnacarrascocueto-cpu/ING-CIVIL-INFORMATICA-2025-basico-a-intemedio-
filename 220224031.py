# FUNDAMENTOS DE PROGRAMACIÓN PARA INGENIERÍA
# FUNDAMENTOS DE COMPUTACIÓN Y PROGRAMACIÓN
# SECCIÓN DEL CURSO: 10145-0-C-1
# PROFESOR DE TEORÍA: Carlos Vera Escobar 
# PROFESOR DE LABORATORIO: Natalia Sanhueza Ruiz
#
# AUTOR
# NOMBRE: Krishna Carrasco Cueto
# RUN:22.022.403-1
# CARRERA: Bachillerato con mención Ingeniería Civil Informática

#Entrada

resultadosp1_str = input("Ingrese los resultados de los jugadores 1: ")
resultadosp2_str = input("Ingrese los resultados de los jugadores 2: ")

#Proceso y Salida


if len(resultadosp1_str) != len(resultadosp2_str):
    print("Las cantidades de versus no concuerdan.")
else:
    cantidad_sets_total = len(resultadosp1_str)

    
    if cantidad_sets_total == 0:
        print("No corresponde a la cantidad de enfretamientos de un torneo.")
    else:
        cant_parti = cantidad_sets_total + 1
        cant_valida = True

        
        if cant_parti < 2:
            cant_valida = False
        else:
           
            temp_parti = cant_parti 
            sigue_prob = True
            
            while temp_parti > 1 and sigue_prob == True:
                if temp_parti % 2 != 0:
                    cant_valida = False
                    sigue_prob = False
                else:
                    temp_parti = temp_parti // 2

        if cant_valida == False:
            print("No corresponde a la cantidad de enfretamientos de un torneo.")
        else:
            
            participantes_1pt = []
            for caracter in resultadosp1_str:
                participantes_1pt.append(int(caracter))
            
            participantes_2pt = []
            for caracter in resultadosp2_str:
                participantes_2pt.append(int(caracter))
            
            
            error = False
            i = 0
            while i < cantidad_sets_total:
                
                p1 = participantes_1pt[i]
                p2 = participantes_2pt[i]
                num_par = i + 1
                nombr_rond = ""
                set_val = False

                
                if i == cantidad_sets_total - 1:
                    nombr_rond = "(Final)"
                   
                    if (p1 == 3 and p2 <= 2) or (p2 == 3 and p1 <= 2):
                        set_val = True
                elif i >= cantidad_sets_total - 3 and cantidad_sets_total >= 3:
                    nombr_rond = "(Semis)"
                    
                    if (p1 == 3 and p2 <= 2) or (p2 == 3 and p1 <= 2):
                        set_val = True
                elif i >= cantidad_sets_total - 7 and cantidad_sets_total >= 7:
                    nombr_rond = "(Cuartos)"
                    
                    if (p1 == 2 and p2 <= 1) or (p2 == 2 and p1 <= 1):
                        set_val = True
                elif i >= cantidad_sets_total - 15 and cantidad_sets_total >= 15:
                    nombr_rond = "(Octavos)"
                    
                    if (p1 == 2 and p2 <= 1) or (p2 == 2 and p1 <= 1):
                        set_val = True
                else:
                    
                    if (p1 == 2 and p2 <= 1) or (p2 == 2 and p1 <= 1):
                        set_val = True

                
                if set_val == False:
                    error = True
                   
                    if nombr_rond != "":
                        print("Partida " + str(num_par) + " " + nombr_rond + ": Cantidad incorrecta de sets. " + str(p1) + " vs " + str(p2))
                    else:
                        print("Partida " + str(num_par) + ": Cantidad incorrecta de sets. " + str(p1) + " vs " + str(p2))

                i = i + 1

            if error == False:
                print("Torneo correcto.")
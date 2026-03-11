# FUNDAMENTOS DE PROGRAMACIÓN PARA INGENIERÍA 
#FUNDAMENTOS DE COMPUTACIÓN Y PROGRAMACIÓN 
# 
# AUTOR 
# NOMBRE: Krishna Carrasco Cueto
# RUN: 22.022.403-1

#Entrada
controles_prom = float(input("Ingrese el promedio de controles: "))
promed_act_clases = float(input("Ingrese el promedio de actividades en clase: "))
pep1_not = float(input("Ingrese la nota de prueba 1: "))
pep2_not = float(input("Ingrese la nota de prueba 2: "))
porcent_asis = float(input("Ingrese el porcentaje de asistencia a clase: "))

#Proceso y salida

promedio_controles = controles_prom * 0.25
promedio_actividades_clases = promed_act_clases * 0.15
promedio_pep1 = pep1_not * 0.30
promedio_pep2 = pep2_not * 0.30
promedio_general = promedio_controles + promedio_actividades_clases + promedio_pep1 + promedio_pep2

if pep1_not > pep2_not:
    nota_mejor = pep1_not
else:
    nota_mejor = pep2_not

por_nota = (3.95 - ((controles_prom * 0.25) + (promed_act_clases * 0.15) + (nota_mejor * 0.30))) / 0.30

if round(por_nota, 1) < por_nota:
    por_nota = round(por_nota + 0.05, 1)
else:
    por_nota = round(por_nota, 1)

if porcent_asis < 75 and promedio_general > 4.0:
    print("Reprobaste. Tu promedio final fue de 3.5")
elif promedio_general >= 4.0:
    print("Aprobaste! Tu promedio final fue de", round(promedio_general, 1))
elif promedio_general >= 3.0 and promedio_general < 4.0:
    print("Debes rendir POR. Tu promedio final fue de", round(promedio_general, 1), "- necesitas",por_nota,"para aprobar")
else:
    print("Reprobaste. Tu promedio final fue de", round(promedio_general, 1))



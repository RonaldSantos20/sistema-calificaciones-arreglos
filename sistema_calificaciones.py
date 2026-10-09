"""Sistema introductorio para consultar y procesar calificaciones usando listas."""

# Vector inicial: las calificaciones de cinco estudiantes.
calificaciones = [85, 67, 92, 74, 58]

print("=" * 48)
print(" SISTEMA DE CALIFICACIONES - ARREGLOS/VECTORES")
print("=" * 48)
print("Calificaciones iniciales:", calificaciones)
print("Cantidad de estudiantes:", len(calificaciones))

# Consulta de un elemento por medio de su indice.
try:
    indice_consulta = int(input("\nIndique el indice que desea consultar (0-4): "))
    if 0 <= indice_consulta < len(calificaciones):
        print("Calificacion en el indice", indice_consulta, "=", calificaciones[indice_consulta])
    else:
        print("Indice fuera de rango. No existe esa posicion en el vector.")
except ValueError:
    print("Entrada no valida: escriba un numero entero para el indice.")

# Modificacion de un elemento, luego de validar el indice y la calificacion.
try:
    indice_modificar = int(input("\nIndique el indice que desea modificar (0-4): "))
    if 0 <= indice_modificar < len(calificaciones):
        nueva_calificacion = int(input("Escriba la nueva calificacion (0-100): "))
        if 0 <= nueva_calificacion <= 100:
            anterior = calificaciones[indice_modificar]
            calificaciones[indice_modificar] = nueva_calificacion
            print("Se cambio la calificacion del indice", indice_modificar,
                  "de", anterior, "a", nueva_calificacion, ".")
        else:
            print("Calificacion no valida: debe estar entre 0 y 100.")
    else:
        print("Indice fuera de rango. No se modifico el vector.")
except ValueError:
    print("Entrada no valida: escriba numeros enteros.")

# Recorrido del vector: clasifica cada estudiante usando una condicion if.
aprobados = 0
reprobados = 0
print("\nResultados por estudiante (se aprueba con 70 o mas):")
for indice, nota in enumerate(calificaciones):
    if nota >= 70:
        estado = "Aprobo"
        aprobados += 1
    else:
        estado = "Reprobo"
        reprobados += 1
    print("Indice", indice, "- Calificacion:", nota, "-", estado)

# Calculos y resultados generales.
promedio = sum(calificaciones) / len(calificaciones)
print("\nRESUMEN FINAL")
print("Promedio:", round(promedio, 2))
print("Calificacion mas alta:", max(calificaciones))
print("Calificacion mas baja:", min(calificaciones))
print("Estudiantes aprobados:", aprobados)
print("Estudiantes reprobados:", reprobados)
print("Vector actualizado:", calificaciones)
print("\nPrograma finalizado correctamente.")

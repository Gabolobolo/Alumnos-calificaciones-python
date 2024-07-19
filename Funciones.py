def imprimir_alumnos(alumnos, notas):
    print("Nombre\t\tApellido\t\tPromedio\t\tAprobacion")
    for i in range(len(alumnos)):
        promedio = sum(notas[i]) / len(notas[i])
        print(f"{alumnos[i][0]}\t\t{alumnos[i][1]}\t\t{promedio:.2f}\t\t{'Aprobado' if promedio >= 6 else 'Reprobado'}")

def buscar_alumno_por_apellido(alumnos, notas):
    apellido = input("Ingrese el apellido del alumno a buscar: ")
    encontrado = False
    print("Nombre\t\tApellido\t\tPromedio\t\tAprobacion")
    for i in range(len(alumnos)):
        if alumnos[i][1] == apellido:
            promedio = sum(notas[i]) / len(notas[i])
            print(f"{alumnos[i][0]}\t\t{alumnos[i][1]}\t\t{promedio:.2f}\t\t{'Aprobado' if promedio >= 6 else 'Reprobado'}")
            encontrado = True
            break
    if not encontrado:
        print("No se encontró ningún alumno con ese apellido.")

def editar_calificaciones(alumnos, notas):
    apellido = input("Ingrese el apellido del alumno para editar calificaciones: ")
    encontrado = False
    for i in range(len(alumnos)):
        if alumnos[i][1] == apellido:
            nuevas_notas = input(f"Ingrese las nuevas calificaciones para {alumnos[i][0]} {alumnos[i][1]} (separadas por espacios): ")
            nuevas_notas = list(map(float, nuevas_notas.split()))
            notas[i] = nuevas_notas
            print(f"Calificaciones actualizadas para {alumnos[i][0]} {alumnos[i][1]}.")
            encontrado = True
            break
    if not encontrado:
        print("No se encontró ningún alumno con ese apellido.")

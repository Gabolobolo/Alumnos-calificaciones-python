import funciones

alumnos = [
    ["Juan", "Perez"],
    ["Ana", "Garcia"],
    ["Luis", "Martinez"],
    ["Maria", "Rodriguez"],
    ["Carlos", "Lopez"],
    ["Sofia", "Gonzalez"]
]

notas = [
    [5.0, 7.0, 6.0],
    [8.0, 9.0, 7.0],
    [4.0, 6.0, 5.0],
    [7.0, 8.0, 9.0],
    [3.0, 5.0, 4.0],
    [9.0, 10.0, 9.0]
]

# Llamadas de prueba
funciones.imprimir_alumnos(alumnos, notas)
funciones.buscar_alumno_por_apellido(alumnos, notas)
funciones.editar_calificaciones(alumnos, notas)
funciones.imprimir_alumnos(alumnos, notas)

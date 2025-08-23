def agregar(lista_estudiantes,nombre):
    lista_estudiantes.append(nombre)
    return lista_estudiantes
def listar_estudiantes(lista_estudiantes):
    print("Mi lista de estudiantes")
    for i,estudiante in enumerate(lista_estudiantes,1):
        print(f"{i}: {estudiante}")
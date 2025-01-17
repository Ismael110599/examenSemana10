# Nodo de tarea (Lista Enlazada)
class NodoTarea:
    def __init__(self, nombre, descripcion, estado="pendiente"):
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado
        self.siguiente = None


# Nodo de proyecto (Lista Enlazada)
class NodoProyecto:
    def __init__(self, nombre, id_proyecto):
        self.nombre = nombre
        self.id_proyecto = id_proyecto
        self.tareas = None  # Cabeza de la lista de tareas
        self.siguiente = None


# Lista de proyectos
class ListaProyectos:
    def __init__(self):
        self.primero = None

    def agregar_proyecto(self, nombre, id_proyecto):
        nuevo_proyecto = NodoProyecto(nombre, id_proyecto)
        if not self.primero:
            self.primero = nuevo_proyecto
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_proyecto
        print(f"Proyecto '{nombre}' agregado con éxito.")

    def agregar_tarea(self, id_proyecto, nombre_tarea, descripcion, estado="pendiente"):
        proyecto = self.buscar_proyecto(id_proyecto)
        if proyecto:
            nueva_tarea = NodoTarea(nombre_tarea, descripcion, estado)
            if not proyecto.tareas:
                proyecto.tareas = nueva_tarea
            else:
                actual = proyecto.tareas
                while actual.siguiente:
                    actual = actual.siguiente
                actual.siguiente = nueva_tarea
            print(f"Tarea '{nombre_tarea}' agregada al proyecto '{proyecto.nombre}'.")
        else:
            print(f"Proyecto con ID {id_proyecto} no encontrado.")

    def cambiar_estado_tarea(self, id_proyecto, nombre_tarea, nuevo_estado):
        proyecto = self.buscar_proyecto(id_proyecto)
        if proyecto:
            actual = proyecto.tareas
            while actual:
                if actual.nombre == nombre_tarea:
                    actual.estado = nuevo_estado
                    print(f"Estado de la tarea '{nombre_tarea}' actualizado a '{nuevo_estado}'.")
                    return
                actual = actual.siguiente
            print(f"Tarea '{nombre_tarea}' no encontrada en el proyecto '{proyecto.nombre}'.")
        else:
            print(f"Proyecto con ID {id_proyecto} no encontrado.")

    def listar_proyectos(self):
        if not self.primero:
            print("No hay proyectos registrados.")
            return
        actual = self.primero
        while actual:
            print(f"\nProyecto: {actual.nombre} (ID: {actual.id_proyecto})")
            print("Tareas:")
            tarea_actual = actual.tareas
            if not tarea_actual:
                print("  No hay tareas registradas.")
            while tarea_actual:
                print(f"  - {tarea_actual.nombre}: {tarea_actual.descripcion} [Estado: {tarea_actual.estado}]")
                tarea_actual = tarea_actual.siguiente
            actual = actual.siguiente

    def buscar_proyecto(self, id_proyecto):
        actual = self.primero
        while actual:
            if actual.id_proyecto == id_proyecto:
                return actual
            actual = actual.siguiente
        return None


# Menú para interactuar con el usuario
def menu():
    proyectos = ListaProyectos()

    while True:
        print("\n--- Menú de Gestión de Proyectos ---")
        print("1. Agregar un nuevo proyecto")
        print("2. Agregar una tarea a un proyecto")
        print("3. Cambiar el estado de una tarea")
        print("4. Listar todos los proyectos y tareas")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre del proyecto: ")
            id_proyecto = input("ID del proyecto: ")
            proyectos.agregar_proyecto(nombre, id_proyecto)

        elif opcion == "2":
            id_proyecto = input("ID del proyecto: ")
            nombre_tarea = input("Nombre de la tarea: ")
            descripcion = input("Descripción de la tarea: ")
            estado = input("Estado de la tarea (pendiente, en progreso, completada): ")
            proyectos.agregar_tarea(id_proyecto, nombre_tarea, descripcion, estado)

        elif opcion == "3":
            id_proyecto = input("ID del proyecto: ")
            nombre_tarea = input("Nombre de la tarea: ")
            nuevo_estado = input("Nuevo estado (pendiente, en progreso, completada): ")
            proyectos.cambiar_estado_tarea(id_proyecto, nombre_tarea, nuevo_estado)

        elif opcion == "4":
            proyectos.listar_proyectos()

        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()

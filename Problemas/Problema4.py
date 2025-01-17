class NodoTarea:
    def __init__(self, nombre, descripcion, estado="pendiente"):
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado
        self.anterior = None
        self.siguiente = None

class ListaDobleTareas:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar_tarea(self, nombre, descripcion, estado="pendiente"):
        nueva_tarea = NodoTarea(nombre, descripcion, estado)
        if not self.cabeza:
            self.cabeza = self.cola = nueva_tarea
        else:
            self.cola.siguiente = nueva_tarea
            nueva_tarea.anterior = self.cola
            self.cola = nueva_tarea

    def insertar_tarea(self, posicion, nombre, descripcion, estado="pendiente"):
        nueva_tarea = NodoTarea(nombre, descripcion, estado)
        if posicion == 0:  # Insertar al inicio
            if not self.cabeza:
                self.cabeza = self.cola = nueva_tarea
            else:
                nueva_tarea.siguiente = self.cabeza
                self.cabeza.anterior = nueva_tarea
                self.cabeza = nueva_tarea
        else:
            actual = self.cabeza
            indice = 0
            while actual and indice < posicion:
                anterior = actual
                actual = actual.siguiente
                indice += 1
            if not actual:  # Insertar al final
                self.agregar_tarea(nombre, descripcion, estado)
            else:  # Insertar en el medio
                nueva_tarea.siguiente = actual
                nueva_tarea.anterior = actual.anterior
                if actual.anterior:
                    actual.anterior.siguiente = nueva_tarea
                actual.anterior = nueva_tarea

    def eliminar_tarea(self, nombre):
        actual = self.cabeza
        while actual:
            if actual.nombre == nombre:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.cola = actual.anterior
                return True
            actual = actual.siguiente
        return False  # Tarea no encontrada

    def avanzar(self):
        actual = self.cabeza
        while actual:
            print(f"Tarea: {actual.nombre}, Descripción: {actual.descripcion}, Estado: {actual.estado}")
            actual = actual.siguiente

    def retroceder(self):
        actual = self.cola
        while actual:
            print(f"Tarea: {actual.nombre}, Descripción: {actual.descripcion}, Estado: {actual.estado}")
            actual = actual.anterior

    def generar_tareas_recursivo(self, inicio_id, fin_id, descripcion_base):
        if inicio_id > fin_id:
            return  # Caso base: cuando el ID alcanza el fin_id, terminamos la recursión

        # Crear una tarea con el ID correspondiente
        nombre_tarea = f"Tarea {inicio_id}"
        descripcion_tarea = f"{descripcion_base} {inicio_id}"
        self.agregar_tarea(nombre_tarea, descripcion_tarea)

        # Llamada recursiva para crear la siguiente tarea
        self.generar_tareas_recursivo(inicio_id + 1, fin_id, descripcion_base)

def menu():
    lista_tareas = ListaDobleTareas()

    # Cargar tareas pre-cargadas
    lista_tareas.agregar_tarea("Tarea 1", "Descripción de la tarea 1", "pendiente")
    lista_tareas.agregar_tarea("Tarea 2", "Descripción de la tarea 2", "en progreso")
    lista_tareas.agregar_tarea("Tarea 3", "Descripción de la tarea 3", "completada")
    lista_tareas.agregar_tarea("Tarea 4", "Descripción de la tarea 4", "pendiente")

    while True:
        print("\n--- Menú de Gestión de Tareas ---")
        print("1. Ver tareas hacia adelante")
        print("2. Ver tareas hacia atrás")
        print("3. Generar tareas automáticamente (Recursividad)")
        print("4. Insertar tarea en posición")
        print("5. Eliminar tarea")
        print("6. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print("\nAvanzando por las tareas:")
            lista_tareas.avanzar()
        elif opcion == "2":
            print("\nRetrocediendo por las tareas:")
            lista_tareas.retroceder()
        elif opcion == "3":
            inicio_id = int(input("Ingresa el ID inicial: "))
            fin_id = int(input("Ingresa el ID final: "))
            descripcion_base = input("Ingresa una descripción base para las tareas: ")
            lista_tareas.generar_tareas_recursivo(inicio_id, fin_id, descripcion_base)
            print(f"Tareas generadas desde ID {inicio_id} hasta {fin_id}.")
        elif opcion == "4":
            posicion = int(input("Posición donde insertar la tarea: "))
            nombre = input("Nombre de la tarea: ")
            descripcion = input("Descripción de la tarea: ")
            estado = input("Estado de la tarea (pendiente, en progreso, completada): ")
            lista_tareas.insertar_tarea(posicion, nombre, descripcion, estado)
            print("Tarea insertada con éxito.")
        elif opcion == "5":
            nombre = input("Nombre de la tarea a eliminar: ")
            if lista_tareas.eliminar_tarea(nombre):
                print("Tarea eliminada con éxito.")
            else:
                print("No se encontró la tarea especificada.")
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

# Iniciar el menú interactivo
menu()

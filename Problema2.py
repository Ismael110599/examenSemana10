class Tarea:
    def __init__(self, nombre, descripcion, estado="pendiente"):
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado
        self.siguiente = None

class ListaCircularTareas:
    def __init__(self):
        self.cabeza = None

    def agregar_tarea(self, nombre, descripcion):
        nueva_tarea = Tarea(nombre, descripcion)
        if not self.cabeza:
            self.cabeza = nueva_tarea
            nueva_tarea.siguiente = self.cabeza
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = nueva_tarea
            nueva_tarea.siguiente = self.cabeza

    def eliminar_tarea(self, nombre_tarea):
        if not self.cabeza:
            return False  # Lista vacía

        actual = self.cabeza
        anterior = None

        while True:
            if actual.nombre == nombre_tarea:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    # Caso especial: eliminar la cabeza
                    if actual.siguiente == self.cabeza:
                        # Solo hay un elemento en la lista
                        self.cabeza = None
                    else:
                        # Encontrar el último nodo
                        ultimo = self.cabeza
                        while ultimo.siguiente != self.cabeza:
                            ultimo = ultimo.siguiente
                        self.cabeza = actual.siguiente
                        ultimo.siguiente = self.cabeza
                return True

            anterior = actual
            actual = actual.siguiente

            if actual == self.cabeza:
                break  # Hemos recorrido toda la lista

        return False  # Tarea no encontrada

    def recorrer_tareas(self, ciclos=1):
        if not self.cabeza:
            print("No hay tareas en la lista.")
            return

        actual = self.cabeza
        contador = 0

        while contador < ciclos:
            print(f"Tarea: {actual.nombre}, Descripción: {actual.descripcion}, Estado: {actual.estado}")
            actual = actual.siguiente
            if actual == self.cabeza:
                contador += 1

def menu():
    lista_tareas = ListaCircularTareas()

    while True:
        print("\n--- Menú de Tareas ---")
        print("1. Agregar tarea")
        print("2. Recorrer tareas cíclicamente")
        print("3. Eliminar tarea")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre de la tarea: ")
            descripcion = input("Descripción de la tarea: ")
            lista_tareas.agregar_tarea(nombre, descripcion)
            print("Tarea agregada con éxito.")
        elif opcion == "2":
            ciclos = int(input("Número de ciclos para recorrer las tareas: "))
            print("\nRecorriendo tareas:")
            lista_tareas.recorrer_tareas(ciclos)
        elif opcion == "3":
            nombre = input("Nombre de la tarea a eliminar: ")
            if lista_tareas.eliminar_tarea(nombre):
                print("Tarea eliminada con éxito.")
            else:
                print("No se encontró la tarea especificada.")
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

# Iniciar el menú interactivo
menu()

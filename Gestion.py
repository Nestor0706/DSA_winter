"""
Problema: Gestión básica de una lista de reproducción
Contexto
Una aplicación de música necesita representar listas de reproducción sencillas. Cada lista debe almacenar información básica y permitir realizar acciones elementales sobre ella.
Instrucciones
1. Crea una clase llamada ListaReproduccion.
2. La clase debe tener:
Un constructor que reciba el nombre de la lista.
Un atributo que almacene las canciones (puede ser una lista).
Un método llamado agregar_cancion que reciba el nombre de una canción y la agregue a la lista.
Un método llamado mostrar_canciones que imprima todas las canciones de la lista.
3. En el programa principal:
Crea al menos dos objetos de la clase ListaReproduccion.
Agrega canciones a cada lista.
Muestra las canciones de cada lista usando mostrar_canciones
"""
class ListaReproduccion:
        def __init__(self, nombre):
            self.nombre = nombre
            self.canciones = []
        
        def agregar_cancion(self, nombre_cancion):
            self.canciones.append(nombre_cancion)
        
        def mostrar_canciones(self):
            print(f"Lista de reproducción: {self.nombre}")
            if self.canciones:
                for i, cancion in enumerate(self.canciones, 1):
                    print(f"  {i}. {cancion}")
            else:
                print("  (vacía)")
            print()

     
lista1 = ListaReproduccion("Favoritos")
lista2 = ListaReproduccion("Estudiar")
            
lista1.agregar_cancion("Bohemian Rhapsody - Queen")
lista1.agregar_cancion("Stairway to Heaven - Led Zeppelin")
lista1.agregar_cancion("Hotel California - Eagles")
        
        
lista2.agregar_cancion("Blinding Lights - The Weeknd")
lista2.agregar_cancion("Anti-Hero - Taylor Swift")
lista2.agregar_cancion("As It Was - Harry Styles")
        
      
lista1.mostrar_canciones()
lista2.mostrar_canciones()
    

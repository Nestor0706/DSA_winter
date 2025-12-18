"""""
Problema: Gestión básica de calificaciones de un grupo
Contexto
Un docente necesita un programa sencillo para registrar y consultar las calificaciones de un grupo de estudiantes. Cada grupo tendrá una lista de calificaciones y se deberán realizar operaciones básicas sobre dicha lista.
Instrucciones
1. Crea una clase llamada Grupo.
2. La clase debe tener:
Un constructor que reciba el nombre del grupo.
Un atributo que almacene las calificaciones en una lista.
Un método llamado agregar_calificacion que reciba una calificación y la agregue a la lista.
Un método llamado mostrar_calificaciones que imprima todas las calificaciones junto con su posición (índice) en la lista.
Un método llamado obtener_calificacion que reciba un índice y muestre la calificación correspondiente a esa posición.
3. En el programa principal:
Crea al menos un objeto de la clase Grupo.
Agrega varias calificaciones.
Consulta calificaciones usando distintos índices.
"""
class Grupo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.calificaciones = []
    
    def agregar_calificacion(self, calificacion):
        self.calificaciones.append(calificacion)
    
    def mostrar_calificaciones(self):        
        no_elementos=len(self.calificaciones)

        for elemento in range(no_elementos):
            print(f"{elemento+1}: {self.calificaciones[elemento]}")
    
    def obtener_calificacion(self, indice):
       print(f"indice: {indice} calificacion: {self.calificaciones[indice -1]}")


grupo1 = Grupo("TICs 3A")

grupo1.agregar_calificacion(90)
grupo1.agregar_calificacion(100)
grupo1.agregar_calificacion(50)
grupo1.agregar_calificacion(70)


grupo1.mostrar_calificaciones()

indice = int(input("dame el valor del indice: "))
grupo1.obtener_calificacion(indice)
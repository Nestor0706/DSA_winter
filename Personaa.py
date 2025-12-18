"""
Una institución desea representar personas dentro de un sistema sencillo. De cada persona se necesita almacenar su nombre y su edad, así como realizar algunas acciones básicas relacionadas con esta información.
Instrucciones
Crea una clase llamada Persona.
La clase debe contar con:
Un constructor que reciba el nombre y la edad de la persona.
Un método llamado saludar que muestre en pantalla un mensaje con el nombre y la edad de la persona.
Un método llamado es_mayor_de_edad que regrese True si la persona tiene 18 años o más, y False en caso contrario.
En el programa principal:
Crea al menos dos objetos de la clase Persona con diferentes valores.
Llama al método saludar para cada objeto.
Muestra en pantalla el resultado del método es_mayor_de_edad para cada persona.
"""
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        print(f"Hola,mi nombre es {self.nombre} y tengo {self.edad} años.")
    def es_mayor_de_edad(self):
        return self.edad >= 18  
p1 = Persona("Anel", 25)
p2 = Persona("Luis", 16)
p1.saludar()
print(p1.es_mayor_de_edad())
p2.saludar()      
print(p2.es_mayor_de_edad())


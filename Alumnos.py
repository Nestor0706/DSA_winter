"""
Problema: Registro básico de alumnos y sus calificaciones
Contexto
Un docente necesita un sistema sencillo para registrar alumnos y almacenar varias calificaciones por alumno. Cada alumno se identifica por su nombre y tiene asociada una lista de calificaciones.
Instrucciones
1. Crea una clase llamada RegistroAlumnos.
2. La clase debe tener:
Un constructor que inicialice un diccionario vacío.
El diccionario debe usar:
Clave: nombre del alumno (string).
Valor: lista de calificaciones (lista de números).
Un método agregar_alumno que reciba el nombre del alumno y lo agregue al diccionario con una lista vacía de calificaciones.
Un método agregar_calificacion que reciba el nombre del alumno y una calificación, y la agregue a su lista correspondiente.
Un método mostrar_registro que muestre cada alumno con todas sus calificaciones.
Un método promedio_alumno que reciba el nombre de un alumno y muestre su promedio de calificaciones (calculado manualmente).
3. En el programa principal:
Agrega varios alumnos.
Registra varias calificaciones para cada alumno.
Muestra el registro completo.
Consulta el promedio de al menos un alumno.
"""
class RegistroAlumnos:              
    def __init__(self):
        self.alumnos = {}
    
    def agregar_alumno(self, nombre):
        self.alumnos[nombre] = []
    
    def agregar_calificacion(self, nombre, calificacion):
        # si el alumno existe agrego la calificacion    
        if nombre in self.alumnos:
            self.alumnos[nombre].append(calificacion)
        else:
            print(f"{nombre} no encontrado !!.")
    
    def mostrar_registro(self):
        for alumno in self.alumnos:
            print(f"{alumno}: {self.alumnos[alumno]}")  
    
    def promedio_alumno(self, nombre):
        if nombre in self.alumnos:
           calificaciones = self.alumnos[nombre]
           promedio = sum(calificaciones) / (len(calificaciones)) 
           print(f"{nombre} promedio: {promedio} - {calificaciones}")
        else:
            print(f"{nombre} no encontrado !!.")
            

registro = RegistroAlumnos()

registro.agregar_alumno("Ana")
registro.agregar_alumno("Luis")

registro.agregar_calificacion("Ana", 8)
registro.agregar_calificacion("Ana", 9)  
registro.agregar_calificacion("Ana", 10)
     
registro.agregar_calificacion("Luis", 5)
registro.agregar_calificacion("Luis", 10)
registro.agregar_calificacion("Luis", 8)
registro.agregar_calificacion("Luis", 7)

registro.mostrar_registro()     

registro.promedio_alumno("Ana")  
registro.promedio_alumno("Luis")

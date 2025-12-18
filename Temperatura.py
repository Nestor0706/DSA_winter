"""
DocsProblema: Análisis básico de temperaturas registradas
Contexto
Una estación meteorológica registra temperaturas a lo largo del día. El sistema debe almacenar dichas temperaturas y permitir obtener información básica a partir de la lista de valores registrados.
Instrucciones
1. Crea una clase llamada RegistroTemperaturas.
2. La clase debe tener:
Un constructor que inicialice una lista vacía de temperaturas.
Un método agregar_temperatura que reciba una temperatura (número) y la agregue a la lista.
Un método mostrar_temperaturas que muestre todas las temperaturas registradas.
Un método contar_mayores_a que reciba un valor y regrese cuántas temperaturas son mayores a ese valor.
3. En el programa principal:
Agrega varias temperaturas.
Muestra la lista completa.
Muestra cuántas temperaturas son mayores a un valor dado.
Restricciones
Usa únicamente Python básico.
No utilices librerías externas.
No está permitido usar funciones como max(), min() o sum() (deben recorrer la lista manualmente).tring for Temperatura
"""
class RegistroTemperaturas:
    def __init__(self):
        self.temperaturas = []
    
    def agregar_temperatura(self, temperatura):
        self.temperaturas.append(temperatura)
    
    def mostrar_temperaturas(self):
        no_elementos=len(self.temperaturas)

        for elemento in range(no_elementos):
            print(f"{elemento+1}: {self.temperaturas[elemento]}")

    def contar_mayores_a(self, valor):
        temporaturas_mayores = 0
        for temperatura in self.temperaturas:
            if temperatura > valor:
                temporaturas_mayores += 1  
        return temporaturas_mayores 

registro = RegistroTemperaturas()  

registro.agregar_temperatura(5)      
registro.agregar_temperatura(7)
registro.agregar_temperatura(12)
registro.agregar_temperatura(14)

registro.mostrar_temperaturas()

print(registro.contar_mayores_a(1))

                          
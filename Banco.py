"""
Problema: Control básico de una cuenta bancaria
Contexto
Un banco necesita un programa sencillo para representar cuentas bancarias de sus clientes. Cada cuenta debe almacenar información básica y permitir realizar operaciones simples.
Instrucciones
1. Crea una clase llamada CuentaBancaria.
2. La clase debe tener:
Un constructor que reciba el nombre del titular y el saldo inicial.
Un método llamado mostrar_info que imprima el nombre del titular y el saldo actual.
Un método llamado depositar que reciba una cantidad y la sume al saldo.
Un método llamado retirar que reciba una cantidad y reste el monto del saldo solo si hay saldo suficiente.
3. En el programa principal:
Crea al menos dos objetos de la clase CuentaBancaria.
Realiza depósitos y retiros en cada cuenta.
Muestra la información final de cada cuenta usando mostrar_info.
"""
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial

    def mostrar_info(self):
        print(f"Titular: {self.titular}, Saldo actual: ${self.saldo}")

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad  
        else:
            print("Saldo insuficiente.")


c1 = CuentaBancaria("Carlos", 1000)        
c2 = CuentaBancaria("María", 500)

c1.depositar(1000)
c2.depositar(500) 

c1.retirar(500)     
c2.retirar(500)  

c1.mostrar_info()      
c2.mostrar_info()  
"""
    ADMINISTRAR UNA CUENTA DE AHORROS

    INTEGRANTES:
        RUBÉN JIMÉNEZ
        JUAN JOSÉ FLÓREZ
"""

import os


class Usuario:
    def __init__(self, nombre, apellido, cedula, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.edad = edad


class Cuenta(Usuario):
    def __init__(self, nombre, apellido, cedula, edad, din_ahorrado):
        super().__init__(nombre, apellido, cedula, edad)
        self.din_ahorrado = din_ahorrado   

    def mostrarben(self):
        beneficio = self.din_ahorrado * 0.05
        cantidad_cuenta = self.din_ahorrado + beneficio
        print("INFORMACIÓN CUENTA DE AHORROS USUARIO JÓVEN")
        print("Titular: ", self.nombre, " ", self.apellido)
        print("Edad: ", self.edad, " Cédula: ", self.cedula)
        print("Saldo: ", self.din_ahorrado)
        print("Beneficio: ", beneficio)
        print("Saldo total: ", cantidad_cuenta)

        os.system("pause")

    def mostrar(self):
        print("INFORMACIÓN CUENTA DE AHORROS")
        print("Titular: ", self.nombre, " ", self.apellido)
        print("Edad: ", self.edad, " Cédula: ", self.cedula)
        print("Saldo: ", self.din_ahorrado)

        os.system("pause")

    def ingresar(self, cantidad):
        if cantidad < 0:
            print("El valor de la consignación debe ser mayor a cero")
        else:
            self.din_ahorrado += cantidad
            print("¡¡¡CONSIGNACIÓN REALIZADA CON ÉXITO!!!")
        
        os.system("pause")

    def retirar(self, cantidad):
        if cantidad < 0:
            print("El valor del retiro debe ser mayor a cero")
        elif cantidad > self.din_ahorrado:
            print("No tiene dinero suficiente en su cuenta para realizar el retiro")
        else:
            self.din_ahorrado -= cantidad
            print("¡¡¡RETIRO REALIZADO CON ÉXITO!!!")

        os.system("pause")


class Beneficio(Cuenta):
    def __init__(self, nombre, apellido, cedula, edad, din_ahorrado):
        super().__init__(nombre, apellido, cedula, edad, din_ahorrado)

    def es_joven(self):
        if self.edad >= 18 and self.edad < 28:
            return True

        return False

    def mostrar(self):
        if self.es_joven():
            return super().mostrarben()

        return super().mostrar()


if __name__ == '__main__':
    os.system("cls")

    print("¡¡¡BIENVENIDO!!!")
    print("Ingrese los siguientes datos:")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    cedula = input("Cédula: ")
    edad = int(input("Edad: "))
    din_ahorrado = 0

    cliente1 = Beneficio(nombre, apellido, cedula, edad, din_ahorrado)
    cliente1.es_joven()

    print("¡¡¡CUENTA DE AHORROS CREADA EXITOSAMENTE!!!")
    os.system("pause")

    while True:
        os.system("cls")
        print("Eliga una opción:")
        print("1. Consignar dinero")
        print("2. Retirar dinero")
        print("3. Mostrar detalles de la cuenta")
        print("0. Salir")

        opcion = int(input())

        if opcion == 1:
            cantidad = input("Digite el valor de la consignación: ")
            cliente1.ingresar(int(cantidad))
        
        elif opcion == 2:
            cantidad = input("Digite el valor del retiro: ")
            cliente1.retirar(int(cantidad))

        elif opcion == 3:
            cliente1.mostrar()

        elif opcion == 0:
            quit()

        else:
            print("Error, opción no disponible, digite una opción válida.")
            os.system("pause")
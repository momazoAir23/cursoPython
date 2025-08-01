class Numero:
    def __init__(self, valor):
        self.valor = valor
    def evaluarNumero(self):
        if self.valor & 1:  
            print("El número ingresado es impar")
            if self.valor == 7:
                print("\n Y es un comodín")
        else:
            print("El número ingresado es par")
            if self.valor == 10:
                print("\n Y es el número 10")
    def sumar(self, otro):
        return self.valor + otro
if __name__ == "__main__":
    print("=== CLASE que Evalua PAR o IMPAR y Suma ===")
    entrada = int(input("Ingrese el número a evaluar: "))
    numero = Numero(entrada)
    numero.evaluarNumero()
    numero.sumar(5)
    print(f"La suma de {numero.valor} y 5 es: {numero.sumar(5)}")
    print("=== Linea agregada para modificar el GIT ===")
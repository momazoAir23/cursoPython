def evaluarNumero(numero):
    if (numero % 2)== 0:
        print("El numero ingresado es par")
        if numero == 10:
            print("Y es el número 10")
    else:
        print("El numero ingresado es impar")
        if numero == 7:
            print("Y es un comodín")
def main():
    print("=== Evaluando número PAR o IMPAR ===")
    entrada = int(input("Ingrese el número a evaluar: "))
    evaluarNumero(entrada)
if __name__ == "__main__":
    main()
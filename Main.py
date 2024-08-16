import Binario
import puntoBinario
import Hexadecimal
import puntoHexadecimal
import puntoOctal
import Octal
import Decimal
import puntoDecimal
import re

print("Este programa sirve para realizar")
print("conversiones entre sistemas numéricos")
print("como el hexadecimal, binario, octal y decimal")
print("tanto enteros como con punto flotante")

print("\nElige la opción que necesitas. Si eliges")
print("binario, hexadecimal, octal o decimal, "
      "\nvas a escribir un número de ese sistema")
print("y se va a convertir a los demás sistemas.")

opcion = True

while opcion == True:
    print("Escribe el numero de lo que quieres hacer: ")
    numeroOpcion = int(input("1. Binario"
          "\n2. Hexadecimal"
          "\n3. Octal"
          "\n4. Decimal"
          "\n5. Salir\n"))
    print("______________________________________________________________")
    if numeroOpcion == 5:
        opcion = False
    elif numeroOpcion == 1:
        correcto = False
        while not correcto:
            try:
                numero = input("Escribe el número en binario: ")

                if numero.__contains__("."):
                    if not re.match(r'^[01]+\.[01]+$', numero):
                        raise ValueError("Ingresaste un número binario con punto flotante no válido")

                    correcto = True
                else:
                    digitos = [int(dig) for dig in numero]

                    for digito in digitos:
                        if digito != 0 and digito != 1:
                            raise ValueError("Ingresaste un dígito no válido")

                    correcto = True
            except ValueError:
                print("Los dígitos deben ser únicamente 0 o 1")

        if numero.__contains__("."):
            print("")
            print("Resultados de hexadecimal, decimal y octal: ")
            puntoBinario.binarioHexadecimalPunto(numero)
            print("")
            print("Decimal: ", end="")
            puntoBinario.binarioDecimalPunto(numero)
            puntoBinario.binarioOctalPunto(numero)
        else:
            print("")
            print("Conversiones a decimal, hexadecimal y octal: ")
            print("Decimal: ", end="")
            Binario.binADecimal(digitos)
            Binario.binAHex(digitos)
            print("")
            Binario.binAOctal(digitos)
        print("\n______________________________________________________________")
    elif numeroOpcion == 2:
        correcto = False
        while not correcto:
            try:
                digitos = []
                numero = input("Escribe el número en hexadecimal: ")
                if numero.__contains__("."):
                    if not re.match(r'^[0123456789ABCDEF]+\.[0123456789ABCDEF]+$', numero):
                        raise ValueError("Ingresaste un número hexadecimal con punto flotante no válido")
                    correcto = True
                else:
                    for i in numero:
                        digitos.append(i)

                    for digito in digitos:
                        if digito not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E',
                                          'F']:
                            raise ValueError("Ingresaste un dígito no válido")

                    correcto = True
            except ValueError:
                print("Los dígitos deben ser, numéricos entre 0 y 9,")
                print("y las letras A, B, C, D, E y F")
        if numero.__contains__("."):
            puntoHexadecimal.hexAOctal(numero)
            print("")
            puntoHexadecimal.hexBinario(numero)
            print("")
            print("Decimal: ", end="")
            puntoHexadecimal.hexDecimal(numero)
        else:
            print("")
            print("Conversiones a binario, decimal y octal: ")
            print("Binario: ", end="")
            Hexadecimal.hexABin(digitos)
            print("")
            print("Decimal: ", end="")
            Hexadecimal.hexADecimal(digitos)
            print("")
            print("Octal: ", end="")
            Hexadecimal.hexAOctal(digitos)
        print("\n______________________________________________________________")
    elif numeroOpcion == 3:
        correcto = False
        while not correcto:
            try:
                numero = input("Escribe el número en octal: ")
                if numero.__contains__("."):
                    if not re.match(r'^[01234567]+\.[01234567]+$', numero):
                        raise ValueError("Ingresaste un número octal con punto flotante no válido")
                    correcto = True
                else:
                    digitos = [int(dig) for dig in numero]

                    for digito in digitos:
                        if digito not in [0, 1, 2, 3, 4, 5, 6, 7]:
                            raise ValueError("Ingresaste un dígito no válido")

                    correcto = True
            except ValueError:
                print("Los dígitos deben ser únicamente 0 o 7")
        if numero.__contains__("."):
            print()
            print("Resultados de decimal, octal y binario: ")
            print("Decimal: ", end="")
            puntoOctal.puntoOctalADecimal(numero)
            puntoOctal.puntoOctalHex(numero)
            print("")
            puntoOctal.puntoOctalBinario(numero)
        else:
            print("")
            print("Resultados de binario, decimal y hexadecimal: ")
            print("Binario: ", end="")
            Octal.octalABinario(digitos)
            print("")
            print("Decimal: ", end="")
            Octal.octalADecimal(digitos)
            print("Hexadecimal: ", end="")
            Octal.octalAHexadecimal(digitos)
        print("\n______________________________________________________________")
    elif numeroOpcion == 4:
        correcto = False
        while not correcto:
            try:
                numero = input("Escribe el número entero en base 10: ")

                if numero.__contains__("."):
                    if not re.match(r'^[0123456789]+\.[0123456789]+$', numero):
                        raise ValueError("Ingresaste un número decimal con punto flotante no válido")
                    correcto = True
                else:
                    numero = int(numero)
                    if numero < 0:
                        print("El número debe ser entero positivo")
                    else:
                        correcto = True
            except ValueError:
                print("Los dígitos ingresados tienen que ser numéricos entre 0 y 9")
        numero = str(numero)
        if numero.__contains__("."):
            print("Resultados a binario, octal y hexadecimal: ")
            print("Binario: ", end="")
            numero = float(numero)
            puntoDecimal.decimalBinarioPunto(numero)
            print("")
            print("Octal: ", end="")
            puntoDecimal.decimalOctalPunto(numero)
            print("")
            print("Hexadecimal: ", end="")
            puntoDecimal.decimalHexPunto(numero)
        else:
            numero = int(numero)
            print("")
            print("Conversiones a binario, hexadecimal y octal: ")
            Decimal.decimalABinario(numero)
            print("")
            Decimal.decimalAHexadecimal(numero)
            print("")
            Decimal.decimalAOctal(numero)
        print("\n______________________________________________________________")

    elif numeroOpcion > 5 or numeroOpcion < 1:
        print("No hay opción con el número ingresado")
        print("\n______________________________________________________________")
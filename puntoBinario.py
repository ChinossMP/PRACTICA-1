def binarioDecimalPunto(numero):
    izquierda = numero[:numero.find(".")]
    derecha = numero[numero.find(".") + 1:]

    digitosIzquierda = [int(digito) for digito in izquierda]

    # de binario a decimal
    bases = []
    for i in range(len(digitosIzquierda)):
        bases.append(2 ** i)

    suma = 0
    digitosIzquierda.reverse()
    for i in range(len(bases)):
        suma += digitosIzquierda[i] * bases[i]

    # parte derecha
    digitosDerecha = [int(digito) for digito in derecha]

    sumaDerecha = 0

    for i in range(1, len(digitosDerecha) + 1, 1):
        sumaDerecha += digitosDerecha[i - 1] * (2 ** -i)

    print(suma + sumaDerecha)

def binarioOctalPunto(numero):
    #separar las dos partes
    izquierda = numero[:numero.find(".")]
    derecha = numero[numero.find(".") + 1:]

    izquierda = [int(digito) for digito in izquierda]

    #Calcular el octal de la parte izquierda

    equivalenciasOctal = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]

    # dividir para encontrar el múltiplo
    multiplo = [izquierda[i:i + 3] for i in range(0, len(izquierda), 3)]

    llenarConCeros = [0] * (len(multiplo) * 3)

    # voltear los digitos
    izquierda.reverse()
    for i in range(len(izquierda)):
        llenarConCeros[i] = izquierda[i]

    llenarConCeros.reverse()
    # dividir en grupos de tres

    subListas = [llenarConCeros[i:i + 3] for i in range(0, len(llenarConCeros), 3)]

    octal = []
    # comparar con la equivalencia
    for i in range(len(subListas)):
        for j in range(len(equivalenciasOctal)):
            if subListas[i] == equivalenciasOctal[j]:
                octal.append(j)



    #Convertir la parte derecha en octal

    derecha = [int(digito) for digito in derecha]
    multiplo = [derecha[i:i+3] for i in range(0,len(derecha), 3)]

    llenarCerosDerecha = [0] * (len(multiplo) * 3)

    for i in range(len(derecha)):
        llenarCerosDerecha[i] = derecha[i]

    subListasDerecha = [llenarCerosDerecha[i : i + 3] for i in range(0, len(llenarCerosDerecha), + 3)]

    octalDerecha = []
    for i in range(len(subListasDerecha)):
        for j in range(8):
            if subListasDerecha[i] == equivalenciasOctal[j]:
                octalDerecha.append(j)

    print("Octal: ", end = "")
    ##Juntar las dos partes
    for i in range(len(octal)):
        print(octal[i], end = "")
    print(".", end = "")
    for j in range(len(octalDerecha)):
        print(octalDerecha[j], end = "")

def binarioHexadecimalPunto(numero):

    izquierda = numero[:numero.find(".")]
    derecha = numero[numero.find(".") + 1:]

    #parte izquierda
    izquierda = [int(digito) for digito in izquierda]

    equivalenciasHex = [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 1],
                        [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1],
                        [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 1]]
    # dividir para encontrar multiplo
    digitosBin = [izquierda[i: i + 4] for i in range(0, len(izquierda), 4)]

    llenarCeros = [0] * (len(digitosBin) * 4)

    # llenar con los dígitos al reves
    izquierda.reverse()

    for i in range(len(izquierda)):
        llenarCeros[i] = izquierda[i]

    llenarCeros.reverse()

    subListas = [llenarCeros[i:i + 4] for i in range(0, len(llenarCeros), 4)]

    hex = []

    for i in range(len(subListas)):
        for j in range(len(equivalenciasHex)):
            if subListas[i] == equivalenciasHex[j]:
                if j == 10:
                    hex.append("A")
                elif j == 11:
                    hex.append("B")
                elif j == 12:
                    hex.append("C")
                elif j == 13:
                    hex.append("D")
                elif j == 14:
                    hex.append("E")
                elif j == 15:
                    hex.append("F")
                else:
                    hex.append(j)

    #la parte derecha
    derecha = [int(digito) for digito in derecha]

    multiplo = [derecha[i: i + 4] for i in range(0, len(derecha), 4)]

    llenarCerosDerecha = [0] * (len(multiplo) * 4)

    #llenar el arreglo
    for i in range(len(derecha)):
        llenarCerosDerecha[i] = derecha[i]

    #dividir en sublistas de 4
    subListasHex = [llenarCerosDerecha[i:i+4] for i in range(0, len(llenarCerosDerecha), 4)]

    hexDerecha = []
    #comparar con el equivalente
    for i in range(len(subListasHex)):
        for j in range(len(equivalenciasHex)):
            if subListasHex[i] == equivalenciasHex[j]:
                if j == 10:
                    hexDerecha.append("A")
                elif j == 11:
                    hexDerecha.append("B")
                elif j == 12:
                    hexDerecha.append("C")
                elif j == 13:
                    hexDerecha.append("D")
                elif j == 14:
                    hexDerecha.append("E")
                elif j == 15:
                    hexDerecha.append("F")
                else:
                    hexDerecha.append(j)

    #mostrar resultado
    print("Hexadecimal: ", end = "")
    for i in range(len(hex)):
        print(hex[i], end = "")
    print(".", end = "")
    for j in range(len(hexDerecha)):
        print(hexDerecha[j], end = "")

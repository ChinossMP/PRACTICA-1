def hexAOctal(digitos):
    # Hexadecimal a octal
    equivalenciasHex = [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 1],
                        [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1],
                        [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 1]]
    equivalenciasOctal = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
    
    for i in range(len(digitos)):
        if digitos[i] == 'A':
            digitos[i] = 10
        elif digitos[i] == 'B':
            digitos[i] = 11
        elif digitos[i] == 'C':
            digitos[i] = 12
        elif digitos[i] == 'D':
            digitos[i] = 13
        elif digitos[i] == 'E':
            digitos[i] = 14
        elif digitos[i] == 'F':
            digitos[i] = 15

    hexABin = []
    digitos = [int(dig) for dig in digitos]
    digitos.reverse()

    for i in range(len(digitos)):
        hexABin.append(equivalenciasHex[digitos[i]])

    vectorBinario = []
    for i in range(len(hexABin)):
        for j in range(4):
            vectorBinario.append(hexABin[i][j])

    vectorBinario.reverse()
    vecAux = vectorBinario

    # Agregar los ceros faltantes
    sublistas = [vectorBinario[i:i + 3] for i in range(0, len(vectorBinario), 3)]
    binarioOctal = [0] * (len(sublistas) * 3)

    for i in range(len(vecAux)):
        binarioOctal[i] = vecAux[i]

    binarioOctal.reverse()

    digitosBin = [binarioOctal[i: i + 3] for i in range(0, len(binarioOctal), 3)]

    numOctal = []

    for i in range(len(digitosBin)):
        for j in range(len(equivalenciasOctal)):
            if digitosBin[i] == equivalenciasOctal[j]:
                numOctal.append(j)

    for i in range(len(numOctal)):
        print(numOctal[i], end = "")

def hexABin(digitos):
    equivalenciasHex = [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 1],
                        [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1],
                        [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 1]]
    for i in range(len(digitos)):
        if digitos[i] == 'A':
            digitos[i] = 10
        elif digitos[i] == 'B':
            digitos[i] = 11
        elif digitos[i] == 'C':
            digitos[i] = 12
        elif digitos[i] == 'D':
            digitos[i] = 13
        elif digitos[i] == 'E':
            digitos[i] = 14
        elif digitos[i] == 'F':
            digitos[i] = 15

    hexABin = []
    digitos = [int(dig) for dig in digitos]

    for i in range(len(digitos)):
        hexABin.append(equivalenciasHex[digitos[i]])

    for i in range(len(hexABin)):
        for j in range(4):
            print(hexABin[i][j], end = "")

def hexADecimal(digitos):
    for i in range(len(digitos)):
        if digitos[i] == 'A':
            digitos[i] = 10
        elif digitos[i] == 'B':
            digitos[i] = 11
        elif digitos[i] == 'C':
            digitos[i] = 12
        elif digitos[i] == 'D':
            digitos[i] = 13
        elif digitos[i] == 'E':
            digitos[i] = 14
        elif digitos[i] == 'F':
            digitos[i] = 15

    digitos.reverse()
    digitos = [int(digito) for digito in digitos]

    numeroDecimal = 0
    for i in range(len(digitos)):
        numeroDecimal += (16 ** i) * digitos[i]

    print(int(numeroDecimal), end = "")
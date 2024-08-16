def octalAHexadecimal(digitos):
    equivalenciasOctal = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]

    equivalenciasHex = [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 1],
                        [0, 1, 1, 0],[0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1],
                        [1, 1, 0, 0], [1, 1, 0, 1],[1, 1, 1, 0], [1, 1, 1, 1]]

    resultadoBinario = []

    digitos.reverse()

    for i in range(len(digitos)):
        resultadoBinario.append(equivalenciasOctal[digitos[i]])

    binario = []
    for i in range(len(resultadoBinario)):
        for j in range(3):
            binario.append(resultadoBinario[i][j])

    sublistas = [binario[i:i + 4] for i in range(0, len(binario), 4)]

    binarioHex = [0] * (len(sublistas) * 4)

    binario.reverse()

    for i in range(len(binario)):
        binarioHex[i] = binario[i]

    binarioHex.reverse()
    sublistas = [binarioHex[i:i + 4] for i in range(0, len(binarioHex), 4)]

    numHexadecimal = []
    for i in range(len(sublistas)):
        for j in range(len(equivalenciasHex)):
            if sublistas[i] == equivalenciasHex[j]:
                if j == 10:
                    numHexadecimal.append("A")
                elif j == 11:
                    numHexadecimal.append("B")
                elif j == 12:
                    numHexadecimal.append("C")
                elif j == 13:
                    numHexadecimal.append("D")
                elif j == 14:
                    numHexadecimal.append("E")
                elif j == 15:
                    numHexadecimal.append("F")
                else:
                    numHexadecimal.append(str(j))

    for i in range(len(numHexadecimal)):
        print(numHexadecimal[i], end = "")

def octalABinario(digitos):
    equivalencias = [[0, 0, 0],
                     [0, 0, 1],
                     [0, 1, 0],
                     [0, 1, 1],
                     [1, 0, 0],
                     [1, 0, 1],
                     [1, 1, 0],
                     [1, 1, 1]]
    resultado = []

    for i in range(len(digitos)):
        resultado.append(equivalencias[digitos[i]])

    for i in range(len(resultado)):
        for j in range(3):
            print(resultado[i][j], end = "")

def octalADecimal(digitos):
    digitos.reverse()
    # Calcular número de octal a decimal

    numDecimal = 0
    for i in range(len(digitos)):
        numDecimal += (8 ** i) * digitos[i]

    print(numDecimal)

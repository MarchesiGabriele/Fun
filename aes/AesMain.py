# cd Google Drive/progetti_flutter/fun/aes
import numpy as np
from pandas import *
import sbox as sb

# TODO: gestire input più lunghi di 16 byte

# TODO: capire come calcolare da solo la sbox (pag 22 lecture 8)

# TODO: eseguire la rotazione dei bit usando lo shift dei bit verso sinistra


# procedura: creo key schedule da 44 word partendo dalla chiave originale, le prime 4 le uso per il primo passaggio. Il primo passaggio
# consiste nel fare una xor tra l'input e le prime 4 word del key schedule. Da questo momento iniziano i 10 round.
# Ognuno dei round esegue:
# Sostituzione byte: sostituisco byte dello state con dei byte corrispondenti presi dalla sbox in base a bit dello state
# Shift Byte: prima riga rimane uguale, secoda shifto a destra di un byte, terza riga shifto a sinistra di due byte e la terza di 3 byte
# Mix Colonne:
# Add roundKey: aggiunla roundkey all'outputstate calcolato nel round precedente
# NB: nell'ultimo round non eseguo lo step "mix colonne" !!


def main():
    # 16 byte input
    input = "colorerossosalto"
    # 32 byte key
    key = "chiavediunacapra"

    state = [[], [], [], []]
    matrixKey = [[], [], [], []]

    # state matrix creation
    for row in range(4):
        for column in range(4):
            state[column].append(input[row * 4 + column])

    print(np.matrix(state))
    print("\n \n")

    # 128 key
    for row in range(4):
        for column in range(4):
            matrixKey[column].append(key[row * 4 + column])

    print(np.matrix(matrixKey))
    print("\n \n")

    # rotazione dei 4 byte della prima colonna di byte
    hold = matrixKey[0][0]
    for row in range(4):
        if row == 3:
            matrixKey[row][0] = hold
            break
        matrixKey[row][0] = matrixKey[row + 1][0]

    print(np.matrix(matrixKey))
    print("\n \n")

    # sbox 16x16 matrix costruction
    sboxMat = []
    for row in range(16):
        sboxMat.append([])
        for column in range(16):
            sboxMat[row].append(hex(sb.sbox[row * 16 + column]))
    print(sboxMat)

    # SOSTITUZIONE BYTE
    for row in range(4):
        for column in range(4):
            # Divido byte dello stato in due metà da 4 bit
            byteBinario = bin(int.from_bytes(state[row][column].encode(), "big"))
            firstHalf = byteBinario[0:5].replace("b", "")
            lastHalf = byteBinario[5:10]

            # Passo da binario a decimale
            firstHalf = int(firstHalf, 2)
            lastHalf = int(lastHalf, 2)

            # print(firstHalf)
            # print(lastHalf)

            # Sostituzione valori nello stato
            state[row][column] = sboxMat[firstHalf][lastHalf]

    print(np.matrix(state))
    print("\n \n")

    # ROW BYTE SHIFT
    # seconda riga
    hold = state[1][0]
    hold1 = state[2][0]
    hold2 = state[2][1]
    hold3 = state[3][3]
    for i in range(4):
        # seconda riga
        if i == 3:
            state[1][i] = hold
        else:
            state[1][i] = state[1][i + 1]

        # terza riga
        if i == 2:
            state[2][i] = hold1
        elif i == 3:
            state[2][i] = hold2
        else:
            state[2][i] = state[2][i + 2]

        # quarta riga (shift a destra di 1 byte)
        if 3 - i == 0:
            state[3][3 - i] = hold3
        else:
            state[3][3 - i] = state[3][2 - i]

    print(np.matrix(state))
    print("\n \n")


if __name__ == "__main__":
    main()

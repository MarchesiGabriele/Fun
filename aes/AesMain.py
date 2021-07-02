import numpy as np

# TODO: gestire input più lunghi di 16 byte


def main():
    # 16 byte input
    input = "colorerossosalto"

    # 32 byte key
    key = "colorerossosaltocolorerossosalto"

    matrix = [[], [], [], []]
    matrixKey = [[], [], [], []]

    # input
    for row in range(4):
        for column in range(4):
            matrix[row].append(input[row * 4 + column])

    # 256 key
    for row in range(4):
        for column in range(8):
            matrixKey[row].append(key[row * 8 + column])

    print(matrix)
    print(matrixKey)


if __name__ == "__main__":
    main()

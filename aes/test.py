import numpy as np


def main():

    state = [
        [0xD4, 0xBF, 0x5D, 0x30],
        [0xE0, 0xB4, 0x52, 0xAE],
        [0xB8, 0x41, 0x11, 0xF1],
        [0x1E, 0x27, 0x98, 0xE5],
    ]
    mixMat = [[2, 3, 1, 1], [1, 2, 3, 1], [1, 1, 2, 3], [3, 1, 1, 2]]

    """ print(f"{mixMat[0][0]:08b}")
    print(f"{state[0][0]:08b}")
    print(mixMat[0][0] * state[0][0])

    print(f"{mixMat[0][1]:08b}")
    print(f"{state[1][0]:08b}")
    print(mixMat[0][1] * state[1][0])

    print(f"{mixMat[0][2]:08b}")
    print(f"{state[2][0]:08b}")
    print(mixMat[0][2] * state[2][0])

    print(f"{mixMat[0][3]:08b}")
    print(f"{state[3][0]:08b}")
    print(mixMat[0][3] * state[3][0]) """

    print(state[0][0])

    c = (
        (mixMat[0][0] * state[0][0])
        ^ (mixMat[0][1] * state[1][0])
        ^ (mixMat[0][2] * state[2][0])
        ^ (mixMat[0][3] * state[3][0])
    )

    print(hex(c))

    # matMul
    newState = state
    for row in range(4):
        for column in range(4):
            result = ""
            for index in range(4):
                if result == "":
                    result = int(mixMat[row][index]) & int(
                        str(state[index][column]), base=16
                    )
                else:
                    result = result ^ (
                        int(mixMat[row][index])
                        & int(str(state[index][column]), base=16)
                    )

            newState[row][column] = hex(result)

    # print("\n MixColumns: \n")
    # print(np.matrix(newState))


if __name__ == "__main__":
    main()

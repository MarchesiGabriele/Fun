def main():
    parola = "PAYPALISHIRING"
    righe = 20

    print(fun(parola, righe))


def fun(parola, numeroRighe):
    currentIndex = 0
    isRising = False
    result = []
    mat = [[] for y in range(numeroRighe)]

    if numeroRighe == 1:
        return parola
    else:
        for i in range(len(parola)):
            if currentIndex < numeroRighe - 1 and not isRising:
                mat[currentIndex].append(parola[i])
                currentIndex += 1
            elif currentIndex == numeroRighe - 1:
                isRising = True if numeroRighe != 2 else False
                mat[currentIndex].append(parola[i])
                currentIndex -= 1
            else:
                if currentIndex == 1 and isRising:
                    mat[currentIndex].append(parola[i])
                    isRising = False
                    currentIndex -= 1
                else:
                    mat[currentIndex].append(parola[i])
                    currentIndex -= 1
        print(mat)

        for i in range(numeroRighe):
            result.extend(mat[i])

        return "".join(result)


if __name__ == "__main__":
    main()

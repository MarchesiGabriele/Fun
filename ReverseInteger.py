def main():
    numero = 123
    print(reverse(numero))


def reverse(numero):
    newNumero = []
    c = str(numero)

    for k in range(len(c)):
        if k == "-":
            newNumero[0] = "-"
        else:
            newNumero[len(c) - k - 1] = c[k]

    return "".join(newNumero)


if __name__ == "__main__":
    main()

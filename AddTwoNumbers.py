def main():
    fun([0], [0])


def fun(l1, l2):
    res = []
    riporto = 0
    for i in range(len(l1) if len(l1) > len(l2) else len(l2)):
        c = []
        if i >= len(l1):
            c = sum(0, l2[i], riporto)
            res.append(c[0])

        elif i >= len(l2):
            c = sum(l1[i], 0, riporto)
            res.append(c[0])

        else:
            c = sum(l1[i], l2[i], riporto)
            res.append(c[0])
            print(c[0])

        riporto = c[1]

    if riporto == 1:
        res.append(1)
    print(res)


def sum(x, y, z):
    somma = x + y + z

    if somma < 10:
        return [somma, 0]
    else:
        return [somma - 10, 1]


if __name__ == "__main__":
    main()

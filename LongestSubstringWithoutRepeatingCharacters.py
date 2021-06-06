# Longest Substring Without Repeating Characters


def main():
    s = "pwwkew"
    print(fun(s))


def fun(s):
    old = []
    max = 0
    for i in range(len(s)):

        print(old)
        max = len(old) if len(old) > max else max

        if old.__contains__(s[i]):
            del old[0 : old.index(s[i]) + 1]

        old.append(s[i])

    max = len(old) if len(old) > max else max

    return max


if __name__ == "__main__":
    main()

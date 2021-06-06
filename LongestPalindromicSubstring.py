# Given a string s, return the longest palindromic substring in s.

s = "bddb"


def main():
    print(fun())


def fun():
    max = ""
    for i in range(len(s)):
        global c
        c = s[i]
        new = check(i, i - 1, i + 1)
        c = ""
        new1 = check1(i, i - 1, i + 1)
        max = new if len(new) > len(max) else max
        max = new1 if len(new1) > len(max) else max
    return max


def check(start, prima, dopo):
    global c
    if prima >= 0 and dopo < len(s):
        if s[prima] == s[dopo]:
            c = s[prima] + c + s[dopo]
            check(start, prima - 1, dopo + 1)
            return c
        else:
            return c
    else:
        return c


def check1(start, prima, dopo):
    global c
    if prima >= 0:
        if s[prima] == s[dopo]:
            c = s[prima] + c + s[dopo]
            check1(start, prima - 1, start + 1)
            return c
        else:
            return c
    elif dopo < len(s):
        if s[dopo] == s[prima]:
            c = s[prima] + c + s[dopo]
            check1(start, start - 1, dopo + 1)
            return c
        else:
            return c
    else:
        return c


if __name__ == "__main__":
    main()

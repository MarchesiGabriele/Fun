# Given a string s, return the longest palindromic substring in s.

s = "ccc"
st1 = 0
st2 = 0


def main():
    print(fun())


def fun():
    max = ""
    for i in range(len(s)):
        global c
        c = s[i]
        new = check(i, i - 1, i + 1)
        c = ""
        new1 = check1(i, i, i - 1, i + 1)
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


def check1(start1, start2, prima, dopo):
    global c
    global st1
    global st2
    if prima >= 0 and start1 < len(s) and st1 == 0:
        if s[prima] == s[start1]:
            st2 = st2 + 1
            c = s[prima] + c + s[start1]
            check1(start1 + 1, start2, prima - 1, dopo)
            return c
        else:
            return c
    elif dopo < len(s) and start2 >= 0 and st2 == 0:
        if s[dopo] == s[start2]:
            st1 = st1 + 1
            c = s[start2] + c + s[dopo]
            check1(start1, start2 - 1, prima, dopo + 1)
            return c
        else:
            return c
    else:
        return c


if __name__ == "__main__":
    main()

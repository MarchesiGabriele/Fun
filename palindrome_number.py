def isPalindrome(x):
    if len(str(x)) <= 1:
        return True
    if str(x)[0] ==  str(x)[len(str(x))-1]:
        return isPalindrome(str(x)[1:-1])
    else:
        return False

if __name__ == "__main__":
    print(isPalindrome(818))
    print(isPalindrome(1))
    print(isPalindrome(-121))
    print(isPalindrome(8998))






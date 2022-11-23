def isPalindrome(x):
    if len(str(x)) <= 1:
        return True
    if str(x)[0] ==  str(x)[len(str(x))-1]:
        return isPalindrome(str(x)[1:-1])
    else:
        return False

def isPalindrome1(x):
    if(x < 0):
        return False
    if x < 10:
        return True
    if x%10  ==  (x//10*):
        return isPalindrome(str(x)[1:-1])
    else:
        return False


if __name__ == "__main__":
    print(isPalindrome(818))
    print(isPalindrome(1))
    print(isPalindrome(-121))
    print(isPalindrome(8998))
    print("\n")
    print(isPalindrome1(818))
    print(isPalindrome1(1))
    print(isPalindrome1(-121))
    print(isPalindrome1(51))
    print(isPalindrome1(8998))







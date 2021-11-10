def main():
    n1 = 125376153716357      
    n2 = 2147483648
    print(reverse(n2))



def reverse(x):
    c = 0
    index = 0
    # flag indicates whether or not the input number is negative. This is used for syntax problem reasons with negative numbers. 
    flag = False

    if x < 0:
        flag = True
        x = 0 - x

    for k in map(int, str(x)): 
        print(k)
        c = c + k * pow(10,index) 
        print(c)
        index += 1

    if c > pow(2,31)-1 or c < -pow(2,31):
        return 0

    if not flag:
        return c
    else:
        return 0-c



if __name__ == "__main__":
    main()

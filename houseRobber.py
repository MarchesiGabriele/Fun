def main():
    houses = [2,4,8,9,9,3]
    print(rob(houses))

def rob(nums):
    res = []
    odd = 0
    even = 0

    for x in range(len(nums)):
        if x%2 == 0:
            even = even + nums[x]
        else:
            odd = odd + nums[x]

    res.append(max(odd,even))   

    for y in range(2):
        if len(nums) > 1:
            top = nums[y]
            x = y
        else:
            return nums[0]
        while(x < len(nums)):
            if x+2 < len(nums):
                if x+3 < len(nums) and nums[x+2] < nums[x+3]:
                    if nums[x+2] < nums[x+3]:
                        top = top + nums[x+3]
                        x = x+3
                        continue
                top = top + nums[x+2]
                x = x+2
                print(top)
            else:
                x = x+1
        res.append(top)

    if len(nums) <= 2:
        return max(nums)
    else:
        return max(res)




if __name__ == "__main__":
    main()












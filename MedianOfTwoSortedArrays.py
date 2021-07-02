def main():
    lista1 = []
    lista2 = [1]
    print(findMedianSortedArrays(lista1, lista2))


def findMedianSortedArrays(nums1, nums2):
    nums = []
    index1 = 0
    index2 = 0

    if len(nums1) == 0:
        nums = nums2
    elif len(nums2) == 0:
        nums = nums1
    else:
        for i in range(len(nums1) + len(nums2)):
            if (
                index1 != len(nums1)
                and index2 != len(nums2)
                and nums1[index1] < nums2[index2]
            ):
                nums.append(nums1[index1])
                index1 += 1
            elif index2 != len(nums2):
                nums.append(nums2[index2])
                index2 += 1
            else:
                nums.append(nums1[index1])
                index1 += 1

    if len(nums) % 2 == 0:
        return (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2
    else:
        return nums[len(nums) // 2]


if __name__ == "__main__":
    main()

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    [1,1,1,2,3,4,4]
    """
    replacement = "_"

    print(nums)

    k=0

    for i in range(len(nums)-1):

        for j in range(i+1, len(nums)-1):

            if nums[i] == nums[j]:
                nums[j] = replacement
                
    numbers = sorted([x for x in nums if isinstance(x, (int, float))])
    symbols = [x for x in nums if not isinstance(x, (int, float))]

    result = numbers + symbols
    k = len(numbers)
    print("After removal")
    print(result)
    print(k)
    

arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

removeDuplicates(arr)
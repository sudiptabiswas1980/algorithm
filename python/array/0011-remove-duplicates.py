def remove_duplicates(nums):
    if not nums:
        return 0

    index = 1  # position for next unique element

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[index] = nums[i]
            index += 1

    return index  # length of unique elements

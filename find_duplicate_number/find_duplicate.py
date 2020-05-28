def find_duplicate(nums):
    for i in range(len(nums) - 1):
        if sorted(nums.copy())[i] == sorted(nums.copy())[i + 1]:
            return sorted(nums.copy())[i]


print(find_duplicate([1, 2, 3, 1]))

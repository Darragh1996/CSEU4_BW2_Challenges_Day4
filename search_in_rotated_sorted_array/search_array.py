import math


def search(nums, target):
    offset = math.ceil(len(nums) / 2)
    index = (len(nums) - offset) % len(nums)
    look = True

    while look:
        if offset == 1:
            look = False

        if nums[index] == target:
            return index
        elif nums[index] > target:
            # move backwards through the arr
            # mod to keep the index within the length of the list
            index = (index - offset) % len(nums)
        elif nums[index] < target:
            index = (index + offset) % len(nums)

        offset = math.ceil(offset / 2)

    return -1

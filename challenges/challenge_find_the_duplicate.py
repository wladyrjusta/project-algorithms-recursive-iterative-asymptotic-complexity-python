def find_duplicate(nums):
    if verify_nums(nums):
        return False
    nums_count = nums_counter(nums)
    if verify_repeated_nums_length(nums_count):
        return False
    else:
        for num in nums_count:
            if nums_count[num] > 1:
                return num


def verify_repeated_nums_length(nums_count):
    repeated = 0
    for num in nums_count:
        if nums_count[num] > 1:
            repeated += 1
    if repeated == 1:
        return False
    else:
        return True


def nums_counter(nums):
    nums.sort()
    nums_counter = {}
    for num in nums:
        if num not in nums_counter:
            nums_counter[num] = 1
        elif nums_counter[num]:
            nums_counter[num] += 1
    return nums_counter


def verify_nums(nums):
    if nums is None or len(nums) == 0 or len(nums) == 1:
        return True
    for num in nums:
        if isinstance(num, str):
            return True
        if num < 0:
            return True


print(find_duplicate([1, 1, 2]))

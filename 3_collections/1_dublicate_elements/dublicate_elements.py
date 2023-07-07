def dublicate_elements(nums: list) -> list:
    my_dict = {}
    for i in set(nums):
        my_dict[i] = my_dict.setdefault(i, nums.count(i))
    return [i for i in my_dict if my_dict[i] >= 2]


nums = [4, 2, 1, 2, 2, 3, 4, 5]
print(dublicate_elements(nums))

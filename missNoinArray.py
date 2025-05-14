def find_missing_number(nums):
    num_set = set(range(min(nums), max(nums) + 1))
    return list(num_set - set(nums))[0]

nums = [1, 2, 3, 5, 6]
print(find_missing_number(nums))  



def find_missing_number(nums):
    n = len(nums) + 1
    total_sum = n * (n + 1) // 2
    return total_sum - sum(nums)

nums = [1, 2, 3, 4, 5, 6]
print(find_missing_number(nums))  
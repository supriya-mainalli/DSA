def reverse_number(nums):
    result = 0
    while nums > 0:
        digit = nums%10
        result = (result*10)+digit
        nums = nums//10
        print(result, nums)
    return result

print(reverse_number(12345))
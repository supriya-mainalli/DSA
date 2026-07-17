nums = 54312
n = abs(nums)

result = 0
while(n>0):
    digit = nums%10
    result = result*10+digit
    nums = nums//10
print(result)
    
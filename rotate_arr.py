nums = [1,2,3,4,5,6,7]

def rotate_arr(nums,k):
    temp = nums[:k]
    n = len(nums)
    k = k%n
    
    for i in range(k, n):
        nums[i-k] = nums[i]
        
    values = n-k
    j = 0
    for i in range(values,n):
        nums[i] = temp[j]
        j += 1
        
    print(nums)
    
print(rotate_arr(nums,3))
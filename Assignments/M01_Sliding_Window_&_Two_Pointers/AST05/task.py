from typing import List
def productExceptSelf(nums):
    n = len(nums)
    res = [1] * n

    p = 1
    for i in range(n):
        res[i] = p
        p *= nums[i]

    p = 1
    for i in range(n - 1, -1, -1):
        res[i] *= p
        p *= nums[i]

    return res

if __name__ == '__main__':
    arr = list(map(int,input().split()))
    print(productExceptSelf(arr))

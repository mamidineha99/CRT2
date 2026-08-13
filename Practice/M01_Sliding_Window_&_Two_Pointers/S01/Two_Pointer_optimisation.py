'''
input : [12,45,63,20,96,25,10]
output : [12,20,,96,10]
'''
#1.create an empty list(res)

'''
arr = list(map(int,input().split()))
i = 0
for j in range(len(arr)):
    if arr[j] % 2 == 0:
        arr[i] = arr[j]
        i += 1
print(arr[:i])
'''
s = input()
li = list(s)
left,right = 0,len(s)-1


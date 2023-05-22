k = int(input())
nums = list()

for i in range(k):
    summ = 0
    for j in range(1, i // 2 + 1):
        if i % j == 0:
            summ += j
    nums.append([i,summ])

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i][0]==nums[j][1] and nums[i][1]==nums[j][0] and i!=j:
            print(*nums[i])
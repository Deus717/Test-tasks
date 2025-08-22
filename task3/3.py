import sys
nums_file = sys.argv[1]

nums = list()

with open(nums_file, 'r') as file:
    for line in file:
        nums.append(int(line))

nums.sort()
median = nums[len(nums)//2]

limit = 0
for i in nums:
    limit += abs(median-i)
    if limit > 20:
        print('20 ходов недостаточно для приведения всех элементов массива к одному числу.')
        break
else:
    print(limit)
        




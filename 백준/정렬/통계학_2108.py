from collections import OrderedDict
import random
import sys

# N = random.randint(1, 500001)
# numbers = []
# for i in range(N):
#     numbers.append(random.randint(-4000, 4001))
#
# print(N)
N = int(sys.stdin.readline())
numbers = []
for i in range(N):
    numbers.append(int(sys.stdin.readline()))

numbers.sort()

_sum = 0
count_dict = OrderedDict()

for i in range(N):
    _sum += numbers[i]

    if i == len(numbers)//2:
        median_value = numbers[i]

    if numbers[i] in count_dict:
        count_dict[numbers[i]] += 1
    else :
        count_dict[numbers[i]] = 1


max_count = max(count_dict.values())

if list(count_dict.values()).count(max_count) >= 2:
    count = 0
    for k,v in count_dict.items():
        if v == max_count:
            count += 1
        if count == 2:
            max_key = k
            break
else :
    for k,v in count_dict.items():
        if v == max_count : max_key = k; break
        else : continue;


print(int(round( float(_sum)/len(numbers))))
print(median_value)
print(max_key)
print(numbers[len(numbers)-1] - numbers[0])
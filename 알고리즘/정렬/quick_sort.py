## selection sort

import random
import time

def check_sorted(sequence, N):
    for i in range(N-1):
        if sequence[i] > sequence[i+1]:
            return False
    return True

def move(sequence, left, right):

    low = left
    high = right
    pivot = (high + low) // 2

    pivot_value = sequence.pop(pivot)
    high -= 1

    while low <= high:
        if sequence[low] > pivot_value and sequence[high] < pivot_value:

            temp = sequence[low]
            sequence[low] = sequence[high]
            sequence[high] = temp
            low += 1
            high -= 1

        elif sequence[low] > pivot_value and sequence[high] >= pivot_value:

            high -= 1

        elif sequence[low] <= pivot_value and sequence[high] < pivot_value:

            low += 1
        else :
            low += 1
            high -= 1


    if low <= high:
        sequence.insert(low+1, pivot_value)
        return low+1
    else :
        sequence.insert(high+1, pivot_value)
        return high+1



def quick_sort(sequence, left, right):
    # divide and conquer
    if right - left <= 0:
        return sequence

    pivot = move(sequence, left, right)

    quick_sort(sequence, 0, pivot-1)
    quick_sort(sequence, pivot+1, right)


## make random integer sequence
print("making random sequence...")
N = random.randint(1, 100)
sequence = list()
for i in range(N):
    sequence.append(random.randint(-10000000, 10000000))
# N = 11
# sequence = [5, 3, 8, 10, 10, 4, 9, 1, 6, 2, 7]
## sort start
start = time.time()

print("now sorting...")
quick_sort(sequence, 0, N-1)


end  = time.time()

## check result of sort function
if check_sorted(sequence,N) :
    print("정럴이 잘 되었습니다.")
else :
    print("정렬이 잘 되지 않았습니다.")

print("start : " , start)
print("end : " , end)
print("size of sequence : ", N)
print("time ratio ( size(sequence) / (end-start) ) : ", N/(end-start))


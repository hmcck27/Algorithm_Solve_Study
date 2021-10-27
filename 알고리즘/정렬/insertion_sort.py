## insertion sort

import random
import time

def check_sorted(sequence, N):
    for i in range(N-1):
        if sequence[i] > sequence[i+1]:
            return False
    return True

def insertion_sort(sequence, N):
    for i in range(1, N):
        for j in range(0, i):
            if sequence[j] > sequence[i]:
                pop_object = sequence.pop(i)
                sequence.insert(j, pop_object)

## make random integer sequence
print("making random sequence...")
N = random.randint(1, 10000)
sequence = list()
for i in range(N):
    sequence.append(random.randint(-10000000, 10000000))

## sort start
start = time.time()

print("now sorting...")
insertion_sort(sequence, N)
print("sorted : ", sequence)

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


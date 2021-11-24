## bubble sort

import random
import time

def check_sorted(sequence, N):
    for i in range(N-1):
        if sequence[i] > sequence[i+1]:
            return False
    return True


def bubble_sort(sequence, N):

    for i in range(N-1):
        for j in range(i+1,N):
            if sequence[i] > sequence[j]:
                temp = sequence[i]
                sequence[i] = sequence[j]
                sequence[j] = temp


## make random integer sequence
print("making random sequence...")
N = random.randint(0,100000)
sequence = list()
for i in range(N):
    sequence.append(random.randint(-10000000, 10000000))

## sort start
start = time.time()

print("now sorting...")
bubble_sort(sequence, N)

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


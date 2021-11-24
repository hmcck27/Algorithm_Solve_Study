## shell sort

import random
import time

def check_sorted(sequence, N):
    for i in range(N-1):
        if sequence[i] > sequence[i+1]:
            return False
    return True

def insertion_sort(sub_sequence, index_list):
    for i in range(1,len(index_list)):
        for j in range(0,i):
            if sub_sequence[index_list[i]] < sub_sequence[index_list[j]]:
                temp = sequence[index_list[i]]
                sequence[index_list[i]] = sequence[index_list[j]]
                sequence[index_list[j]] = temp

def shell_sort(sequence, N):

    gap = N

    while gap >= 1 :

        gap = gap // 2
        if gap % 2 == 0:
            gap += 1

        # add sub list
        for i in range(gap):
            temp_index_list = list()
            for j in range(len(sequence)):
                if j % gap == i:
                    temp_index_list.append(j)

            insertion_sort(sequence, temp_index_list)


        if(gap == 1):
            break

## make random integer sequence
print("making random sequence...")
N = random.randint(1, 10000)
sequence = list()
for i in range(N):
    sequence.append(random.randint(-10000000, 10000000))


# N = 11
# sequence = [11, 9, 7, 21, 5, 4, 23, 2, 1, 14, 16]

## sort start
start = time.time()

print("now sorting...")
shell_sort(sequence, N)
# insertion_sort(sequence, N)

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


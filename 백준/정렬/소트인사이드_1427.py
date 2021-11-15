import sys

N = int(sys.stdin.readline())

N_list = [int(i) for i in list(str(N))]

N_list.sort(reverse=True)

print("".join([str(i) for i in N_list]))




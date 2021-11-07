import sys
N = int(sys.stdin.readline().rstrip())
word_list = list()

for i in range(N):
    word_list.append(sys.stdin.readline().rstrip().split())

for i in range(N):
    for j in word_list[i]:
        for k in range(len(j)-1,-1,-1):
            print(j[k], end='')
        print(" ", end='')
    print()

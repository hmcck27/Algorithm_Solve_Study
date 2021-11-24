from sys import stdin

n = int(stdin.readline().rstrip())

array = list()
for _ in range(n):
    input_text = stdin.readline().rstrip()
    array.append(list())
    for i in range(n):
        array[_].append(input_text[i])

# for i in range(n):
#     for j in range(n):
#         print(array[i][j])

max_value = 0

def swap(fir, sec):


def getMaxValue(array):
    for i zlib

def bombonni(array):
    # 가로 체크
    for i in range(n):
        for j in range(n-1):
            if array[i][j] != array[i][j+1]:
                swap((i,j),(i,j+1))
                getMaxValue()
                swap((i,j),(i,j+1))
            if array[j][i] != array[j+1][i]:
                swap((i, j), (i, j + 1))
                getMaxValue()
                swap((i, j), (i, j + 1))

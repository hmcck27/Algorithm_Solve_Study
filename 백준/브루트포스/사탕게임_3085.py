from sys import stdin

n = int(stdin.readline().rstrip())
array = list()
for i in range(n):
    input_ = stdin.readline().rstrip()
    input_list = list()
    for j in range(len(input_)):
        input_list.append(input_[j])
    array.append(input_list)

print(array)

def check_row(i):


def check_col(i, j, max_value):




def swap(tuple1,tuple2):
    temp = array[tuple1[0]][tuple1[1]]
    array[tuple1[0]][tuple1[1]] = array[tuple2[0]][tuple2[1]]
    array[tuple2[0]][tuple2[1]] = temp


def swapCheck(i,j):

    # check col
    if i + 1 < n and j < n and i >= 0 and j >= 0:
        if array[i][j] != array[i+1][j]:
            swap((i,j),(i+1,j))
            for i in range(n):
                max_value = check_row(i,j, max_value)
                max_value = check_col(i,j, max_value)
            swap((i, j), (i + 1, j))

    # check row
    if i < n and j + 1 < n and i >= 0 and j >= 0:
        if array[i][j] != array[i][j + 1]:
            swap((i,j),(i, j+1))
            for i in range(n):
                max_value = check_row(i, max_value)
                max_value = check_col(j, max_value)
            swap((i, j), (i, j + 1))


    return max_value

def bombonni(array):

    for i in range(n):
        for j in range(n):
            swapCheck()





bombonni(array)


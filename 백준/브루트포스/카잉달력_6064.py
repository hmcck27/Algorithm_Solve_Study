import sys
n = int(sys.stdin.readline())
array = list()
for i in range(n):
    temp_list = list(map(int, sys.stdin.readline().split(" ")))
    array.append(temp_list)

def get_year(m,n,x,y):
    count = 1
    temp_x = 1
    temp_y = 1
    while True:
        print(temp_x, temp_y, count, x, y)
        ## 탈출 조건
        if m == temp_x and n == temp_y:
            return -1
        if temp_x == x and temp_y == y:
            return count

        if temp_x < m:
            temp_x += 1
        elif temp_x == m:
            temp_x = 1

        if temp_y < n:
            temp_y += 1
        elif temp_y == n:
            temp_y = 1

        count += 1

def get_year2(m,n,x,y):
    count = 1
    temp_x = 1
    temp_y = 1

    # 먼저 x를 맞춘다.
    count += x - temp_x
    countStep = 0
    temp_x = x
    temp_y = x

    while True :
        # print(temp_x, temp_y, n, count)


        if temp_y == y:
            break
        if countStep > n :
            # print(temp_x, temp_y, n, count, countStep)
            count = -1
            break

        if temp_y == n:
            countStep += 1
            temp_y = 0
        elif temp_y > n:
            temp_y = temp_y - n
        elif temp_y < n:
            countStep += 1
            temp_y = temp_y + m
            count += m


    return count



# print(get_year(temp_list[0],temp_list[1],temp_list[2],temp_list[3]))

for i in array:
    print(get_year2(i[0],i[1],i[2],i[3]))

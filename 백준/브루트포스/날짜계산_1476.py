from sys import stdin

a,b,c = map(int, stdin.readline().split())

i = 0
a_tmp = 0
b_tmp = 0
c_tmp = 0

while True:
    if a_tmp == a and b_tmp == b and c_tmp == c:
        break

    if a_tmp == 15:
        a_tmp = 1
    else:
        a_tmp += 1

    if b_tmp == 28:
        b_tmp = 1
    else:
        b_tmp += 1

    if c_tmp == 19:
        c_tmp = 1
    else:
        c_tmp += 1

    i+=1

print(i)




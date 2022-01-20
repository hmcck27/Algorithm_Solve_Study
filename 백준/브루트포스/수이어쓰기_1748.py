import sys

n = int(sys.stdin.readline())
temp_n = n


## 156의 자릿수를 구하고
count = 0

while True:
    if temp_n < 10 :
        count += 1
        break
    temp_n /= 10
    count += 1



## 자릿수 * 개수 의 반복
ans = 0
ans += count * (n - (10)**(count-1) + 1)
count -= 1



## 2 부터 시작
for i in range(count, 0, -1):

    ans += (i)*(10**(i) - 10**(i-1))

print(ans)





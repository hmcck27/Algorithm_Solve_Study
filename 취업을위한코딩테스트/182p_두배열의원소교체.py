n, m = map(int, input().split())
a_list = list()
b_list = list()

a_list = list(map(int, input().split()))

b_list = list(map(int, input().split()))

a_list.sort()
print(a_list)
b_list.sort(reverse=True)
print(b_list)

for i, (v1, v2) in enumerate(zip(a_list, b_list)):

    if i >= m or v1 > v2 :
        break
    if v1 < v2 :
        temp = a_list[i]
        a_list[i] = b_list[i]
        b_list[i] = temp

print(sum(a_list))

N = int(input())
score_list = list()
for i in range(N):
    input_data = input().split()
    score_list.append((input_data[0], int(input_data[1])))

array = sorted(score_list, key=lambda student:student[1])

for i in array:
    print(i[0], end=' ')
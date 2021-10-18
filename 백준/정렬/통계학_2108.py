'''


문제
수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.

산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이
N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 단, N은 홀수이다. 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.

출력
첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.

둘째 줄에는 중앙값을 출력한다.

셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.

넷째 줄에는 범위를 출력한다.

'''

'''
    sort 한방이면 된다. 무슨 sort를 사용할까 ?

'''


def merge_sort(list) :
    if len(list) <= 1 :
        return list
    mid = len(list)//2
    leftList = list[:mid]
    rightList = list[mid:]
    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)
    return merge(leftList, rightList)

def merge(leftList, rightList):

    merged = list()
    while len(leftList) > 0 or len(rightList) > 0 :
        if len(leftList) > 0 and len(rightList) > 0:
            if leftList[0] < rightList[0] :
                merged.append(leftList[0])
                leftList = leftList[1:]
            else :
                merged.append(rightList[0])
                rightList = rightList[1:]
        elif len(leftList) > 0 :
            merged.append(leftList[0])
            leftList = leftList[1:]
        elif len(rightList) > 0 :
            merged.append(rightList[0])
            rightList = rightList[1:]
    return merged


N = int(input())

numbers = list()

for i in range(N) :
    numbers.append(int(input()))

# sortedList = merge_sort(numbers)

sortedList = sorted(numbers)

sum_ = sortedList[0]
count = len(sortedList)
count_dict = dict()

max_count = 1
temp_count = 1
pre = sortedList[0]
max_num = sortedList[0]


for i in range(1, len(sortedList)) :
    sum_ += sortedList[i]
    if pre == sortedList[i] :
        temp_count += 1
    else :
        temp_count = 1

    if max_count <= temp_count :

        if max_count == temp_count :
            max_num = sortedList[i-1]
        else :
            max_num = sortedList[i]

        max_count = temp_count

    pre = sortedList[i]

# 산술 평균
print(round(sum_/count))

# 중앙값
print(sortedList[count//2])

# 최빈값
print(pre_value)

# 범위
print(sortedList[count-1] - sortedList[0])


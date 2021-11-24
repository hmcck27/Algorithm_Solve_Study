def solution(nums):

    answer = 0

    num_list = list()

    for i in nums:
        if i in num_list :
            continue
        else:
            num_list.append(i)

    if len(num_list) > len(nums)//2 :
        answer = len(nums) // 2
    else :
        answer = len(num_list)

    return answer



nums = [3,1,2,3]

print(solution(nums))
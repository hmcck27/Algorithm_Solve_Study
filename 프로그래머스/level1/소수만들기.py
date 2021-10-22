
prime_num_list = list()
not_prime_list = list()

def primeChk(num):

    if num <= 1:
        return False

    divide_count = 0
    prime_flag = True

    for i in range(1, num+1):
        if i == 1 :
            divide_count += 1
        elif i == num:
            divide_count += 1
        else :
            if num % i == 0:
                prime_flag = False

    if prime_flag == True:
        prime_num_list.append(num)


    return prime_flag



def solution(nums):
    answer = 0

    for i in range(0,len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):

                num1 = nums[i]
                num2 = nums[j]
                num3 = nums[k]


                # print("start by ", i, j ,k , i+j+k)

                if num3+num2+num1 in not_prime_list:
                    continue
                elif num3+num2+num1 in prime_num_list:
                    answer += 1
                elif primeChk(num3+num2+num1):
                    answer += 1
                else :
                    not_prime_list.append(num1+num2+num3)



    return answer


nums = [1,2,3,4]
# nums = [1,2,7,6,4]
print(solution(nums))
print(prime_num_list)
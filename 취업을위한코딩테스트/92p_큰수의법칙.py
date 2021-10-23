def solution(N,M,K,num_list):

    max_value1 = max(num_list)
    num_list.remove(max_value1)
    max_value2 = max(num_list)

    print(max_value1)
    print(max_value2)
    print(M//K)
    print(M%K)


    return max_value1*(M//K)*(K) + max_value2*(M%K)



N = 5
M = 8
K = 3
num_list = [2,4,5,4,6]

N = 5
M = 7
K = 2
num_list = [3,4,3,4,3]

print(solution(N,M,K,num_list))
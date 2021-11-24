import sys
n = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
nums.sort()
print(nums[0]*nums[-1])
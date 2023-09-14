A, B = map(int, input().split())
n = int(input())
nums = list(map(int, input().split()))
nums.reverse()

numA = 0
for i in range(n):
    numA += nums[i] * (A**i)

result = []
while numA:
    result.append(numA % B)
    numA //= B

print(" ".join(map(str, result[::-1])))

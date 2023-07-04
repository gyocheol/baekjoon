N = int(input())
res = 0
p_list = []
m_list = []
z_list = []

for _ in range(N):
    n = int(input())
    if n == 0: z_list.append(n)
    elif n == 1: res += 1
    elif n > 0: p_list.append(n)
    else: m_list.append(n)

p_list.sort()
m_list.sort(reverse=True)

while p_list:
    num1 = p_list.pop()
    if p_list:
        num2 = p_list.pop()
        res += num1 * num2
    else:
        res += num1

while m_list:
    num1 = m_list.pop()
    if m_list:
        num2 = m_list.pop()
        res += num1 * num2
    else:
        if z_list:
            num2 = z_list.pop()
        else:
            res += num1
print(res)
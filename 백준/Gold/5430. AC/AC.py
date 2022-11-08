from collections import deque

for _ in range(int(input())):
    p = input()
    n = int(input())
    arr = deque(input().strip('[]').split(','))
    
    # 이거 안하면 arr에 ['']이 남아있음
    if not n:
        arr = deque()

    flag = 1
    cnt = 0

    for i in p:
        # R의 개수를 보고 뒤집을지 안 뒤집을지 결정
        if i == 'R':
            cnt += 1
        else:
            if arr:
                if not cnt % 2:
                    arr.popleft()
                else:
                    arr.pop()
            # 이거 없을 때 틀림 / arr이 비었을 때 D가 안들어오면 []이 출력되어야 함
            else:
                flag = 0

    if cnt % 2:
        arr.reverse()

    if flag:
        # 이거도 그냥 프린트 때이면 deque붙고 list로 감싸도 str형식에 ,뒤에 띄워져 있음
        print(f"[{','.join(arr)}]")
    else:
        print('error')
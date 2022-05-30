n = int(input())
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
cnt = 1
def compu (n):
    global cnt
    if cnt == n + 1:
        def ques (n):
            list_que = []
            list_que.extend(['"재귀함수가 뭔가요?"','"재귀함수는 자기 자신을 호출하는 함수라네"','라고 답변하였지.'])
            for i in list_que:
                print("____"*n + i)
        return(ques(n))

    elif cnt != n+1:
        list_jal = []
        list_jal.extend(['"재귀함수가 뭔가요?"','"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.','마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.','그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'])
        def jal (n):
            global cnt
            for i in list_jal:
                print("____"*(cnt-1) + i)
            cnt+=1
            if cnt == n + 1:
                return compu(n)
            else:
                return jal(n)
        return(jal(n))

def lastcall (n):
    print("____"*(n-1) + "라고 답변하였지.")
    if n == 1:
        return "라고 답변하였지"
    else:
        n-=1
        return lastcall(n)
compu(n)
lastcall(n)
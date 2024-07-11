class PartyRoomManager:
    def __init__(self, N):
        self.N = N
        self.rooms = [0] * N  # 방의 상태를 0으로 초기화 (0: 빈 방, 1: 사용 중인 방)
        self.allocations = []  # (시작 방 번호, 끝 방 번호, 손님 수)의 리스트
        self.allocation_history = []  # 할당된 방의 히스토리 (시작 방 번호, 끝 방 번호)
    
    def find_empty_rooms(self, Y):
        count = 0
        for i in range(self.N):
            if self.rooms[i] == 0:
                count += 1
                if count == Y:
                    return i - Y + 1
            else:
                count = 0
        return -1

    def new(self, X, Y):
        start = self.find_empty_rooms(Y)
        if start == -1:
            print("REJECTED")
        else:
            for i in range(start, start + Y):
                self.rooms[i] = 1
            self.allocations.append((start, start + Y - 1, X))
            self.allocation_history.append((start, start + Y - 1))
            print(f"{start + 1} {start + Y}")

    def in_(self, A, B):
        start, end, guests = self.allocations[A - 1]
        self.allocations[A - 1] = (start, end, guests + B)
    
    def out(self, A, B):
        start, end, guests = self.allocations[A - 1]
        new_guest_count = guests - B
        if new_guest_count == 0:
            for i in range(start, end + 1):
                self.rooms[i] = 0
            self.allocations[A - 1] = (-1, -1, 0)
            print(f"CLEAN {start + 1} {end + 1}")
        else:
            self.allocations[A - 1] = (start, end, new_guest_count)


# 입력 처리
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
Q = int(data[1])
queries = data[2:]

manager = PartyRoomManager(N)

index = 0
for _ in range(Q):
    command = queries[index]
    if command == 'new':
        X = int(queries[index + 1])
        Y = int(queries[index + 2])
        manager.new(X, Y)
        index += 3
    elif command == 'in':
        A = int(queries[index + 1])
        B = int(queries[index + 2])
        manager.in_(A, B)
        index += 3
    elif command == 'out':
        A = int(queries[index + 1])
        B = int(queries[index + 2])
        manager.out(A, B)
        index += 3

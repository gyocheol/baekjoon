import heapq

def solution(jobs):
    jobs = sorted([(s, l, i) for i, (s, l) in enumerate(jobs)])
    
    heap = []
    time = 0
    idx = 0
    total_turnaround = 0
    n = len(jobs)
    
    while idx < n or heap:

        while idx < n and jobs[idx][0] <= time:
            s, l, num = jobs[idx]
            heapq.heappush(heap, (l, s, num))
            idx += 1
        
        if heap:
            l, s, num = heapq.heappop(heap)
            time += l
            total_turnaround += time - s
        else:
            time = jobs[idx][0]
    
    return total_turnaround // n
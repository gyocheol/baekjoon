while True:
    try:
        seq = list(map(int, input().split()))
        if len(seq) == 2:
            print("Jolly")
            continue
        n = seq[0]
        arr = seq[1:]
        comp_arr = [i for i in range(1, n)]
        for i in range(n-1):
            jolly = abs(arr[i]-arr[i+1])
            if jolly in comp_arr:
                comp_arr.remove(jolly)
        if comp_arr:
            print("Not jolly")
        else:
            print("Jolly")

    except: break
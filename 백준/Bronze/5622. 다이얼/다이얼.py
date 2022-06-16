word = input()

time = {3:["A","B","C"], 4:["D","E","F"], 5:["G","H","I"],6:["J","K","L"],
        7:["M","N","O"], 8:["P","Q","R","S"], 9:["T","U","V"], 10:["W","X","Y","Z"]}

ans = 0
for i in word:
    for j, z in time.items():
        if i in z :
            ans += j
print(ans)
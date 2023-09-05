scores = []
credits = []
avg = 0
total = 0
while True:
    try:
        x, s, c = map(str, input().split())
        scores.append(float(s))
        credits.append(c)
    except : break

for i in range(len(scores)):
    if credits[i] != "P":
        avg += scores[i]
        if credits[i] == "A+":
            total += scores[i] * 4.5
        elif credits[i] == "A0":
            total += scores[i] * 4.0
        elif credits[i] == "B+":
            total += scores[i] * 3.5
        elif credits[i] == "B0":
            total += scores[i] * 3.0
        elif credits[i] == "C+":
            total += scores[i] * 2.5
        elif credits[i] == "C0":
            total += scores[i] * 2.0
        elif credits[i] == "D+":
            total += scores[i] * 1.5
        elif credits[i] == "D0":
            total += scores[i] * 1.0

print(round(total/avg, 6))
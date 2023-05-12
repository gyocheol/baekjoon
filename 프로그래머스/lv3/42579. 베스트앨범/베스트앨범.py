def solution(genres, plays):
    answer = []

    temp = [[genres[i], plays[i], i] for i in range(len(genres))]
    total_genre_d = {}

    temp.sort(key=lambda x:(x[0], -x[1], x[2]))

    for i in temp:
        if i[0] not in total_genre_d:
            total_genre_d[i[0]] = i[1]
        else:
            total_genre_d[i[0]] += i[1]

    total_genre_d = sorted(total_genre_d.items(), key=lambda x: -x[1])

    for i in total_genre_d:
        cnt = 0
        for j in temp:
            if i[0] == j[0]:
                cnt += 1
                if cnt > 2:
                    break
                else:
                    answer.append(j[2])

    return answer
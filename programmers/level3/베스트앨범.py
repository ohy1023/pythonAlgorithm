def solution(genres, plays):
    answer = []
    hash_map = {}
    for i in range(len(genres)):
        if genres[i] in hash_map:
            hash_map[genres[i]].append([plays[i], i])
        else:
            hash_map[genres[i]] = [[plays[i], i]]

    genre_rank = {}
    for genre in hash_map.keys():
        songs = hash_map[genre]
        plays_sum = 0
        for song in songs:
            plays_sum += song[0]
        genre_rank[genre] = plays_sum

    rank = sorted(genre_rank.items(), key=lambda x: x[1], reverse=True)

    for genre in rank:
        song_rank = sorted(hash_map[genre[0]], key=lambda x: (-x[0], x[1]))
        best_two = 0
        for song in song_rank:
            answer.append(song[1])
            best_two += 1
            if best_two == 2:
                break

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))

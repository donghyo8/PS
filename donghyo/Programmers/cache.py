def solution(cacheSize, cities):
    answer = 0
    cache = []

    # 페이지 default 초기화
    for i in range(cacheSize + 1):
        cache.append(0)

    if cacheSize >= 0 and len(cities) <= 100000:
        for i in cities:
            i = i.upper()
            # 해당 리스트에 포함되어 있지 않으면 cache miss
            if not i in cache:
                # cache list의 사이즈와 cache size 비교해 페이지가 꽉차있지 않으면 도시 추가 및 cache miss 시간 누적
                if len(cache) < cacheSize:
                    cache.append(i)
                    answer += 5

                # 페이지가 꽉차있으면 제일 오래 쓰지 않은 원소 제거
                else:
                    cache.pop(0)
                    cache.append(i)
                    answer += 5
                    
            # 포함되어 있으면 해당 인덱스의 원소를 제거하고 cache에 새로운 원소 추가
            # cache hit 시간 누적
            else:
                cache.pop(cache.index(i))
                cache.append(i)
                answer += 1
    return answer

cacheSize = 0
cities1 = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
cities2 = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
cities3 = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
cities4 = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
cities5 = ["Jeju", "Pangyo", "NewYork", "newyork"]
cities6 = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]

solution(cacheSize, cities6)
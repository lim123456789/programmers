from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)
    
    cache = deque()
    cache_set = set()
    total_time = 0
    
    for city in cities:
        city = city.lower()
        if city in cache_set:
            total_time += 1
            cache.remove(city)
            cache.append(city)
        else:
            total_time += 5
            if len(cache) >= cacheSize:
                removed_city = cache.popleft()
                cache_set.remove(removed_city)
            cache.append(city)
            cache_set.add(city)
    
    return total_time
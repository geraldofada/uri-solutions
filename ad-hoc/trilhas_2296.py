hikes = int(input())
result = {} 
result_back = {}

for i in range(hikes):
    hike_points = list(map(int, input().split()))

    total_elevation = 0
    for now, nxt in zip(hike_points[1:], hike_points[2:]):
        if nxt > now:
            total_elevation += nxt - now
    
    total_elevation_back = 0
    for now, nxt in zip(hike_points[:0:-1], hike_points[-2:0:-1]):
        if nxt > now:
            total_elevation_back += nxt - now
    
    result[i+1] = total_elevation
    result_back[i+1] = total_elevation_back

result_min = min(result, key=result.get)
result_back_min = min(result_back, key=result_back.get)

if result_min < result_back_min:
    print(result_min)
else:
    print(result_back_min)
# def solution(dirs):    
#     location = set()
#     x,y = 0,0
    
#     for route in dirs:
#         if route == 'U':
#             if (y < 5):
#                 y += 1
#         elif route == 'D':
#             if (y > -5):
#                 y -= 1
#         elif route == 'R':
#             if (x < 5):
#                 x += 1
#         else:
#             if (x > -5):
#                 x -= 1
#         location.add((x,y))
#     print(location)
#     return len(location)

# 로직
# 1. 튜플은 변경이 불가한 타입이므로 x,y 변수에 각각 0 할당
# 2. 경로에 맞춰 이동하면서, 이동이 끝나면 set 타입을 가진 변수, locations에 현재 좌표 추가
# 방문한 좌표 X, 이동한 경로의 개수를 구해야 하는 문제

def solution(dirs):
    x, y = 0, 0           # 시작 위치 (0,0)
    visited = set()       # 방문한 경로(에지)를 저장할 집합

    for move in dirs:
        nx, ny = x, y     # 이동 전 위치에서 출발
        if move == 'U':
            if y < 5:
                ny += 1
            else:
                continue
        elif move == 'D':
            if y > -5:
                ny -= 1
            else:
                continue
        elif move == 'R':
            if x < 5:
                nx += 1
            else:
                continue
        elif move == 'L':
            if x > -5:
                nx -= 1
            else:
                continue
        
        # 현재 위치와 새 위치 사이의 경로를 정렬하여 저장 (양방향 동일 취급)
        edge = ((x, y), (nx, ny)) if (x, y) < (nx, ny) else ((nx, ny), (x, y))
        visited.add(edge)
        
        # 현재 위치 업데이트
        x, y = nx, ny

    return len(visited)

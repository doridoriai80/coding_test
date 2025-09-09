

def solution(X, Y, D):
    # 남은 거리
    distance = Y - X
    # 필요한 점프 횟수 (올림 연산)
    jumps = (distance + D - 1) // D
    return jumps

print(solution(10, 85, 30))


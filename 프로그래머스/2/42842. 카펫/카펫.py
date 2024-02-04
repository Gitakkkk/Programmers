def solution(brown, yellow):
    answer = [0, 0]

    full = brown + yellow 

    for i in range(1, full):
        if full % i == 0:
            width = full / i
            height = i
            if width * 2 + height * 2 - 4 == brown:
                answer[0] = width
                answer[1] = height
                break

    return answer
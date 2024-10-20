# 시간 복잡도 : O(N*2log(N*2))

def solution(numbers):
    answer = []
    
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    
    set_answer = set(answer)  # 리스트를 바로 집합으로 변환
    sorted_answer = sorted(set_answer)  # 집합을 정렬
    return sorted_answer

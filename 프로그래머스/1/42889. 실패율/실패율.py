# def solution(N, stages):
#     answer = []
    
#     # 참여자 수
#     a = len(stages)
#     # 스테이지, 1부터 시작
#     b = 1
#     # 실패율 배열
#     c = [100] * len(stages)
#     # 실패한 참여자 수
#     d = 0
    
#     while b > N:
#         for i  in range(len(stages):
#             if stages[i] == b:
#                 d += 1
#             if i == len(stages-1):
#                 c[i] = d / a
    
#     for failPercent in c:
#         if failPercent in 
    
#     return answer

# [생각한 로직]
# 1. 반복문을 돌며 b(현재 스테이지)가 참여자가 멈춰있는 스테이지와 동일하다면 d(실패한 참여자 수) +=1
# 2. stages의 마지막 값에 접근한 경우, 실패율 계산하여 c(실패율 배열)에 해당 스테이지의 실패율 추가
# 3. c 배열 반복문 돌며 낮은 순으로 정렬하여 응답
# 3-1. 0번째부터 N번째까지 단순 반복문으로 진행되는 경우, ...

def solution(N, stages):
    answer = []
    total_players = len(stages)
    failure_rates = {}

    for stage in range(1, N+1):
        if total_players == 0:
            failure_rates[stage] = 0
        else:
            # 현재 스테이지에 머물고 있는 플레이어 수
            count = stages.count(stage)
            failure_rates[stage] = count / total_players
            # 다음 스테이지로 넘어가기 위해 현재 스테이지에서 실패한 플레이어는 제외
            total_players -= count

    # 실패율이 높은 순, 동일할 경우 스테이지 번호가 낮은 순으로 정렬
    answer = sorted(failure_rates, key=lambda x: (-failure_rates[x], x))
    return answer
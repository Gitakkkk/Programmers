# 시간복잡도 : O(N)
# 1번 : 1,2,3,4,5
# 2번 : 2,1,2,3,2,4,2,5
# 3번 : 3,3,1,1,2,2,4,4,5,5

# def solution(answers):    
#     a = [1,2,3,4,5]
#     b = [2,1,2,3,2,4,2,5]
#     c = [3,3,1,1,2,2,4,4,5,5]
    
#     cnt  = [{1:0}, {2:0}, {3:0}]
    
#     for i in range(len(answers)):
#         if (answers[i] == i % len(a)):
#             cnt[0].value += 1
#         if (answers[i] == i % len(b)):
#             cnt[1].value += 1
#         if (answers[i] == i % len(c)):
#             cnt[2].value += 1
    
#     if ()
    
#     return [max(cntA, cntB, cntC)]

def solution(answers):
    patterns = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]
    
    scores = [0]*3
    
    for i, answer in enumerate(answers):
        for j, pattern in enumerate(patterns):
            if answer == pattern[i % len(pattern)]:
                scores[j] += 1
    
    maxScore = max(scores)
    
    highestScores = []
    for i, score in enumerate(scores):
        if score == maxScore:
            highestScores.append(i+1)
                        
    return highestScores
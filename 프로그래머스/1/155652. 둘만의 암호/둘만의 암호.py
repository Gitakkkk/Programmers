def solution(s, skip, index):
    answer = ''
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(skip)):
        alphabet = alphabet.replace(skip[i], '')
    for i in range(len(s)):
        idx = (alphabet.index(s[i]) + index) % len(alphabet)
        answer += alphabet[idx]
    
    return answer
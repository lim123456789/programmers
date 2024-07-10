def solution(s):
    words = s.split(' ')
    JCwords = []
    
    for word in words:
            JCwords.append(word.capitalize())
          
    answer = ' '.join(JCwords)
    return answer

if __name__ == "__main__":
    s = input("문자열 입력: ")
    print(solution(s))
def generate_words(current, length, words, vowels):
    if len(current) == length:
        words.append(current)
        return
    
    for vowel in vowels:
        generate_words(current + vowel, length, words, vowels)
        
def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    words = []
    
    for length in range(1, 6):
        generate_words("", length, words, vowels)

    words.sort()
    answer = words.index(word) + 1
    
    return answer
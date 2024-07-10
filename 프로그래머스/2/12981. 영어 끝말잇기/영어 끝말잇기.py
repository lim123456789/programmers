def solution(n, words):
    wordlist = set()
    wordlist.add(words[0]) 

    for i in range(1, len(words)):
        if (words[i] in wordlist) or (words[i-1][-1] is not words[i][0]):
            return [(i % n) + 1, (i // n) + 1]
        wordlist.add(words[i])
        
    return [0, 0]
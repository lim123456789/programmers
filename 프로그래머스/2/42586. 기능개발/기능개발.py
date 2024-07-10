def solution(progresses, speeds):
    from math import ceil
    
    leftdays = [ceil((100 - progress) / speed) for progress, speed in zip(progresses, speeds)]

    answer = []

    deploy = leftdays[0]
    count = 0
    
    for day in leftdays:
        if day <= deploy:
            count += 1
        else:
            answer.append(count)
            deploy = day
            count = 1

    answer.append(count)
    
    return answer
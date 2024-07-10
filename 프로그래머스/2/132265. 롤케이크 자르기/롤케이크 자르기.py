from collections import Counter

def solution(topping):
    left_toppings = set()
    right_toppings = Counter(topping)
    
    fair = 0
    
    for t in topping:
        left_toppings.add(t)
        right_toppings[t] -= 1
        
        if right_toppings[t] == 0:
            del right_toppings[t]
        
        if len(left_toppings) == len(right_toppings):
            fair += 1
    
    return fair
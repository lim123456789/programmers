def solution(want, number, discount):
    from collections import Counter
    
    want_dict = {want[i]: number[i] for i in range(len(want))}
    
    total_days = len(discount)
    discount_days = 10
    valid_days = 0

    current_window = Counter(discount[:discount_days])
    
    if all(current_window.get(product, 0) >= want_dict[product] for product in want_dict):
        valid_days += 1
    
    for i in range(1, total_days - discount_days + 1):
        current_window = Counter(discount[i:discount_days+i])
        
        if all(current_window.get(product, 0) >= want_dict[product] for product in want_dict):
            valid_days += 1
    
    return valid_days
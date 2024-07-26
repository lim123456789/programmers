from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0 
    bridge = deque()  
    current_weight = 0  
    
    while truck_weights or bridge:        
        time += 1

        if bridge and bridge[0][1] == time:
            _, _time = bridge.popleft()
            current_weight -= _

        if truck_weights:
            if current_weight + truck_weights[0] <= weight and len(bridge) < bridge_length:
                truck = truck_weights.pop(0)
                current_weight += truck
                bridge.append((truck, time + bridge_length))
    
    return time
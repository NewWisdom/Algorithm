def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_on = [0]* bridge_length
    while truck_weights:
        answer +=1
        bridge_on.pop(0)
        if sum(bridge_on) + truck_weights[0] > weight :
            bridge_on.append(0)
        else:
            bridge_on.append(truck_weights.pop(0))
    while sum(bridge_on)>0:
        answer +=1
        bridge_on.pop(0)
    return answer
def solution(money, expected, actual):
    bet = 100
    for i in range(len(expected)):
        if money <= bet :
            bet = money
        if expected[i] == actual[i]:
            money+=bet
            bet = 100
        else :
            money -= bet
            bet *=2
        if money < 0:
            money = 0
            break
    return money

print(solution(1200,	['T', 'T', 'H', 'H', 'H'],	['H', 'H', 'T', 'H', 'T']))
def answer(x):
    weight = 0
    total = 0
    pows = []
    weights = []
    left = x
    right = 0
    while total < x:
        total += 3 ** weight
        pows.append(3 ** weight)
        weight += 1

    weight -= 1
    right = pows[weight]
    weights.append('R')
    weight -= 1
    while weight >= 0:
        diff  = left - right
        if diff > 0:
            diff = abs(diff)
            if diff == pows[weight]:
                weights.insert(0, 'R')
                right += pows[weight]
            elif diff > pows[weight]/2:
                weights.insert(0, 'R')
                right += pows[weight]
            else:
                weights.insert(0, '-')
        elif diff < 0:
            diff = abs(right - left)
            if diff == pows[weight]:
                weights.insert(0, 'L')
                left += pows[weight]
            elif diff > pows[weight]/2:
                weights.insert(0, 'L')
                left  += pows[weight]
            else:
                weights.insert(0, '-')
        else:
            weights.insert(0,'-')
        weight -= 1
    return ','.join(weights)

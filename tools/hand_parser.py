RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
straight_hands = []
for i in range(len(RANKS) - 5 + 1):
    straight_hands.append(RANKS[i:i+5])


def is_flush(hand):
    suits = [c[0] for c in hand]
    return True if len(set(suits)) == 1 else False


def is_straight(hand):
    ranks = [r[1:] for r in hand]
    res = False
    for p_h in straight_hands:
        if set(ranks) == set(p_h):
            res = True
            break
    return res


def is_straight_flush(hand):
    return True if is_flush(hand) and is_straight(hand) else False


def is_royal_flush(hand):
    return True if is_flush(hand) and is_straight(hand) and set([r[1:] for r in hand]) == {'A', 'K', 'Q', 'J',
                                                                                           '10'} else False


def is_four(hand):
    ranks = [r[1:] for r in hand]
    r_d = {}
    for r in ranks:
        if r in r_d.keys():
            r_d[r] += 1
        else:
            r_d[r] = 1
    return True if 4 in list(r_d.values()) else False


def is_full_house(hand):
    ranks = [r[1:] for r in hand]
    r_d = {}
    for r in ranks:
        if r in r_d.keys():
            r_d[r] += 1
        else:
            r_d[r] = 1

    return True if 3 in list(r_d.values()) and 2 in list(r_d.values()) else False


def is_three(hand):
    ranks = [r[1:] for r in hand]
    r_d = {}
    for r in ranks:
        if r in r_d.keys():
            r_d[r] += 1
        else:
            r_d[r] = 1

    return True if 3 in list(r_d.values()) else False


def is_two_pairs(hand):
    ranks = [r[1:] for r in hand]
    r_d = {}
    for r in ranks:
        if r in r_d.keys():
            r_d[r] += 1
        else:
            r_d[r] = 1
    return True if len(list(r_d.values())) == 3 else False


def is_pair(hand):
    ranks = [r[1:] for r in hand]
    r_d = {}
    for r in ranks:
        if r in r_d.keys():
            r_d[r] += 1
        else:
            r_d[r] = 1
    return True if 2 in list(r_d.values()) else False


def parse(hand):
    if is_royal_flush(hand):
        return "ROYAL FLUSH"
    elif is_straight_flush(hand):
        return "STRAIGHT FLUSH"
    elif is_four(hand):
        return "FOUR"
    elif is_full_house(hand):
        return "FULL HOUSE"
    elif is_flush(hand):
        return "FLUSH"
    elif is_straight(hand):
        return "STRAIGHT"
    elif is_three(hand):
        return "THREE"
    elif is_two_pairs(hand):
        return "TWO PAIRS"
    elif is_pair(hand):
        return "PAIR"
    else:
        return "???"


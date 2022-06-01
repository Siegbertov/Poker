RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
straight_hands = []
for i in range(len(RANKS) - 5 + 1):
    straight_hands.append(RANKS[i:i+5])
rank_map = {
        'A': 1,
        'K': 2,
        'Q': 3,
        'J': 4,
        '10': 5,
        '9': 6,
        '8': 7,
        '7': 8,
        '6': 9,
        '5': 10,
        '4': 11,
        '3': 12,
        '2': 13
    }


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


def sort_hand(hand: list, is_card=True):
    if is_card:
        return rank_map[hand[1:]]
    else:
        return rank_map[hand]


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
        return "HIGH HAND"


def extra_parse(hand: list, name: str):
    if name == "ROYAL FLUSH":
        return name

    elif name == "STRAIGHT FLUSH":
        hand_sorted = [el[1:] for el in sorted(hand, key=sort_hand)]
        if hand_sorted[1] == "5":
            return "5"
        else:
            return hand_sorted[0]

    elif name == "FOUR":
        ranks = [r[1:] for r in hand]
        r_d = {}
        for r in ranks:
            if r in r_d.keys():
                r_d[r] += 1
            else:
                r_d[r] = 1
        for k, v in r_d.items():
            if v == 4:
                return k

    elif name == "FULL HOUSE":
        ranks = [r[1:] for r in hand]
        r_d = {}
        for r in ranks:
            if r in r_d.keys():
                r_d[r] += 1
            else:
                r_d[r] = 1
        r_d = dict(sorted(r_d.items(), key=lambda x: x[1], reverse=True))
        return "+".join(list(r_d.keys()))

    elif name == "FLUSH":
        return "+".join([c[1:] for c in sorted(hand, key=sort_hand)])

    elif name == "STRAIGHT":
        hand_sorted = [el[1:] for el in sorted(hand, key=sort_hand)]
        if hand_sorted[1] == "5":
            return "5"
        else:
            return hand_sorted[0]
    elif name == "THREE":
        ranks = [r[1:] for r in hand]
        r_d = {}
        for r in ranks:
            if r in r_d.keys():
                r_d[r] += 1
            else:
                r_d[r] = 1
        for k, v in r_d.items():
            if v == 3:
                return k

    elif name == "TWO PAIRS":
        ranks = [r[1:] for r in hand]
        r_d = {}
        for r in ranks:
            if r in r_d.keys():
                r_d[r] += 1
            else:
                r_d[r] = 1
        r_d = dict(sorted(r_d.items(), key=lambda x: x[1], reverse=True))
        r_d.popitem()
        return "+".join(sorted(list(r_d.keys()), key=lambda x: rank_map[x]))

    elif name == "PAIR":
        ranks = [r[1:] for r in hand]
        r_d = {}
        for r in ranks:
            if r in r_d.keys():
                r_d[r] += 1
            else:
                r_d[r] = 1
        for k, v in r_d.items():
            if v == 2:
                return k

    elif name == "HIGH HAND":
        return sorted(hand, key=sort_hand)[0][1:]
    else:
        return "???"


if __name__ == "__main__":
    hand = ['♣A', '♣2', '♣3', '♣4', '♣5']


    def func(hand):
        return "+".join([c[1:] for c in sorted(hand, key=sort_hand)])


    print(func(hand))



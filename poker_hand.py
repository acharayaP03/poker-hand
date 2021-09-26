
#!/usr/bin/env python3

# for looping large number of data stream 
from itertools import groupby


"""
    Poker Hand: 
    Read poker_hand.txt.
    Create High card number for 'T', 'J', 'Q', 'K' and 'A' as 10,11,12,13,14 and combine with range(2, 10) 
    and save it to card_value variable.
"""

# Card Value for cards above 10
card_value = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

# update card_value while inserting all numbers from 0 to 9
card_value.update((str(low_card), low_card) for low_card in [2,3,4,5,6,7,8,9])
# print(card_value)

def result(hand):
    """
        result function will receive cards hands dealt to each player as a tuple
        then we will extract the first index of it 
    """
    sorted_hand = sorted([c[0] for c in hand], reverse=True)
    # seconds index in tuple is suits 
    suits = [s[1] for s in hand]
    # return false if hand is not straight    
    straights = (sorted_hand == list(range(sorted_hand[0], sorted_hand[0]-5, -1)))
    
    flush = all(suit == suits[0] for suit in suits)

    if straights and flush: return 8, sorted_hand[1]
    if flush: return 5, sorted_hand
    if straights: return 4, sorted_hand[1]

    three_of_kinds = []
    two_of_kinds = []
    for v, group in groupby(sorted_hand):
       
        cc = sum(1 for _ in group)
        
        if cc == 4: return 7, v, sorted_hand, print(v, sorted_hand)
        elif cc == 3: three_of_kinds.append(v)
        elif cc == 2: two_of_kinds.append(v)

    if three_of_kinds: return (6 if two_of_kinds else 3), three_of_kinds, two_of_kinds, sorted_hand
    return len(two_of_kinds), two_of_kinds, sorted_hand


player_one = 0
player_two = 0
with open("poker_hand.txt") as file:
    for lines in file:
        cards = [(card_value[line[0]], line[1]) for line in lines.split(' ')]
        player_one += result(cards[:5]) > result(cards[5:])
        player_two += result(cards[:5]) < result(cards[5:])

print(f"Player 1: {player_one}")
print(f"Player 2: {player_two}")
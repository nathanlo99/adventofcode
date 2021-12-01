
import sys

player = -1
hands = [[], []]
for line in sys.stdin.readlines():
    line = line.strip()
    if line.startswith("Player"):
        player += 1
    elif line != "":
        hands[player].append(int(line))

def play_normal_round(hand1, hand2):
    if not hand1:
        return False, hand1, hand2
    elif not hand2:
        return False, hand1, hand2
    else:
        top_card1, top_card2 = hand1[0], hand2[0]
        if top_card1 > top_card2:
            return True, hand1[1:] + [top_card1, top_card2], hand2[1:]
        else:
            return True, hand1[1:], hand2[1:] + [top_card2, top_card1]

def play_recursive_round(hand1, hand2):
    if not hand1:
        return 2, hand1, hand2
    elif not hand2:
        return 1, hand1, hand2
    else:
        top_card1, hand1, top_card2, hand2 = hand1[0], hand1[1:], hand2[0], hand2[1:]
        if len(hand1) >= top_card1 and len(hand2) >= top_card2:
            winner, end1, end2 = play_recursive_game(hand1[:top_card1], hand2[:top_card2])
            if winner == 1:
                return 0, hand1 + [top_card1, top_card2], hand2
            elif winner == 2:
                return 0, hand1, hand2 + [top_card2, top_card1]
        elif top_card1 > top_card2:
            return 0, hand1 + [top_card1, top_card2], hand2
        else:
            return 0, hand1, hand2 + [top_card2, top_card1]

def play_recursive_game(hand1, hand2):
    game_number = play_recursive_game.count
    play_recursive_game.count += 1
    seen = set()
    # print("Starting a game with", hand1, hand2)
    round_num = 1
    while True:
        # print("Game", game_number, "round", round_num, hand1, hand2)
        round_num += 1
        key = (tuple(hand1 + hand2), len(hand1))
        if key in seen:
            return 1, hand1, hand2
        seen.add(key)
        result, new_hand1, new_hand2 = play_recursive_round(hand1, hand2)
        if result > 0:
            assert result in (1, 2)
            return result, hand1, hand2
        else:
            hand1, hand2 = new_hand1, new_hand2

play_recursive_game.count = 1

def calculate_score(hand):
    print(hand)
    return sum((len(hand) - idx) * card for idx, card in enumerate(hand))

"""
hand1, hand2 = hands[0], hands[1]
while True:
    # print(hand1, hand2)
    result, new_hand1, new_hand2 = play_normal_round(hand1, hand2)
    if not result:
        print(calculate_score(new_hand1 + new_hand2))
        break
    else:
        hand1, hand2 = new_hand1, new_hand2
"""

hand1, hand2 = hands[0], hands[1]
result, end1, end2 = play_recursive_game(hand1, hand2)
print(calculate_score(end1 + end2))

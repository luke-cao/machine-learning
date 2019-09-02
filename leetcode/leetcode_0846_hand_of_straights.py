from typing import List
from collections import Counter


class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W:
            return False
        hand_counter = Counter(hand)
        counter_keys = sorted(hand_counter)
        while counter_keys:
            min_card_num = counter_keys[0]
            min_card_count = hand_counter[min_card_num]
            for i in range(W):
                curr_card_num = min_card_num + i
                if not hand_counter[curr_card_num]:
                    return False
                hand_counter[curr_card_num] = hand_counter[curr_card_num] - min_card_count
                if hand_counter[curr_card_num] < 0:
                    return False
                elif hand_counter[curr_card_num] == 0:
                    del hand_counter[curr_card_num]
                    counter_keys.remove(curr_card_num)
        return True



hand = [1,2,3,6,2,3,4,7,8]
w = 3
print(Solution().isNStraightHand(hand, w))

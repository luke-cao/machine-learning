from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        """
        5 is most convenient bill, so it has lowest priority to pay back to customer.
        changes: list

        :param bills:
        :return:
        """

        changes = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            if bill == 5:
                changes[5] += 1
            elif bill == 10:
                if changes[5] > 0:
                    changes[10] += 1
                    changes[5] -= 1
                else:
                    return False
            elif bill == 20:
                if changes[10] >= 1 and changes[5] >= 1:
                    changes[20] += 1
                    changes[10] -= 1
                    changes[5] -= 2
                elif changes[5] >= 3:
                    changes[20] += 1
                    changes[5] -= 3
                else:
                    return False
        return True


input = [5,5,5,10,20]
input2 = [5,5,5,5,20,20,5,5,5,5]
print(Solution().lemonadeChange(input))
print(Solution().lemonadeChange(input2))
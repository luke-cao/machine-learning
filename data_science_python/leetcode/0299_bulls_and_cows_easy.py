from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        """
        secret and guess have the same length
        :param secret:
        :param guess:
        :return:
        """
        bulls = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
        intersection = Counter(secret) & Counter(guess)
        cows = sum(intersection.values()) - bulls
        return f'{bulls}A{cows}B'





def stringToString(input):
    import json

    return json.loads(input)


def main():
    import sys
    import io

    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            secret = stringToString(line)
            line = next(lines)
            guess = stringToString(line)

            ret = Solution().getHint(secret, guess)

            out = (ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()

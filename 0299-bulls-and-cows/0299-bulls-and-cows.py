class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bullsCount = 0
        cowsCount = 0
        bullMap = defaultdict(int)
        n = len(secret)
        bullsVisited = set()
        for i in range(n):
            digit = secret[i]
            if secret[i] == guess[i]:
                bullsCount += 1
                bullsVisited.add(i)
            else:
                bullMap[digit] += 1
        for i in range(len(guess)):
            g = guess[i]
            if i not in bullsVisited:
                if bullMap[g] > 0:
                    cowsCount += 1
                    bullMap[g] -= 1
        
        return str(bullsCount) + "A" + str(cowsCount) + "B"
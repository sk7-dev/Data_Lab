class Solution:
    def isHappy(self, n: int) -> bool:
        squares = {0:0, 1: 1, 2:4, 3:9, 4:16, 5:25, 6:36, 7:49, 8:64, 9:81}
        visited = set()
        while n != 2:
            squareNum = 0
            while n > 0:
                dig = n % 10
                squareNum += squares[dig]
                n //= 10
            if squareNum in visited:
                return False
            if squareNum == 1:
                return True
            n = squareNum
            visited.add(squareNum)
        return False
class Solution:
    MOD = (10**9 +7)

    def countHousePlacements(self, n: int) -> int:
        a = [0,0]
        self.FastDoubling(n+2,a)
        return ((a[0] % self.MOD) ** 2) % self.MOD
        
    def FastDoubling(self, n, res):
        if (n == 0):
            res[0] = 0
            res[1] = 1
            return
        self.FastDoubling((n // 2), res)
 
        a = res[0]
        b = res[1]
 
        c = 2 * b - a
 
        if (c < 0):
            c += self.MOD
        c = (a * c) % self.MOD
 

        d = (a * a + b * b) % self.MOD
 

        if (n % 2 == 0):
            res[0] = c
            res[1] = d
        else:
            res[0] = d
            res[1] = c + d


if __name__ == "__main__":
    s = Solution()
    print(s.countHousePlacements(9)) # 4
    print(s.countHousePlacements(2)) # 9
    print(s.countHousePlacements(3)) # 25
    print(s.countHousePlacements(5)) # 169
    print(s.countHousePlacements(8000)) # 
    """
    7921
    9
    25
    169
    47869168
    """
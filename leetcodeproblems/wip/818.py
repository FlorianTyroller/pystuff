class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        i = 1
        while i-1 < target:
            i*=2
        return i

if __name__ == "__main__":
    s = Solution()
    print(s.racecar(1)) # A
    print(s.racecar(2)) # ARRA , AARA
    print(s.racecar(3)) # AA
    print(s.racecar(4)) # ARRAA, AARRA
    print(s.racecar(5)) # ARRAARA
    print(s.racecar(6)) # AAARA
    print(s.racecar(7)) # AAA

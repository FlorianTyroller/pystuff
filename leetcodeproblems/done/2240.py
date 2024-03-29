class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        s = 0
        for i in range(total//cost1 + 1):
            t = total - cost1*i
            s += t//cost2 + 1
        return s


if __name__ == "__main__":
    s = Solution()
    print(s.waysToBuyPensPencils(20, 10, 5))